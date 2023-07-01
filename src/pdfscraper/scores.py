from .scraper import extract_rawdata, RawPageText
from dataclasses import dataclass, InitVar

NotValidAttributeError  = Exception("not a valid attribute")

@dataclass
class CEFR_Scores:
    data: InitVar
    reference: str = ""
    session: str = ""
    name: str = ""
    session: str = ""
    result: str = ""
    overall: int = 0
    level: str = ""
    reading: int = 0
    use_of_english: int = 0
    writing: int = 0
    listening: int = 0
    speaking: int = 0

    def __post_init__(self, data: RawPageText):
        self.add_data(data)
        
    def add_data(self, data: RawPageText):
        """for each text in list of text check if text in reference table. get attribute from ref. tabl and update attribute"""
        referencetable = {
           "Reference No.": "reference",
           "Candidate name": "name",
           "Session": "session",
           "Result": "result",
           "Overall Score": "overall",
           "CEFR Level": "level",
           "Reading": "reading",
           "Use of English": "use_of_english",
           "Writing": "writing",
           "Listening": "listening",
           "Speaking": "speaking"
        }
        for idx, text in enumerate(data):
            if text in referencetable:
                if not len(data)>idx+1:
                    #reached end of texts"
                    continue
                value = data[idx+1]
                if getattr(self, referencetable[text]):
                    #attribute has already been set. (level?) -> skip
                    continue
                self.add_value(key = referencetable[text], value = value)
            

    def check_int(self, attribute: str) -> bool:
        """check if attribute is of instance int """  
        return isinstance(getattr(self, attribute), int)

    def add_value(self, key: str, value: str):
        if not hasattr(self, key):
            raise NotValidAttributeError
        if self.check_int(key):
            value = int(value)
        setattr(self, key, value)        


def extract_cefr_scores(file: str) -> list[CEFR_Scores]:
    rawdata = extract_rawdata(file)
    return [CEFR_Scores(rawpage) for rawpage in rawdata]