from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph
from math import ceil
import re

def create_cards(input_file, output_file):
    # Read sentences from file
    with open(input_file, 'r', encoding='utf-8') as f:
        sentences = [line.strip() for line in f if line.strip()]

    # Calculate number of pages needed
    cards_per_page = 12
    num_pages = ceil(len(sentences) / cards_per_page)

    # Set up the document
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # Card dimensions
    card_width = width / 2
    card_height = height / 6

    # Margins
    margin = 15 * mm

    styles = getSampleStyleSheet()
    style = ParagraphStyle('Custom', 
                           parent=styles['Normal'],
                           alignment=TA_CENTER,
                           fontSize=12,
                           leading=14)

    def draw_wrapped_text(c, text, x, y, width, height):
        # Convert BBCode to HTML
        text = re.sub(r'\[b\](.*?)\[/b\]', r'<b>\1</b>', text)
        text = re.sub(r'\[i\](.*?)\[/i\]', r'<i>\1</i>', text)

        p = Paragraph(text, style)
        w, h = p.wrap(width - 2*margin, height - 2*margin)

        # Calculate vertical centering
        y_centered = y + (height - h) / 2

        # Draw the paragraph
        p.drawOn(c, x + margin, y_centered)

    for page in range(num_pages):
        for i in range(cards_per_page):
            if page * cards_per_page + i >= len(sentences):
                break

            # Calculate card position
            row = i // 2
            col = i % 2
            x = col * card_width
            y = height - (row + 1) * card_height

            # Draw card outline
            c.rect(x, y, card_width, card_height)

            # Add sentence
            sentence = sentences[page * cards_per_page + i]
            draw_wrapped_text(c, sentence, x, y, card_width, card_height)

        c.showPage()

    c.save()

# Usage
create_cards('sentence_list.txt', 'output_cards.pdf')