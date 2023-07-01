# from calculator import avg_score_calculator
from pdfscraper import extract_data_to_pages
import os

file = os.path.join( "testfiles", "B2 2020.pdf")
text = extract_data_to_pages(file)



