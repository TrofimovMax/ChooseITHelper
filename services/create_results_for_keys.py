# services/create_results_for_keys.py

from sqlalchemy.orm import Session
from models.result import Result
from models.key import Key
from services.calculate_ahp import calculate_ahp
from services.calculate_smart import calculate_smart
from services.calculate_adaptive_weighted_method import calculate_adaptive_weighted_method
from services.fetch_frameworks_by_filters import fetch_frameworks_by_filters
from services.prepare_criteria_and_alternatives import prepare_criteria_and_alternatives
from services.prepare_matrix_parameters import prepare_matrix_parameters


def create_results_for_keys(query_keys: list[str], db: Session):
    """
    Create results for the given query keys by evaluating frameworks.
    """
    # Fetch key IDs for the query keys
    keys = db.query(Key.id).filter(Key.key.in_(query_keys)).all()
    keys_ids = [key.id for key in keys]

    if not keys_ids:
        raise ValueError("No matching keys found in the database.")

    # Separate keys into criteria and alternatives
    criteria, alternatives = prepare_criteria_and_alternatives(keys_ids, db)

    # Fetch top 5 frameworks based on matching key counts
    top_frameworks = fetch_frameworks_by_filters(keys_ids, db)

    if not top_frameworks:
        raise ValueError("No matching frameworks found for the given keys.")

    # Prepare parameters for AHP and SMART calculations
    ahp_parameters = smart_parameters = prepare_matrix_parameters(top_frameworks, criteria, alternatives, db)

    # Calculate results for each framework
    smart_results = {
        param["framework_id"]: calculate_smart(param["framework_id"], alternatives)
        for param in smart_parameters
    }

    ahp_results = {
        param["framework_id"]: calculate_ahp(param["framework_id"], criteria)
        for param in ahp_parameters
    }

    adaptive_weighted_results = calculate_adaptive_weighted_method()

    # Store the results in the database
    new_result = Result(
        query_keys=query_keys,
        smart_results=smart_results,
        ahp_results=ahp_results,
        adaptive_weighted_results=adaptive_weighted_results,
    )

    db.add(new_result)
    db.commit()

    return new_result
