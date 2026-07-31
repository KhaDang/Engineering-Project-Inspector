class EngineeringFileManagerError(Exception):
    pass

class MissingBomFileError(
    EngineeringFileManagerError
):
    pass

class EmptyFolderError(
    EngineeringFileManagerError
):
    pass
