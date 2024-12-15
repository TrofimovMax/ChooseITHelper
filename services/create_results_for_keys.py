# services/create_results_for_keys.py

from models.result import Result


def create_results_for_keys(query_keys: list[str]):
    new_result = Result(
        query_keys=query_keys,
        smart_results={"example_framework": 0.85},
        ahp_results={"example_framework": 0.90},
        adaptive_weighted_results={
            "example_framework": {
                "feasibility": 0.8,
                "novelty": 0.75,
                "usefulness": 0.9,
            }
        },
    )

    return new_result
