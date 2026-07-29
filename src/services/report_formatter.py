import pandas as pd

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

    def create_report(self,report_type, results, columns):
        report = []
        if len(results)>0:
            for drawing in results:
                if report_type == 1 :
                    report.append(drawing.to_table_row())
                if report_type == 2:
                    report.append(drawing.to_table_row_rev())
                if report_type == 3:
                    report.append(drawing.to_table_row_fol())

        df = pd.DataFrame(report, columns=columns)
        df.to_excel("Report.xlsx", index=False)
