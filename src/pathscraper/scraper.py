import os
from glob import glob
from pdfscraper import extract_cefr_scores, CEFR_Scores

InvalidPathError = Exception("path is not a valid path")

def load_dir(source: str) -> list[CEFR_Scores]:
    if not os.path.isdir(source):
        raise InvalidPathError
    query = os.path.join(source, "*.pdf")
    filelist = glob(query)
    return [scores for file in filelist for scores in extract_cefr_scores(file)]