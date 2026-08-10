# import issues
from rules.missing_record_rule import MissingInLeft, MissingInRight

class DialogCopyMissingConfig:
    # For type selector radio buttons configuration
    TYPE_OPTIONS = {
        "left": 'MissingInLeft',
        "right": 'MissingInRight',

    }
    FILTER = {
        "left": MissingInLeft,
        "right": MissingInRight,
    }

    CHECK_OPTIONS = {
        ".sldprt": ".sldprt",
        ".sldasm": ".sldasm",
        ".slddrw": ".slddrw",
        ".pdf": ".pdf",
        ".step": ".step"
    }
