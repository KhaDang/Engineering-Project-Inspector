import os
from collections import defaultdict
from pathlib import Path

#Import model drawing_record
from models.drawing_record import DrawingRecord

class FolderScanner:

    def __init__(self):
        self.folder_path: str
    def scan_folder(
            self,
            folder_path,
            ) -> dict[str, DrawingRecord]:
        search_folder = Path(fr"{folder_path}")

        # -----------------------------
        # Build file index
        # (Much faster than searching repeatedly)
        # -----------------------------

        file_index = defaultdict(lambda: defaultdict(list))

        for root, dirs, files in os.walk(search_folder):
            for file in files:
                name, ext = os.path.splitext(file)
                ext = ext.lower()
                if ext in [".sldprt", ".slddrw", ".sldasm", ".pdf"]:
                    file_index[name][ext].append(
                        os.path.join(root, file)
                    )

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
            if ".pdf" in extensions:
                paths = extensions[".pdf"]
                record.pdf_path = paths[0]
                if len(paths) > 1:
                    record.pdf_duplicates.extend(paths[1:])

            records[drawing_number] = record
        return records


from dataclasses import dataclass

@dataclass
class FolderStatistics:

    part_count: int = 0
    drawing_count: int = 0
    assembly_count: int = 0
    duplicate_count: int = 0
    drawing_records: int = 0

def count_file_types(self, records) -> FolderStatistics:

    stats = FolderStatistics()
    stats.drawing_records = len(records)

    for record in records.values():

        if record.part_path:
            stats.part_count += 1

        if record.drawing_path:
            stats.drawing_count += 1

        if record.assembly_path:
            stats.assembly_count += 1

        stats.duplicate_count += len(record.part_duplicates)
        stats.duplicate_count += len(record.drawing_duplicates)
        stats.duplicate_count += len(record.assembly_duplicates)

    return stats