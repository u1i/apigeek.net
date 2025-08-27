#!/usr/bin/env python3
"""
Test script to show what changes would be made to products/README.md
and test if CDN URLs are accessible.
"""

import re
import requests
from pathlib import Path
from typing import Tuple

CDN_BASE_URL = "https://cdn.naida.ai/art"

def update_markdown_urls(content: str, base_cdn_url: str, relative_dir: str) -> Tuple[str, int]:
    """Update markdown image references and links to use CDN URLs."""
    changes = 0
    
    # Build the full CDN path for this directory
    if relative_dir:
        cdn_dir_url = f"{base_cdn_url}/{relative_dir}"
    else:
        cdn_dir_url = base_cdn_url
    
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
    
    # Apply replacements
    content = re.sub(r'\[\!\[\]\(([^)]+)\)\]\(([^)]+)\)', replace_clickable_image, content)
    content = re.sub(r'\!\[([^\]]*)\]\(([^)]+)\)', replace_image_ref, content)
    
    return content, changes

def test_cdn_url(url: str) -> bool:
    """Test if a CDN URL is accessible."""
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except:
        return False

def main():
    products_readme = Path("/Users/uli/projects/apigeek.net/art/products/README.md")
    
    # Read the file
    with open(products_readme, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    print("🔍 PRODUCTS README.MD DRY RUN")
    print("=" * 50)
    
    # Show what changes would be made
    updated_content, changes = update_markdown_urls(original_content, CDN_BASE_URL, "products")
    
    print(f"📊 Would update {changes} URLs")
    print()
    
    # Show first few lines of transformation
    print("📝 SAMPLE TRANSFORMATION:")
    print("-" * 30)
    original_lines = original_content.split('\n')[:8]
    updated_lines = updated_content.split('\n')[:8]
    
    for i, (orig, updated) in enumerate(zip(original_lines, updated_lines), 1):
        if orig != updated:
            print(f"Line {i}:")
            print(f"  BEFORE: {orig}")
            print(f"  AFTER:  {updated}")
            print()
    
    # Test some CDN URLs
    print("🌐 TESTING CDN ACCESSIBILITY:")
    print("-" * 30)
    
    test_urls = [
        f"{CDN_BASE_URL}/products/albert-einstein-action-figure.jpg",
        f"{CDN_BASE_URL}/products/captions/albert-einstein-action-figure.jpg",
        f"{CDN_BASE_URL}/products/apple-vr-headset.jpg",
        f"{CDN_BASE_URL}/products/durian-couch.jpg"
    ]
    
    for url in test_urls:
        status = "✅ ACCESSIBLE" if test_cdn_url(url) else "❌ NOT FOUND"
        print(f"{status}: {url}")

if __name__ == "__main__":
    main()
