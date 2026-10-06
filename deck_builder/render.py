"""
Render module: converts PPTX to PDF via Keynote AppleScript and renders high-res PNG slides via PyMuPDF.
"""
import subprocess
import os
import time
import pymupdf
from deck_builder.config import OUTPUT_PPTX_PATH, RENDERS_DIR

def render_presentation_to_images(pptx_path=OUTPUT_PPTX_PATH, output_dir=RENDERS_DIR, dpi=150):
    """
    Renders presentation slides to PNG images:
    1. Uses Keynote AppleScript to export PPTX to temporary PDF.
    2. Uses PyMuPDF to render each PDF page into a high-res PNG image.
    Returns list of generated image file paths.
    """
    os.makedirs(output_dir, exist_ok=True)
    temp_pdf = os.path.join(output_dir, "temp_export.pdf")
    
    abs_pptx = os.path.abspath(pptx_path)
    abs_pdf = os.path.abspath(temp_pdf)

    # AppleScript to launch Keynote, open PPTX, export PDF, and close
    applescript = f'''
    tell application "Keynote"
        activate
        close every document saving no
        delay 1
        with timeout of 60 seconds
            set theDoc to open POSIX file "{abs_pptx}"
            delay 2
            export theDoc to POSIX file "{abs_pdf}" as PDF
            close theDoc saving no
        end timeout
        quit
    end tell
    '''
    
    res = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)
    if res.returncode != 0 or not os.path.exists(abs_pdf):
        raise RuntimeError(f"Keynote export to PDF failed (RC={res.returncode}): {res.stderr}\n{res.stdout}")

    # Now render PDF pages to PNG using PyMuPDF
    doc = pymupdf.open(abs_pdf)
    image_paths = []
    
    for page_idx, page in enumerate(doc):
        pix = page.get_pixmap(dpi=dpi)
        img_path = os.path.join(output_dir, f"slide_{page_idx + 1}.png")
        pix.save(img_path)
        image_paths.append(img_path)

    # Clean up temporary PDF
    if os.path.exists(abs_pdf):
        os.remove(abs_pdf)

    # Allow Keynote to settle or quit cleanly
    time.sleep(1)
    subprocess.run(['osascript', '-e', 'tell application "Keynote" to quit'], capture_output=True)

    return image_paths
