from rules.missing_record_rule import MissingRecordRule, MissingInLeft, MissingInRight, FileMatching
from rules.revision_rule import RevisionRule, RevisionMatching, RevisionMismatch

class RevInspectorConfig:

    TYPE_OPTIONS = {
        "bom": "Missing in BOM",

        "folder": "Missing in Folder",

        "rev_matching": "Rev Matching",

        "outdated": "Drw Outdated",

        "default": "None",

    }

    # For report table filter configuration
    FILTERS = {
        "bom": lambda r:
        r.has_issue(MissingInLeft),

        "folder": lambda r:
        r.has_issue(MissingInRight),

        "rev_matching": lambda r:
        r.has_issue(RevisionMatching),

        "outdated": lambda r:
        r.has_issue(RevisionMismatch),

        "default": lambda r:
        True,
    }

    ENABLE_REVISION = True

    RULES = [
        MissingRecordRule(),
        RevisionRule(),
        # DuplicateRule,
    ]

    KEY_COLUMNS = [
        "BOM Key",
        "Revision",
    #     "Some key",
    #     "Another key"
    ]
    REPORT_TABLE_COLUMNS = [
        "Drawing Number",
        "Bom_rev",
        "Folder_rev",
        "Status"
    ]

    REPORT_STATUS_MESSAGES = [

        ("info", "      Indexed files ", "drawing_records"),

    ]
    REPORT_RESULT_MESSAGES = [

        ("info", "      Matching file", ""),

        ("info", "      Missing in Folder", ""),

        ("info", "      Missing in BOM", ""),


    ]