# services/calculate_ahp.py

from typing import List, Dict
from ahpy import Compare
from services.format_results import format_results
from sqlalchemy.orm import Session


def calculate_ahp(ahp_input: List[Dict], criteria_weights: dict, db: Session, raw_frameworks: list) -> list[dict]:
    scores_accumulator = {}

    criterion_map = {}
    for fw in ahp_input:
        title = fw["title"]
        for crit, score in fw.get("criteria_scores", {}).items():
            criterion_map.setdefault(crit, {})[title] = score

    for criterion, framework_scores in criterion_map.items():
        comparisons = {}
        frameworks = list(framework_scores.keys())

        for i in range(len(frameworks)):
            for j in range(i + 1, len(frameworks)):
                a = frameworks[i]
                b = frameworks[j]
                a_score = framework_scores[a] or 1e-6
                b_score = framework_scores[b] or 1e-6
                comparisons[(a, b)] = a_score / b_score

        model = Compare(name=criterion, comparisons=comparisons, precision=5, random_index='saaty')
        weight = criteria_weights.get(criterion, 1.0)
        for fw, local_score in model.target_weights.items():
            scores_accumulator[fw] = scores_accumulator.get(fw, 0.0) + weight * local_score

    return format_results(scores_accumulator, raw_frameworks, db, method_key="ahp_score")
