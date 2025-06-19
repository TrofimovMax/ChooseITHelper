# services/calculate_ahp.py

from typing import List, Dict
from ahpy import Compare
from services.format_results import format_results
from sqlalchemy.orm import Session


def calculate_ahp(
    ahp_input: List[Dict],
    criteria_weights: dict,
    db: Session,
    raw_frameworks: list,
    reporter=None
) -> list[dict]:
    scores_accumulator = {}
    criterion_map = {}

    for fw in ahp_input:
        title = fw["title"]
        for crit, score in fw.get("criteria_scores", {}).items():
            criterion_map.setdefault(crit, {})[title] = score

    if reporter:
        reporter.add_section("AHP Formula", r"$S_j = \sum_{i=1}^{n} w_i \cdot s_{ij}$, where $s_{ij}$ is the local priority of alternative $j$ for criterion $i$.")

    for criterion, framework_scores in criterion_map.items():
        comparisons = {}
        frameworks = list(framework_scores.keys())
        matrix = []

        for i in range(len(frameworks)):
            row = []
            for j in range(len(frameworks)):
                a_score = framework_scores[frameworks[i]] or 1e-6
                b_score = framework_scores[frameworks[j]] or 1e-6
                value = a_score / b_score
                row.append(f"{value:.3f}")
                if i < j:
                    comparisons[(frameworks[i], frameworks[j])] = value
            matrix.append(row)

        if reporter:
            safe_criterion = criterion.replace('_', r'\_')
            table = []

            table.append(r"\begin{longtable}{l" + " r" * len(frameworks) + "} ")
            table.append(r"\toprule")
            table.append(" & " + " & ".join(frameworks) + r" \\ \midrule")

            for i, row in enumerate(matrix):
                table.append(f"{frameworks[i]} & " + " & ".join(row) + r" \\")

            table.append(r"\bottomrule \end{longtable}")
            reporter.add_section(f"Pairwise Matrix for {safe_criterion}", "\n".join(table))

        model = Compare(name=criterion, comparisons=comparisons, precision=5, random_index='saaty')
        weight = criteria_weights.get(criterion, 1.0)

        for fw, local_score in model.target_weights.items():
            scores_accumulator[fw] = scores_accumulator.get(fw, 0.0) + weight * local_score

    total = sum(scores_accumulator.values()) or 1e-6
    normalized_scores = {k: v / total for k, v in scores_accumulator.items()}

    if reporter:
        summary = [r"\begin{longtable}{l r} \toprule Framework & Normalized AHP Score \\ \midrule"]
        for title, score in normalized_scores.items():
            summary.append(f"{title} & {score:.5f} \\\\")
        summary.append(r"\bottomrule \end{longtable}")
        reporter.add_section("Final AHP Scores", "\n".join(summary))

    return format_results(normalized_scores, raw_frameworks, db, method_key="ahp_score")
