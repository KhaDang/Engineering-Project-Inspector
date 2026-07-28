from rules.missing_record_rule import MissingRecordRule
from rules.revision_rule import RevisionRule

class RevInspectorConfig:

    TYPE_OPTIONS = {
         "match": "Matching",
        "mismatch": "Revision mismatch",
        "default": "None",

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