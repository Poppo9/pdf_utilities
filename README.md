# PDF Utility Scripts

This project provides three utility scripts to work with PDF files:

1. `split-pdf.py`: A script to split a PDF file into smaller parts based on a specified maximum size.
2. `pdf-to-html.py`: A script to convert a PDF file to HTML format.
3. `pdf-to-txt.py`: A script to convert a PDF file to text format.

## Requirements

- Python 3.x
- `PyPDF2`
- `pdfminer.six`
- `tqdm`

You can install the required Python packages using pip:

```sh
pip install PyPDF2 pdfminer.six tqdm
```

## `split-pdf.py`

This script splits a PDF file into smaller parts based on a specified maximum size.

### Usage

1. Ensure your PDF file is in the same directory as `split-pdf.py`.
2. Run the script:

```sh
python split-pdf.py
```

### Script Description

- Lists all PDF files in the current directory.
- Prompts the user to select a PDF file to split.
- Prompts the user to specify the maximum size (in MB) for each split part.
- Prompts the user to enter the base name for the output files and the output folder name.
- Splits the PDF file and saves the parts in the specified output folder.

### Example

```sh
Welcome to the PDF splitter!
Available PDF files:
1. example.pdf
Enter the number of the PDF file you want to split: 1
Enter the maximum size for each part (in MB): 2
Enter the base name for the output files (without extension): part
Enter the name of the output folder (it will be created if it does not exist): output
Splitting 'example.pdf'...
This process might take some time for large PDF files.
Splitting completed. The split PDF files have been saved in the 'output' folder.
```

## `pdf-to-html.py`

This script converts a PDF file to HTML format.

### Usage

1. Ensure your PDF file is in the same directory as `pdf-to-html.py`.
2. Run the script:

```sh
python pdf-to-html.py
```

### Script Description

- Lists all PDF files in the current directory.
- Prompts the user to select a PDF file to convert.
- Prompts the user to enter the name for the output HTML file.
- Converts the PDF file to HTML and saves it with the specified name.

### Example

```sh
Welcome to the PDF to HTML converter!
Available PDF files:
1. example.pdf
Enter the number of the PDF file you want to convert: 1
Enter the name of the output HTML file (without extension): example_output
Converting 'example.pdf' to 'example_output.html'...
This process might take some time for large PDF files.
Conversion completed. The HTML file has been saved as 'example_output.html'.
```

## `pdf-to-txt.py`

This script converts a PDF file to text format.

### Usage

1. Ensure your PDF file is in the same directory as `pdf-to-txt.py`.
2. Run the script:

```sh
python pdf-to-txt.py
```

### Script Description

- Lists all PDF files in the current directory.
- Prompts the user to select a PDF file to convert.
- Prompts the user to enter the name for the output text file.
- Converts the PDF file to text and saves it with the specified name.

### Example

```sh
Welcome to the PDF to Text converter!
Available PDF files:
1. example.pdf
Enter the number of the PDF file you want to convert: 1
Enter the name of the output text file (without extension): example_output
Converting 'example.pdf' to 'example_output.txt'...
This process might take some time for large PDF files.
Conversion completed. The text file has been saved as 'example_output.txt'.
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.
