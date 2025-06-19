# services/adaptive_metrics.py

from sqlalchemy.orm import Session
from models.resource import Resource, ResourceType
from models.framework import Framework
from services.helpers.latex_report import LaTeXReport


def calculate_metric_average(db: Session, framework_id: int, metric_type: ResourceType,
                             reporter: LaTeXReport = None) -> float:
    records = db.query(Resource).filter(
        Resource.framework_id == framework_id,
        Resource.type == metric_type
    ).all()

    valid = [r for r in records if r.total and r.total > 0]

    if not valid:
        return 0.0

    normalized_sum = sum(r.rank / r.total for r in valid)
    average = normalized_sum / len(valid)

    if reporter:
        rows = [
            r"\begin{longtable}{l l}",
            r"\toprule",
            f"Metric type & {metric_type.value} \\",
            f"Total resources & {len(records)} \\",
            f"Valid resources & {len(valid)} \\",
            f"Normalized average & {average:.5f} \\",
            r"\bottomrule",
            r"\end{longtable}"
        ]
        reporter.add_section(f"Metric Calculation: {metric_type.value}", "\n".join(rows))

    return average


def calculate_adaptive_coefficient(db: Session, framework_id: int, reporter: LaTeXReport = None) -> float:
    framework = db.query(Framework).filter(Framework.id == framework_id).first()
    if not framework:
        if reporter:
            reporter.add_section(f"Adaptive Coefficient for Framework ID {framework_id}", "Framework not found.")
        return 0.0

    f_ij = calculate_metric_average(db, framework_id, ResourceType.feasibility, reporter)
    n_ij = calculate_metric_average(db, framework_id, ResourceType.novelty, reporter)
    u_ij = calculate_metric_average(db, framework_id, ResourceType.usefulness, reporter)

    alpha = framework.feasibility or 0.0
    beta = framework.novelty or 0.0
    gamma = framework.usefulness or 0.0

    p_ij = (alpha * f_ij + beta * n_ij + gamma * u_ij) / 3

    if reporter:
        rows = [
            r"\begin{longtable}{l l}",
            r"\toprule",
            f"Alpha (feasibility weight) & {alpha:.2f} \\",
            f"Beta (novelty weight) & {beta:.2f} \\",
            f"Gamma (usefulness weight) & {gamma:.2f} \\",
            f"f_ij & {f_ij:.5f} \\",
            f"n_ij & {n_ij:.5f} \\",
            f"u_ij & {u_ij:.5f} \\",
            f"\textbf{{p_ij}} & \textbf{{{p_ij:.5f}}} \\",
            r"\bottomrule",
            r"\end{longtable}"
        ]
        reporter.add_section(f"Adaptive Coefficient for {framework.title}", "\n".join(rows))

    return p_ij
