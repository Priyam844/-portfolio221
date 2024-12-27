from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)
os.makedirs('generated', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    about = request.form['about']
    skills = request.form.getlist('skills')

    # Render portfolio HTML
    html = render_template('portfolio.html', name=name, email=email, about=about, skills=skills)

    # Save as PDF (optional)
    pdf_path = os.path.join('generated', f'{name}_portfolio.pdf')
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, html)
    pdf.output(pdf_path)

    return render_template('portfolio.html', name=name, email=email, about=about, skills=skills)

@app.route('/download/<name>')
def download(name):
    pdf_path = os.path.join('generated', f'{name}_portfolio.pdf')
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
