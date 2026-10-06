"""
Configuration constants and styling definitions for the AegisMAS presentation deck.
"""
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, "ppt", "sample.pptx")
OUTPUT_PPTX_PATH = os.path.join(BASE_DIR, "ppt", "AegisMAS_Capstone_Proposal.pptx")
OUTPUT_PPTX_ROOT_PATH = os.path.join(BASE_DIR, "AegisMAS_Capstone_Proposal.pptx")
RENDERS_DIR = os.path.join(BASE_DIR, "ppt", "renders")

# ── Slide Dimensions ─────────────────────────────────────────────────────────
SLIDE_WIDTH_EMU = 12192000   # 13.33 inches (16:9 widescreen)
SLIDE_HEIGHT_EMU = 6858000   # 7.50 inches

# ── Typography ───────────────────────────────────────────────────────────────
FONT_FAMILY = "Trebuchet MS"

# ── Design System Color Palette ──────────────────────────────────────────────
# Template Preserved Colors
C_TEAL       = RGBColor(0x33, 0xCC, 0xCC)   # #33CCCC (Template horizontal bar)
C_RED        = RGBColor(0xFF, 0x00, 0x00)   # #FF0000 (Template slide title label)
C_NAVY       = RGBColor(0x00, 0x33, 0xCC)   # #0033CC (Template body text)

# AegisMAS Technical Theme Colors
C_INDIGO     = RGBColor(0x37, 0x30, 0xA3)   # #3730A3 (Primary accent & headers)
C_CYAN       = RGBColor(0x08, 0x91, 0xB2)   # #0891B2 (Highlight & emphasis)
C_DARK       = RGBColor(0x1E, 0x29, 0x3B)   # #1E293B (Body / paragraph text)
C_MUTED      = RGBColor(0x47, 0x55, 0x69)   # #475569 (Secondary / muted text)
C_GREEN      = RGBColor(0x05, 0x96, 0x69)   # #059669 (Green path / Target success)
C_AMBER      = RGBColor(0xD9, 0x77, 0x06)   # #D97706 (Amber path / Warning)
C_CRIMSON    = RGBColor(0xDC, 0x26, 0x26)   # #DC2626 (Red path / Threat)
C_CALLOUT_BG = RGBColor(0xEE, 0xF2, 0xFF)   # #EEF2FF (Callout card background)
C_WHITE      = RGBColor(0xFF, 0xFF, 0xFF)   # #FFFFFF (White)
C_LIGHT_INDIGO = RGBColor(0xA5, 0xB4, 0xFC) # #A5B4FC (Subtitle tint)
