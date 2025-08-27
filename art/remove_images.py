#!/usr/bin/env python3
"""
Script to safely remove all image files from the art project tree
since they are now served from CDN.
"""

import os
from pathlib import Path

def remove_image_files(root_dir: str) -> tuple[int, int]:
    """
    Remove all image files from the directory tree.
    
    Returns: (files_removed, total_size_mb)
    """
    root_path = Path(root_dir)
    
    # Image file extensions to remove
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}
    
    files_removed = 0
    total_size = 0
    
    # Find and remove all image files
    for file_path in root_path.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            try:
                # Get file size before removal
                file_size = file_path.stat().st_size
                total_size += file_size
                
                # Remove the file
                file_path.unlink()
                files_removed += 1
                
                print(f"Removed: {file_path.relative_to(root_path)}")
                
            except Exception as e:
                print(f"Error removing {file_path}: {e}")
    
    total_size_mb = total_size / (1024 * 1024)
    return files_removed, total_size_mb

def main():
    """Main function to remove image files."""
    root_directory = "/Users/uli/projects/apigeek.net/art"
    
    print("🗑️  REMOVING IMAGE FILES FROM ART PROJECT")
    print("=" * 50)
    print("Images are now served from CDN, removing local copies...")
    print()
    
    # Remove image files
    files_removed, size_mb = remove_image_files(root_directory)
    
    print()
    print("=" * 50)
    print(f"✅ Removed {files_removed} image files")
    print(f"💾 Freed up {size_mb:.1f} MB of disk space")
    print()
    print("📁 Preserved files:")
    print("   - All README.md files (now with CDN URLs)")
    print("   - All .backup files")
    print("   - All scripts (.py, .sh)")
    print("   - All templates and text files")

if __name__ == "__main__":
    main()
