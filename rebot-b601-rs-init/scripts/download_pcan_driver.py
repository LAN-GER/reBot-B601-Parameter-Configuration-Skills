#!/usr/bin/env python3
"""
Download PCAN-USB Windows driver from PEAK-System.

If automatic download fails, opens the browser to the manual download page.
"""

import os
import sys
import urllib.request
import urllib.error
import webbrowser

# PEAK-System driver download URLs (attempted in order)
DRIVER_URLS = [
    "https://www.peak-system.com/fileadmin/media/files/PeakOemDrv.exe",
    "https://www.peak-system.com/fileadmin/media/files/DrvSetup5.exe",
    "https://www.peak-system.com/quick/DrvSetup5",
]

# Product page for manual download
PRODUCT_PAGE = "https://www.peak-system.com/products/hardware/external-pc-interfaces/pcan-usb/"

# Default save directory
SAVE_DIR = os.path.join(os.path.expanduser("~"), "Downloads")


def download_file(url: str, save_path: str, timeout: int = 60) -> bool:
    """Download a file from URL to save_path."""
    try:
        print(f"[INFO] Downloading from: {url}")
        print(f"[INFO] Saving to: {save_path}")
        urllib.request.urlretrieve(url, save_path)
        file_size = os.path.getsize(save_path)
        print(f"[SUCCESS] Downloaded {file_size} bytes")
        return True
    except Exception as e:
        print(f"[ERROR] Download failed: {e}")
        return False


def open_browser(url: str) -> None:
    """Open the default web browser to the given URL."""
    print(f"[INFO] Opening browser: {url}")
    webbrowser.open(url)


def main() -> int:
    print("=" * 60)
    print("PCAN-USB Windows Driver Downloader")
    print("=" * 60)
    print()
    print("This script will attempt to download the PEAK-System")
    print("PCAN-USB device driver for Windows.")
    print()

    # Ensure save directory exists
    os.makedirs(SAVE_DIR, exist_ok=True)

    # Try each download URL
    downloaded = False
    for url in DRIVER_URLS:
        filename = os.path.basename(url.split("?")[0].split("#")[0])
        if not filename or "." not in filename:
            filename = "PeakOemDrv.exe"
        save_path = os.path.join(SAVE_DIR, filename)

        if download_file(url, save_path):
            downloaded = True
            print()
            print("=" * 60)
            print("[SUCCESS] Driver downloaded successfully!")
            print(f"[INFO] Location: {save_path}")
            print("=" * 60)
            print()
            print("Next steps:")
            print("1. Run the downloaded installer")
            print("2. Follow the PEAK-System installation wizard")
            print("3. After installation, connect your PCAN-USB adapter")
            print("4. Verify in Device Manager that 'PCAN-USB' appears")
            break

    if not downloaded:
        print()
        print("=" * 60)
        print("[WARNING] Automatic download failed.")
        print("=" * 60)
        print()
        print("Opening the PEAK-System download page in your browser...")
        print(f"URL: {PRODUCT_PAGE}")
        print()
        print("Please download the driver manually:")
        print("1. Click 'Device driver setup 5.x for Windows'")
        print("2. Click the 'Download' button")
        print("3. Run the downloaded installer")
        print()
        open_browser(PRODUCT_PAGE)

    return 0 if downloaded else 1


if __name__ == "__main__":
    sys.exit(main())
