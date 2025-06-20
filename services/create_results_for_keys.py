# services/create_results_for_keys.py

from sqlalchemy.orm import Session
from models.result import Result
from models.key import Key
from services.build_ahp_input import build_ahp_input
from services.build_awm_input import enrich_frameworks_with_meta
from services.build_smart_input import build_smart_input
from services.calculate_ahp import calculate_ahp
from services.calculate_criteria_weights import calculate_criteria_weights
from services.calculate_smart import calculate_smart
from services.calculate_adaptive_weighted_method import calculate_adaptive_weighted_method
from services.fetch_frameworks_by_filters import fetch_frameworks_by_filters
from services.helpers.latex_report import LaTeXReport
from services.prepare_criteria_and_alternatives import prepare_criteria_and_alternatives
from database import SessionLocal


def create_results_for_keys(query_keys: list[str], user_id: int):
    """
    Create results for the given query keys by evaluating frameworks.
    """
    db: Session = SessionLocal()
    try:
        # Fetch key IDs for the query keys
        keys = db.query(Key.id).filter(Key.title.in_(query_keys)).all()
        keys_ids = [key.id for key in keys]

        if not keys_ids:
            raise ValueError("No matching keys found in the database.")

        # Separate keys into criteria and alternatives
        criteria, alternatives = prepare_criteria_and_alternatives(keys_ids, db)

        # Fetch top 5 frameworks based on matching key counts
        top_frameworks = fetch_frameworks_by_filters(keys_ids, db)

        criteria_weights = calculate_criteria_weights(criteria, top_frameworks, db)

        if not top_frameworks:
            raise ValueError("No matching frameworks found for the given keys.")

        smart_input = build_smart_input(top_frameworks, criteria, db)
        smart_reporter = LaTeXReport("S.M.A.R.T. Report")
        smart_results = calculate_smart(smart_input, criteria_weights, db, top_frameworks, reporter=smart_reporter)
        smart_path_to_report = smart_reporter.save()
        print(f"📄 S.M.A.R.T. Report saved to: {smart_path_to_report}")

        ahp_input = build_ahp_input(top_frameworks, criteria, db)
        ahp_reporter = LaTeXReport("AHP Report")
        ahp_results = calculate_ahp(ahp_input, criteria_weights, db, top_frameworks, reporter=ahp_reporter)
        ahp_path_to_report = ahp_reporter.save()
        print(f"📄 AHP Report saved to: {ahp_path_to_report}")

        enriched_frameworks = enrich_frameworks_with_meta(ahp_input, top_frameworks)
        awm_reporter = LaTeXReport("AWM Report")
        awm_results = calculate_adaptive_weighted_method(
            frameworks=enriched_frameworks,
            criteria_weights=criteria_weights,
            raw_frameworks=top_frameworks,
            db=db,
            reporter=awm_reporter
        )
        awm_path_to_report = awm_reporter.save()
        print(f"📄 AWM Report saved to: {awm_path_to_report}")

        # Store the results in the database
        new_result = Result(
            user_id=user_id,
            query_keys=query_keys,
            smart_results=smart_results,
            ahp_results=ahp_results,
            awm_results=awm_results,
        )

        db.add(new_result)
        db.commit()
        return new_result
    finally:
        db.close()
