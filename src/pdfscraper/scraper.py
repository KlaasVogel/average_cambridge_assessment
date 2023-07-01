import os
import fitz

NoFileException= Exception("file not found")

def get_document(file: str) -> fitz.Document:
    try:
        if not os.path.isfile(file):
            raise NoFileException
        filepath = os.path.abspath(file)
        return fitz.open(filepath)
    except:
        return []        

class RawPageText(list[str]):
    """a list of all the raw text found in a pdf"""
    def load(self, text: str):
        words = text.split("\n")
        self.extend(words)

class RawPages(list[RawPageText]):
    """a list pages with raw text"""
    def add_page(self) -> RawPageText:
        newpage = RawPageText()
        self.append(newpage)
        return newpage

def extract_pdfdata_to_rawpages(document: fitz.Device) -> RawPages:
    """extract data from pdf, splaces xml in same directory with same name as pdf. returns (full) path of xml"""
    output = RawPages()
    for page in document:
        rawpage = output.add_page()
        text = page.get_text()
        rawpage.load(text)
    return output

def extract_rawdata(file: str) -> RawPages:
    document = get_document(file)
    rawdata = extract_pdfdata_to_rawpages(document)
    return rawdata



    


