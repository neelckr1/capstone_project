"""
Helper functions for formatting text frames, paragraphs, runs, and geometric shapes.
"""
from pptx.util import Pt, Emu
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from deck_builder.config import (
    FONT_FAMILY, C_DARK, C_INDIGO, C_RED, C_WHITE
)

def clear_tf(shape):
    """Clear all paragraphs and runs from a text frame and enable word wrap."""
    tf = shape.text_frame
    tf.word_wrap = True
    for p in list(tf.paragraphs)[1:]:
        p._p.getparent().remove(p._p)
    for r in list(tf.paragraphs[0].runs):
        r._r.getparent().remove(r._r)
    tf.paragraphs[0].text = ""
    return tf

def add_para(tf, level=0, space_after=5):
    """Add a new paragraph to a text frame at the given level."""
    p = tf.add_paragraph()
    p.level = level
    p.space_after = Pt(space_after)
    return p

def add_run(para, text, bold=False, italic=False, size=14, color=None):
    """Add a formatted run to a paragraph."""
    run = para.add_run()
    run.text = text
    run.font.name = FONT_FAMILY
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color
    return run

def write_header_bullet(tf, label, body="", label_color=C_INDIGO, body_color=C_DARK,
                         level=0, size=14, first=False, space_after=5):
    """Write a labeled bullet: bold colored label + regular body text."""
    if first:
        p = tf.paragraphs[0]
        p.level = level
        p.space_after = Pt(space_after)
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
    else:
        p = add_para(tf, level=level, space_after=space_after)
    if label:
        add_run(p, label + (" " if body else ""), bold=True, size=size, color=label_color)
    if body:
        add_run(p, body, bold=False, size=size, color=body_color)
    return p

def write_bullet(tf, text, level=0, bold=False, color=C_DARK, size=13, first=False, space_after=5):
    """Write a plain bullet at the given indent level."""
    if first:
        p = tf.paragraphs[0]
        p.level = level
        p.space_after = Pt(space_after)
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
    else:
        p = add_para(tf, level=level, space_after=space_after)
    add_run(p, text, bold=bold, size=size, color=color)
    return p

def add_card(slide, left, top, width, height, fill_color, line_color=None):
    """Add a rounded rectangle card with optional fill and line color."""
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(1.5)
    else:
        shape.line.fill.background()
    return shape

def add_textbox(slide, left, top, width, height, text="", size=13, bold=False,
                color=C_DARK, bg_color=None, align=PP_ALIGN.LEFT):
    """Add a floating text box with optional background color."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    if bg_color:
        txBox.fill.solid()
        txBox.fill.fore_color.rgb = bg_color
    txBox.line.fill.background()
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    p.space_after = Pt(4)
    if text:
        run = p.add_run()
        run.text = text
        run.font.name = FONT_FAMILY
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    return txBox

def set_slide_title(slide, shape_name, title_text):
    """Find title shape by name and set its text to red 24pt bold Trebuchet MS."""
    for shape in slide.shapes:
        if shape.name == shape_name and shape.has_text_frame:
            tf = clear_tf(shape)
            p = tf.paragraphs[0]
            p.space_after = Pt(4)
            run = p.add_run()
            run.text = title_text
            run.font.name = FONT_FAMILY
            run.font.size = Pt(24)
            run.font.bold = True
            run.font.color.rgb = C_RED
            return tf
    raise ValueError(f"Shape with name '{shape_name}' not found on slide.")
