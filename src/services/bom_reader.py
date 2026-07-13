import pandas as pd
from pathlib import Path
import openpyxl

#Import model drawing_record
from models.drawing_record import DrawingRecord

class BomReader:

    def __init__(self):
        file_path: str
    #
    def read_bom_df(self, file_path):
        search_file = Path(fr"{file_path}")
        df = pd.read_excel(search_file, header=1)
        return df

    def read_header(self, file_path):
        df = self.read_bom_df(file_path)
        headers = [
            str(col).strip()
            for col in df.columns
            if not str(col).startswith("Unnamed")
        ]
        return headers
    def read_bom(
            self,
             file_path: str,
             col_values: {},
         ) -> dict[str,DrawingRecord]:

        # Read the excel file and store it into data frame
        bom_file = Path(fr"{file_path}")
        df = pd.read_excel(bom_file, header=1)

        # Create empty dict to store result
        records: dict[str, DrawingRecord] = {}

        # loop through the data frame to store data into dict: records
        for _, row in df.iterrows():
            # Check for missing values of drawing col
            drawing_number = row[col_values['bom_key']]
            if pd.isna(drawing_number):
                continue
            drawing_number = str(row[col_values['bom_key']]).strip()
            revision = row[col_values['secondary_key']] ## Should be optional

            record = DrawingRecord(
                drawing_number = drawing_number,
                revision= revision
            )
            records[drawing_number] = record
        return records


