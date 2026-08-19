from views.copy_missing_dialog import CopyMissingDialog


from services.folder_scanner import FolderScanner
from services.copy_service import CopyService
from services.error_handler import ErrorHandler


# import Exceptions - Error Handler

from exceptions.base_exception import EngineeringFileManagerError

class CopyMissingController:


    def __init__(self,
                parent,
                comparison_result,
                    ):
        self.master = parent,

        self.folder_scanner = FolderScanner()

        self.comparison_result = comparison_result

        self.copy_service = CopyService()

        self.error_handler = ErrorHandler()


    def show(self):
        dialog = CopyMissingDialog(self.master, self.on_copy_missing_files)

    def on_copy_missing_files(self, request, progress_message):
        lookup_list = [
            result.drawing_number
            for result in self.comparison_result
            if result.has_issue(request.copy_mode)
        ]
        request.lookup_list = lookup_list
        try:
            indexed_files = self.folder_scanner.scan_folder(
                                                            request.source,
                                                            # progress_message.start_progress,
                                                            # progress_message.update_progress,

                                                            )
        except EngineeringFileManagerError as e:
            self.error_handler.handle(e)
            return

        try:
            results = self.copy_service.copy(
                indexed_files,
                request,
                progress_message
            )
        except EngineeringFileManagerError as e:
            self.error_handler.handle(e)
            return

        progress_message.confirmed_message(f'Found and copied {len(results.copied)}/{len(request.lookup_list)} files. Process Done!')



        # find_folder = self.folder_scanner.scan_folder(request.search_folder, None, None)


