from rules.missing_record_rule import MissingRecordRule, MissingInLeft, MissingInRight, FileMatching

class FolderInspectorConfig:
    # Configuration for radio buttons
    TYPE_OPTIONS = {
        "dir1": "Missing in Dir 1",
        "dir2": "Missing in Dir 2",
        "match": "Matching",
        "default": "None",

    }

    FILTERS = {
        "dir1": lambda r:
        r.has_issue(MissingInLeft),

        "dir2": lambda r:
        r.has_issue(MissingInRight),

        "match": lambda r:
        r.has_issue(FileMatching),

        "default": lambda r:
        True,
    }

    RULES = [
        MissingRecordRule(),
        # RevisionRule,
        # DuplicateRule,
    ]
    # column to read BOM
    # KEY_COLUMNS = [
    #     "BOM Key",
    # #     "Revision",
    # #     "Some key",
    # #     "Another key"
    # ]

    REPORT_TABLE_COLUMNS = [
        "Drawing Number",
        "Directory 1",
        "Directory 2",
        "Status"
    ]

    REPORT_STATUS_MESSAGES = [

        ("info", "      Indexed files ", "drawing_records"),

        ("info", "      SLDPRT", "part_count"),

        ("info", "      SLDDRW", "drawing_count"),

        ("info", "      SLDASM", "assembly_count"),

        ("info", "      PDF", "pdf_count"),

        ("info", "      Duplication", "duplicate_count")

    ]