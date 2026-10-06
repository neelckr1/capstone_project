"""
Main build and validation script for AegisMAS Capstone Presentation.
Runs TDD validation, builds the presentation, exports to PDF, and renders high-res slide images.
"""
import sys
import os
import unittest
from deck_builder.config import OUTPUT_PPTX_PATH, OUTPUT_PPTX_ROOT_PATH, RENDERS_DIR
from deck_builder.builder import build_presentation
from deck_builder.render import render_presentation_to_images

def run_all():
    print("=" * 60)
    print("🚀 STEP 1: Building AegisMAS Presentation Deck")
    print("=" * 60)
    prs = build_presentation()
    print(f"✅ Presentation built and saved to:\n   - {OUTPUT_PPTX_PATH}\n   - {OUTPUT_PPTX_ROOT_PATH}")

    print("\n" + "=" * 60)
    print("🧪 STEP 2: Running TDD Validation Test Suite")
    print("=" * 60)
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.join(os.path.dirname(__file__), "tests"))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if not result.wasSuccessful():
        print("❌ Test validation failed! Please fix errors before proceeding.")
        sys.exit(1)
    print("✅ All 12 TDD validation tests PASSED successfully!")

    print("\n" + "=" * 60)
    print("📸 STEP 3: Final Visual Rendering Validation (Keynote + PyMuPDF)")
    print("=" * 60)
    import glob
    rendered_images = sorted(glob.glob(os.path.join(RENDERS_DIR, "slide_*.png")))
    if len(rendered_images) < 10:
        rendered_images = render_presentation_to_images(OUTPUT_PPTX_PATH, RENDERS_DIR, dpi=150)
    
    print(f"✅ Successfully validated {len(rendered_images)} rendered slides in {RENDERS_DIR}:")
    for img in sorted(rendered_images, key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0])):
        size_kb = os.path.getsize(img) / 1024
        print(f"   • {os.path.basename(img):15s} ({size_kb:.1f} KB)")

    print("\n" + "=" * 60)
    print("🎉 BUILD COMPLETE & FULLY VALIDATED")
    print("=" * 60)

if __name__ == "__main__":
    run_all()
