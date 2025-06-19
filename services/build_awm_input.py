# services/build_awm_input.py

from typing import List, Dict


def enrich_frameworks_with_meta(
    frameworks: List[Dict],
    raw_frameworks: List
) -> List[Dict]:
    """
    Adds fields to frameworks structures:
    - id
    - feasibility
    - novelty
    - usefulness
    Found in raw_frameworks ORM models.
    """
    enriched = []

    for fw in frameworks:
        match = next(
            (rf for rf in raw_frameworks if rf.title == fw["title"]), None
        )
        if match:
            fw["id"] = match.id
            fw["feasibility"] = match.feasibility
            fw["novelty"] = match.novelty
            fw["usefulness"] = match.usefulness
            enriched.append(fw)

    return enriched
