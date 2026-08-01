from tkinter import messagebox

from exceptions.base_exception import MissingBomFileError, EmptyFolderError, InvalidColumnMappingError

ERROR_MESSAGES = {

    MissingBomFileError:
        "BOM selection is invalid, click Browse button to select BOM file!",

    EmptyFolderError:
        "Project folder selection is invalid, click Browse button to select path!",

    InvalidColumnMappingError:
        "Column selection is invalid."

}

class ErrorHandler:
    def handle(
        self,
        exception
    ):
        if isinstance(exception, MissingBomFileError):
            messagebox.showerror("Error - MissingBomFileError", ERROR_MESSAGES[MissingBomFileError] )

        if isinstance(exception, EmptyFolderError):
            messagebox.showerror("Error - EmptyFolderError", ERROR_MESSAGES[EmptyFolderError] )

        if isinstance(exception, InvalidColumnMappingError):
            messagebox.showerror("Error - InvalidColumnMappingError", ERROR_MESSAGES[InvalidColumnMappingError] )

