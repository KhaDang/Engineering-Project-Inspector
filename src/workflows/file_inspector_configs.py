from rules.missing_record_rule import MissingRecordRule, MissingInLeft, MissingInRight, FileMatching
from exceptions.base_exception import MissingBomFileError, EmptyFolderError

class FileInspectorConfig:
    # For type selector radio buttons configuration
    TYPE_OPTIONS = {
        "bom": "Missing in bom",
        "folder": "Missing in folder",
        "match": "Matching",
        "default": "None",

    }
    # For report table filter configuration
    FILTERS = {
        "bom": lambda r:
        r.has_issue(MissingInLeft),

        "folder": lambda r:
        r.has_issue(MissingInRight),

        "match": lambda r:
        r.has_issue(FileMatching),

        "default": lambda r:
        True,
    }

    # Which rule to run compare
    RULES = [
        MissingRecordRule(),
        # RevisionRule,
        # DuplicateRule,
    ]

    # For combo boxes configuration
    KEY_COLUMNS = [
        "BOM Key",
    #     "Revision",
    #     "Some key",
    #     "Another key"
    ]
    # For columns of report table configuration
    REPORT_TABLE_COLUMNS = [
        "Drawing Number",
        ".sldprt",
        ".slddrw",
        ".sldasm",
        "Status"
    ]
    # For Report Formater
    REPORT_STATUS_MESSAGES = [

        ("info", "      Indexed files ", "drawing_records"),

        ("info", "      SLDPRT", "part_count"),

        ("info", "      SLDDRW", "drawing_count"),

        ("info", "      SLDASM", "assembly_count"),

        ("info", "      Duplication", "duplicate_count")

    ]
    REPORT_RESULT_MESSAGES = [

        ("info", "      Matching file", ""),

        ("info", "      Missing in Folder", ""),

        ("info", "      Missing in BOM", ""),


    ]
