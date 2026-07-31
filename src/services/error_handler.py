from tkinter import messagebox

from exceptions.base_exception import MissingBomFileError, EmptyFolderError

ERROR_MESSAGES = {

    MissingBomFileError:
        "Please select a BOM file.",

    EmptyFolderError:
        "Project folder contains no drawings.",

    # InvalidColumnMappingError:
    #     "Column selection is invalid."

}

class ErrorHandler:
    def handle(
        self,
        exception
    ):
        if isinstance(exception, MissingBomFileError):
            messagebox.showerror("Error - MissingBomFileError", ERROR_MESSAGES[MissingBomFileError] )
