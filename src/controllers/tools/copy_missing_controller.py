from views.copy_missing_dialog import CopyMissingDialog
from services.folder_scanner import FolderScanner

class CopyMissingController:


    def __init__(self,
                parent,
                comparison_result,
                    ):
        self.master = parent,

        self.folder_scanner = FolderScanner()

        self.comparison_result = comparison_result

    def show(self):
        dialog = CopyMissingDialog(self.master, self.on_copy_missing_files)

    def on_copy_missing_files(self, request):
        lookup_list = [
            result.drawing_number
            for result in self.comparison_result
            if result.has_issue(request.copy_mode)
        ]
        request.lookup_list = lookup_list

        print(request.lookup_list)
        # find_folder = self.folder_scanner.scan_folder(request.search_folder, None, None)


