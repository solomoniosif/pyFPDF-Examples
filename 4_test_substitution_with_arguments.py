# 4_test_substitution_with_arguments.py
# python3 4_test_substitution_with_arguments.py --title "Title From Arguments"

import os
from fpdf import FPDF, HTMLMixin
import argparse

parser = argparse.ArgumentParser(description='PDF maker with custom arguments')
parser.add_argument("--title", default="", help="This is the title of the PDF")
args = parser.parse_args()
title = args.title

class HTML2PDF(FPDF, HTMLMixin):
    pass


#title = "test title from program"
subtitle = "test title from program"
text = "Nunc consequat nisi ut tempus porta. Mauris dictum neque nibh, eget volutpat turpis pellentesque a. Pellentesque tempor magna vitae risus bibendum maximus. In ultricies posuere ex, a cursus quam imperdiet ac. Nulla id dui a mauris volutpat varius dictum non ligula. In hac habitasse platea dictumst. Nulla nibh odio, rhoncus eget feugiat at, eleifend sed orci. Aenean vitae diam tellus. Pellentesque eget fermentum libero. Sed orci erat, porttitor a elit at, euismod egestas odio."
src = "templates/assets/img/banff_3.jpg"
width = "500"
height = "200"

root = os.path.dirname(os.path.abspath(__file__))
htmlpath = os.path.join(root, 'templates', '3_test_substitution_with_image.html')
with open(htmlpath, 'r') as file:
    html = file.read()

    # replace spots in text with pre-defined values
    html = html.replace("{% title %}", title)
    html = html.replace("{% subtitle %}", subtitle)
    html = html.replace("{% text %}", text)
    html = html.replace("{% src %}", src)
    html = html.replace("{% width %}", width)
    html = html.replace("{% height %}", height)

    pdf = HTML2PDF()
    pdf.add_page()
    pdf.write_html(html)
    pdf.output('pdfs/4_test_substitution_with_arguments.pdf')
