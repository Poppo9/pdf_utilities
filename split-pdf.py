import PyPDF2
import os
from tqdm import tqdm

def get_pdf_files():
    return [f for f in os.listdir('.') if f.endswith('.pdf')]

def split_pdf(input_pdf_path, output_folder, max_size_mb, output_base_name):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file)
        total_pages = len(reader.pages)
        
        part_number = 1
        start_page = 1
        writer = PyPDF2.PdfWriter()
        
        for page_num in tqdm(range(total_pages), desc="Splitting the PDF", unit="page"):
            writer.add_page(reader.pages[page_num])
            
            temp_output_path = f"{output_folder}/temp.pdf"
            with open(temp_output_path, 'wb') as temp_output_file:
                writer.write(temp_output_file)
            
            if os.path.getsize(temp_output_path) > max_size_mb * 1024 * 1024:
                end_page = page_num
                output_pdf_path = f"{output_folder}/{output_base_name}_part_{part_number:03d}_pages_{start_page}-{end_page}.pdf"
                with open(output_pdf_path, 'wb') as output_pdf_file:
                    writer.write(output_pdf_file)
                
                part_number += 1
                writer = PyPDF2.PdfWriter()
                start_page = page_num + 1
            
            os.remove(temp_output_path)
        
        if len(writer.pages) > 0:
            end_page = total_pages
            output_pdf_path = f"{output_folder}/{output_base_name}_part_{part_number:03d}_pages_{start_page}-{end_page}.pdf"
            with open(output_pdf_path, 'wb') as output_pdf_file:
                writer.write(output_pdf_file)

def main():
    print("Welcome to the PDF splitter!")
    
    pdf_files = get_pdf_files()
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    print("Available PDF files:")
    for i, file in enumerate(pdf_files, 1):
        print(f"{i}. {file}")
    
    while True:
        choice = input("Enter the number of the PDF file you want to split: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(pdf_files):
                input_pdf = pdf_files[index]
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            max_size_mb = float(input("Enter the maximum size for each part (in MB): "))
            if max_size_mb > 0:
                break
            else:
                print("Size must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    
    output_base_name = input("Enter the base name for the output files (without extension, leave blank to use PDF name): ").strip()
    if not output_base_name:
        output_base_name = os.path.splitext(input_pdf)[0]
    
    output_folder = input("Enter the name of the output folder (it will be created if it does not exist): ")
    
    print(f"Splitting '{input_pdf}'...")
    print("This process might take some time for large PDF files.")
    split_pdf(input_pdf, output_folder, max_size_mb, output_base_name)
    print(f"Splitting completed. The split PDF files have been saved in the '{output_folder}' folder.")

if __name__ == "__main__":
    main()
