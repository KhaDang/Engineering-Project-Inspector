import os
import shutil
import pandas as pd
from collections import defaultdict
from pathlib import Path

#Import model drawing_record
from models.drawing_record import DrawingRecord

class FolderScanner:

    def __init__(self):
        self.folder_path: str
    def scan_folder(self, folder_path) -> dict[str, DrawingRecord]:
        search_folder = Path(fr"{folder_path}")

        # -----------------------------
        # Build file index
        # (Much faster than searching repeatedly)
        # -----------------------------

        print("Indexing files...")
        file_index = defaultdict(lambda: defaultdict(list))
        for root, dirs, files in os.walk(search_folder):
            for file in files:
                name, ext = os.path.splitext(file)
                ext = ext.lower()
                if ext in [".sldprt", ".slddrw", ".sldasm"]:
                    file_index[name][ext].append(
                        os.path.join(root, file)
                    )
        print(f"{len(file_index)} unique drawing names.")

        records = {}
        for drawing_number, extensions in file_index.items():
            record = DrawingRecord (drawing_number = drawing_number)

            if ".sldprt" in extensions:
                paths = extensions[".sldprt"]
                record.part_path = paths[0]
                if len(paths) > 1:
                    record.part_duplicates.extend(paths[1:])

            if ".slddrw" in extensions:
                paths = extensions[".slddrw"]
                record.drawing_path = paths[0]
                if len(paths) > 1:
                    record.drawing_duplicates.extend(paths[1:])

            if ".sldasm" in extensions:
                paths = extensions[".sldasm"]
                record.assembly_path = paths[0]
                if len(paths) > 1:
                    record.assembly_duplicates.extend(paths[1:])

            records[drawing_number] = record
        return records
