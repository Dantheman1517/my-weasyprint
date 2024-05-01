import os
import weasyprint
from jinja2 import Environment, FileSystemLoader

ROOT = '.'
ASSETS_DIR = os.path.join(ROOT, 'assets')

TEMPLAT_SRC = os.path.join(ROOT, 'templates')
CSS_SRC = os.path.join(ROOT, 'static/css')
DEST_DIR = os.path.join(ROOT, 'output')

# TEMPLATE = 'template.html'
TEMPLATE = 'subheadings.html'
CSS = 'style.css'
OUTPUT_FILENAME = 'my-report.pdf'

def start():
    print('start generate report...')
    env = Environment(loader=FileSystemLoader(TEMPLAT_SRC))
    template = env.get_template(TEMPLATE)
    css = os.path.join(CSS_SRC, CSS)

    # variables
    # template_vars = { 'assets_dir': 'file://' + ASSETS_DIR }
    template_vars = [
    {'title': 'Subheading 1', 'description': 'Description for Subheading 1'},
    {'title': 'Subheading 2', 'description': 'Description for Subheading 2'},
    {'title': 'Subheading 3', 'description': 'Description for Subheading 3'}
    # Add more items as needed
    ]
    # template_vars = {
    #     'title': 'Jinja2 Example',
    #     'heading': 'Hello, Jinja2!',
    #     'content': 'This is a simple example of using Jinja2 to render HTML.'
    # }

    # rendering to html string
    rendered_string = template.render(template_vars=template_vars)
    html = weasyprint.HTML(string=rendered_string)
    report = os.path.join(DEST_DIR, OUTPUT_FILENAME)
    # html.write_pdf(report, stylesheets=[css])
    html.write_pdf(report)
    print('file is generated successfully and under {}', DEST_DIR)


if __name__ == '__main__':
    start()