from rules.missing_record_rule import MissingRecordRule

class FolderInspectorConfig:
    # Configuration for radio buttons
    TYPE_OPTIONS = {
        "dir1": "Missing in Dir 1",
        "dir2": "Missing in Dir 2",
        "match": "Matching",
        "default": "None",

    }

    ENABLE_REVISION = False

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