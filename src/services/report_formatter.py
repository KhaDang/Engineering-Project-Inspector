

class ReportFormatter:

    def report(
        self,
        progress,
        stats,
        config
    ):

        for level, title, attribute in config:
            value = getattr(
                stats,
                attribute
            )
            if level == "info":
                progress.info(f"{title}: {value}")
            else:
                progress.warning(f"{title}: {value}")

