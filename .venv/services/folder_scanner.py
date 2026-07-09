import os
import shutil
import pandas as pd
from collections import defaultdict

class FolderScanner:

    def __init__(self, folder_path):
        self.folder_path = folder_path
    def scan_folder(self, folder_path):
        search_folder = r + folder_path

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