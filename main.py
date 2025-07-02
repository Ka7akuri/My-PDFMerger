# Import the PdfWriter class from PyPDF2 to handle creating and merging PDF files
from PyPDF2 import PdfWriter

# Create an instance of PdfWriter, which will be used to merge the PDF files
merger = PdfWriter()

# Create an empty list to store the names of the PDF files to be merged
pdfs = []

# Ask the user how many PDF files they want to merge
n = int(input("How many pdfs do you want to merge?\n"))

# Loop through the range from 0 to n (number of PDFs)
for i in range(0, n):
    # Ask the user to input the name (filename) of each PDF
    name = input(f"Enter the name of the pdf {i + 1}: ")
    # Add the PDF name to the list
    pdfs.append(name)

# Loop through the list of PDF filenames
for pdf in pdfs:
    # Append each PDF to the merger object
    merger.append(pdf)

# Write (save) the merged PDF as a new file called "merged-pdf.pdf"
merger.write("merged-pdf.pdf")

# Close the merger to free up system resources
merger.close()