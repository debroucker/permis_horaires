import PyPDF2

def read_pdf(pdf_path) :
    fhandle = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(fhandle)
    pagehandle = pdfReader.getPage(0)
    return pagehandle.extractText()

def extract_good_text(pdf_text):
    pdf_text_split = pdf_text.split('\n')
    pdf_text_split = pdf_text_split[12:]
    pdf_text_split = pdf_text_split[:-4]
    good_text_split = []
    for e in pdf_text_split :
        try :
            int(e.strip())
        except :
            good_text_split.append(e)
    res = []
    for i in range(0, len(good_text_split)-1, 5):
        res.append([good_text_split[i].split('.')[1], int(good_text_split[i+1].split('H')[0]), good_text_split[i+2]])
    return res
