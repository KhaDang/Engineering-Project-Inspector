from views.copy_missing_dialog import CopyMissingDialog


from services.folder_scanner import FolderScanner
from services.copy_service import CopyService

class CopyMissingController:


    def __init__(self,
                parent,
                comparison_result,
                    ):
        self.master = parent,

        self.folder_scanner = FolderScanner()

        self.comparison_result = comparison_result

        self.copy_service = CopyService()


    def show(self):
        dialog = CopyMissingDialog(self.master, self.on_copy_missing_files)

    def on_copy_missing_files(self, request):
        lookup_list = [
            result.drawing_number
            for result in self.comparison_result
            if result.has_issue(request.copy_mode)
        ]
        request.lookup_list = lookup_list

        indexed_files = self.folder_scanner.scan_folder(request.source)
        results = self.copy_service.copy(indexed_files= indexed_files, request=request)


        # find_folder = self.folder_scanner.scan_folder(request.search_folder, None, None)


