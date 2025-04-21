def save_pdf(file_path, content):
    """Saves the content to a PDF file."""
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf.output(file_path)

def load_pdf(file_path):
    """Loads content from a PDF file."""
    from PyPDF2 import PdfReader

    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def delete_file(file_path):
    """Deletes a specified file."""
    import os

    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")