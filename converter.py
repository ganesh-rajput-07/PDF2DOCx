## if you dont have pdf2docx module installed then run the following command or skip this step
pip install pdf2docx

#after Ensuring that we have the pdf2docx module installed we can convert the pdf to docx
#importing the Converter class from pdf2docx

from pdf2docx import Converter

#selection of pdf
pdf_file= "2024S.pdf"

#selection of docx name that we wanted get
docx_file="2024S.docx"

# creating instance of the Converter class
cv=Converter(pdf_file)

# calling the convert method
cv.convert(docx_file)

# calling the close method after conversion
cv.close()

## run on Jupyter Notebook for efficient working of code 
## pdf file should be in same directory where notebook is saved