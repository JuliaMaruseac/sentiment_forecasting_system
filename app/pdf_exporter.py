from xhtml2pdf import pisa
from jinja2 import Environment, FileSystemLoader
import pandas as pd

def generate_pdf(data, file_path="report.pdf"):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")
    html = template.render(data=data)

    with open(file_path, "wb") as f:
        pisa.CreatePDF(html, dest=f)
