#!/usr/bin/env python3
"""
Script to update all README.md files in the art project tree,
adding CDN FQDN to image references and links.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

# Configuration
CDN_BASE_URL = "https://cdn.naida.ai/art"  # Change this to your CDN FQDN
DRY_RUN = False  # Set to False to actually modify files

def find_readme_files(root_dir: str) -> List[Path]:
    """Find all README.md files recursively in the directory tree."""
    root_path = Path(root_dir)
    readme_files = []
    
    for readme_path in root_path.rglob("README.md"):
        readme_files.append(readme_path)
    
    return sorted(readme_files)

def get_relative_dir_from_root(readme_path: Path, root_dir: str) -> str:
    """Get the relative directory path from the root directory."""
    root_path = Path(root_dir)
    relative_path = readme_path.parent.relative_to(root_path)
    
    # Convert to URL-style path (forward slashes)
    if str(relative_path) == ".":
        return ""
    return str(relative_path).replace("\\", "/")

def update_markdown_urls(content: str, base_cdn_url: str, relative_dir: str) -> Tuple[str, int]:
    """
    Update markdown image references and links to use CDN URLs.
    
    Returns: (updated_content, number_of_changes)
    """
    changes = 0
    
    # Build the full CDN path for this directory
    if relative_dir:
        cdn_dir_url = f"{base_cdn_url}/{relative_dir}"
    else:
        cdn_dir_url = base_cdn_url
    
    # Pattern 1: Image references ![](path) and ![alt](path)
    def replace_image_ref(match):
        nonlocal changes
        alt_text = match.group(1) if match.group(1) else ""
        image_path = match.group(2)
        
        # Skip if already has http/https
        if image_path.startswith(('http://', 'https://')):
            return match.group(0)
        
        # Remove leading ./ if present
        clean_path = image_path.lstrip('./')
        
        changes += 1
        return f"![{alt_text}]({cdn_dir_url}/{clean_path})"
    
    # Pattern 2: Link references [![](thumb)](full) - clickable images
    def replace_clickable_image(match):
        nonlocal changes
        thumb_path = match.group(1)
        full_path = match.group(2)
        
        # Skip if already has http/https
        if thumb_path.startswith(('http://', 'https://')) and full_path.startswith(('http://', 'https://')):
            return match.group(0)
        
        # Clean paths
        clean_thumb = thumb_path.lstrip('./') if not thumb_path.startswith(('http://', 'https://')) else thumb_path
        clean_full = full_path.lstrip('./') if not full_path.startswith(('http://', 'https://')) else full_path
        
        # Update paths if they're relative
        if not thumb_path.startswith(('http://', 'https://')):
            clean_thumb = f"{cdn_dir_url}/{clean_thumb}"
            changes += 1
        
        if not full_path.startswith(('http://', 'https://')):
            clean_full = f"{cdn_dir_url}/{clean_full}"
            changes += 1
        
        return f"[![]({clean_thumb})]({clean_full})"
    
    # Pattern 3: Regular links [text](url) - but only update relative URLs
    def replace_link(match):
        nonlocal changes
        link_text = match.group(1)
        url = match.group(2)
        
        # Skip if already has http/https or is an anchor link
        if url.startswith(('http://', 'https://', '#')):
            return match.group(0)
        
        # Only update if it looks like a relative path to an image or local resource
        if any(url.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']):
            clean_url = url.lstrip('./')
            changes += 1
            return f"[{link_text}]({cdn_dir_url}/{clean_url})"
        
        return match.group(0)
    
    # Apply replacements in order
    # 1. First handle clickable images [![](thumb)](full)
    content = re.sub(r'\[\!\[\]\(([^)]+)\)\]\(([^)]+)\)', replace_clickable_image, content)
    
    # 2. Then handle simple image references ![](path) or ![alt](path)
    content = re.sub(r'\!\[([^\]]*)\]\(([^)]+)\)', replace_image_ref, content)
    
    # 3. Finally handle regular links [text](url) for image files
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
    
    return content, changes

def process_readme_file(readme_path: Path, root_dir: str, cdn_base_url: str, dry_run: bool = True) -> Tuple[int, str]:
    """
    Process a single README.md file.
    
    Returns: (number_of_changes, status_message)
    """
    try:
        # Read the file
        with open(readme_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Get relative directory
        relative_dir = get_relative_dir_from_root(readme_path, root_dir)
        
        # Update URLs
        updated_content, changes = update_markdown_urls(original_content, cdn_base_url, relative_dir)
        
        if changes > 0:
            if not dry_run:
                # Write back to file
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                status = f"✅ Updated {changes} URLs"
            else:
                status = f"🔍 Would update {changes} URLs (DRY RUN)"
        else:
            status = "⚪ No changes needed"
        
        return changes, status
        
    except Exception as e:
        return 0, f"❌ Error: {str(e)}"

def main():
    """Main function to process all README files."""
    root_directory = "/Users/uli/projects/apigeek.net/art"
    
    print(f"🔍 Scanning for README.md files in: {root_directory}")
    print(f"📡 CDN Base URL: {CDN_BASE_URL}")
    print(f"🧪 Dry Run Mode: {'ON' if DRY_RUN else 'OFF'}")
    print("-" * 60)
    
    # Find all README files
    readme_files = find_readme_files(root_directory)
    
    if not readme_files:
        print("❌ No README.md files found!")
        return
    
    print(f"📄 Found {len(readme_files)} README.md files:")
    print()
    
    total_changes = 0
    
    # Process each file
    for readme_path in readme_files:
        relative_path = readme_path.relative_to(Path(root_directory))
        changes, status = process_readme_file(readme_path, root_directory, CDN_BASE_URL, DRY_RUN)
        
        print(f"{relative_path}: {status}")
        total_changes += changes
    
    print()
    print("-" * 60)
    print(f"📊 Summary: {total_changes} total URL updates {'would be made' if DRY_RUN else 'completed'}")
    
    if DRY_RUN and total_changes > 0:
        print()
        print("💡 To apply changes, set DRY_RUN = False in the script")

if __name__ == "__main__":
    main()
