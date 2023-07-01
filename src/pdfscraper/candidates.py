from .scraper import extract_rawdata


def extract_candidates(file: str):
    rawdata = extract_rawdata(file)
    print(rawdata)