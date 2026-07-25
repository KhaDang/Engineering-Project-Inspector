from rules.missing_record_rule import MissingRecordRule

class FileInspectorConfig:

    TYPE_OPTIONS = {
        "bom": "Missing in bom",
        "folder": "Missing in folder",
        "match": "Matching",
        "default": "None",

    }

    ENABLE_REVISION = False

    RULES = [
        MissingRecordRule(),
        # RevisionRule,
        # DuplicateRule,
    ]

    KEY_COLUMNS = [
        "BOM Key",
    #     "Revision",
    #     "Some key",
    #     "Another key"
    ]

    REPORT_TABLE_COLUMNS = [
        "Drawing Number",
        ".sldprt",
        ".slddrw",
        ".sldasm",
        "Status"
    ]