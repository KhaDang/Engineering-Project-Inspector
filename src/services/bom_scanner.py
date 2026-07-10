import os
import shutil
import pandas as pd
from collections import defaultdict
from pathlib import Path
import openpyxl

#Import model drawing_record
from models.bom_record import BOMRecord

class BomReader:

    def __init__(self):
        file_path: str

    def read_bom(self, file_path):
        search_file = Path(fr"{file_path}")
        df = pd.read_excel(search_file, header=1)
        print(df)


