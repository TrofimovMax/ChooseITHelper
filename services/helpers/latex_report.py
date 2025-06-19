# services/helpers/latex_report.py

from datetime import datetime
from pathlib import Path


class LaTeXReport:
    def __init__(self, title: str = "Calculation Report"):
        self.title = title
        self.sections = []
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        project_root = Path(__file__).resolve().parent.parent.parent
        reports_dir = project_root / "reports"

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.filename = reports_dir / f"{self.title.replace(' ', '_')}_{timestamp}.tex"

    def add_section(self, title: str, content: str):
        self.sections.append((title, content))

    def save(self):
        content = [
            r"\documentclass{article}",
            r"\usepackage{amsmath, booktabs, geometry, longtable}",
            r"\geometry{a4paper, margin=1in}",
            r"\title{%s}" % self.title,
            r"\author{ChooseITHelper Engine}",
            r"\begin{document}",
            r"\maketitle",
        ]
        for title, body in self.sections:
            content.append(r"\section*{%s}" % title)
            content.append(body)
        content.append(r"\end{document}")

        self.filename.parent.mkdir(parents=True, exist_ok=True)
        self.filename.write_text("\n".join(content), encoding="utf-8")
        return self.filename
