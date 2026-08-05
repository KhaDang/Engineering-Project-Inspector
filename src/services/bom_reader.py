from plistlib import InvalidFileException

import pandas as pd
from pathlib import Path
import openpyxl

#Import model drawing_record
from models.drawing_record import DrawingRecord

# Import Exception
from exceptions.base_exception import MissingBomFileError, InvalidColumnMappingError


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
             selected_columns: {},
         ) -> dict[str,DrawingRecord]:

        # Manage the error
        if not Path(file_path).is_file():
            raise MissingBomFileError(file_path)

        for col, value in selected_columns.items():
            if not value:
                print(f"debug invalid columns")
                raise InvalidColumnMappingError(file_path)

        # Read the excel file and store it into data frame
        bom_file = Path(fr"{file_path}")
        df = pd.read_excel(bom_file, header=1)



        # Create empty dict to store result
        records: dict[str, DrawingRecord] = {}

        # loop through the data frame to store data into dict: records
        for _, row in df.iterrows():

            record = self.create_record(
                row,
                selected_columns
            )
            if pd.isna(record.drawing_number):
                continue

            records[record.drawing_number] = record
        return records


    def create_record(self,
                      row,
                      selected_colums):
        drawing = self.normalize(row[selected_colums['BOM Key']])

        revision = None
        if "Revision" in selected_colums:
            revision = self.normalize(row[selected_colums['Revision']])

        return DrawingRecord(
            drawing_number=drawing,
            bom_revision=revision
        )


    @staticmethod
    def normalize(value):
        if pd.isna(value):
            return None

        return str(value).strip()