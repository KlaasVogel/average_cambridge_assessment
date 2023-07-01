# from calculator import avg_score_calculator
from pdfscraper import extract_cefr_scores
import os

file = os.path.join( "testfiles", "B2 2020.pdf")
scores = extract_cefr_scores(file)
print(scores)



