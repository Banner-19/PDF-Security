from PyPDF2 import PdfReader, PdfWriter

pdfWriter = PdfWriter()

# Read the pdf file which will be encrypted
with open("regression_analysis.pdf", "rb") as pdf_file:
    pdf = PdfReader(pdf_file)

    for page_num in range(len(pdf.pages)):
        pdfWriter.add_page(pdf.pages[page_num])

    # Encryption process goes here
    passw = input('Enter your password: ')
    pdfWriter.encrypt(passw)
    print('Password was set successfully!')

    setNewName = input('What will you name your encrypted pdf? (without ".pdf"): ')
    newPdfName = f"{setNewName}.pdf"

    # Create a new encrypted PDF
    with open(newPdfName, 'wb') as f:
        pdfWriter.write(f)

print('Excellent! You have secured your PDF file!')
