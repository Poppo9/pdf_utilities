import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
from tqdm import tqdm

def get_total_pages(pdf_path):
    with open(pdf_path, 'rb') as file:
        return len(list(PDFPage.get_pages(file)))

def pdf_to_txt(pdf_path, txt_path):
    total_pages = get_total_pages(pdf_path)
    resource_manager = PDFResourceManager()
    output_string = BytesIO()
    codec = 'utf-8'
    laparams = LAParams()
    
    with TextConverter(resource_manager, output_string, codec=codec, laparams=laparams) as converter:
        with open(pdf_path, 'rb') as fin:
            interpreter = PDFPageInterpreter(resource_manager, converter)
            for page in tqdm(PDFPage.get_pages(fin), total=total_pages, desc="Converting pages", unit="page"):
                interpreter.process_page(page)
    
    with open(txt_path, 'w', encoding='utf-8') as fout:
        fout.write(output_string.getvalue().decode('utf-8'))

def main():
    print("Welcome to the PDF to TXT converter!")
    
    # List all PDF files in the current directory
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    print("Available PDF files:")
    for i, file in enumerate(pdf_files, 1):
        print(f"{i}. {file}")
    
    while True:
        choice = input("Enter the number of the PDF file you want to convert: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(pdf_files):
                pdf_file = pdf_files[index]
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    txt_file = input("Enter the name of the output TXT file (without extension, leave blank to use PDF name): ").strip()
    if not txt_file:
        txt_file = os.path.splitext(pdf_file)[0]
    txt_file += ".txt"
    
    print(f"Converting '{pdf_file}' to '{txt_file}'...")
    print("This process might take some time for large PDF files.")
    pdf_to_txt(pdf_file, txt_file)
    print(f"Conversion completed. The TXT file has been saved as '{txt_file}'.")

if __name__ == "__main__":
    main()
