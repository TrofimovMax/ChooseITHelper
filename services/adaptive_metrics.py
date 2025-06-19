# services/adaptive_metrics.py

from sqlalchemy.orm import Session
from models.resource import Resource, ResourceType
from models.framework import Framework


def calculate_metric_average(db: Session, framework_id: int, metric_type: ResourceType) -> float:
    print(f"\n[METRIC] Calculating {metric_type.value} for Framework ID: {framework_id}")
    records = db.query(Resource).filter(
        Resource.framework_id == framework_id,
        Resource.type == metric_type
    ).all()
    print(f"  ➤ Found {len(records)} resource records.")

    valid = [r for r in records if r.total and r.total > 0]
    print(f"  ➤ Valid entries (rank / total > 0): {len(valid)}")

    if not valid:
        return 0.0

    normalized_sum = sum(r.rank / r.total for r in valid)
    average = normalized_sum / len(valid)
    print(f"  ➤ Normalized average: {average:.5f}")
    return average


def calculate_adaptive_coefficient(db: Session, framework_id: int) -> float:
    print(f"\n[COEFFICIENT] Calculating adaptive coefficient for Framework ID: {framework_id}")
    framework = db.query(Framework).filter(Framework.id == framework_id).first()
    if not framework:
        print("  ❌ Framework not found.")
        return 0.0

    f_ij = calculate_metric_average(db, framework_id, ResourceType.feasibility)
    n_ij = calculate_metric_average(db, framework_id, ResourceType.novelty)
    u_ij = calculate_metric_average(db, framework_id, ResourceType.usefulness)

    alpha = framework.feasibility or 0.0
    beta = framework.novelty or 0.0
    gamma = framework.usefulness or 0.0

    p_ij = (alpha * f_ij + beta * n_ij + gamma * u_ij) / 3
    print(f"  ➤ α = {alpha}, β = {beta}, γ = {gamma}")
    print(f"  ➤ f_ij = {f_ij:.5f}, n_ij = {n_ij:.5f}, u_ij = {u_ij:.5f}")
    print(f"  → Adaptive coefficient p_ij = {p_ij:.5f}")

    return p_ij
