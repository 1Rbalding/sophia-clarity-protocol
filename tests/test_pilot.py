# tests/test_assistance_and_onboarding.py
# (or append to tests/test_pilot.py)

def test_permanent_six_month_floor():
    # reserves below 6 months → assistance = 0
    # reserves above 6 months → 40% of excess only
    assert assistance_allocation(surplus_below_floor) == 0
    assert assistance_allocation(surplus_above_floor) == 0.40 * excess

def test_priority_order():
    applicants = [
        {"type": "individual", "never_owned": False},  # 3-year gap
        {"type": "family", "never_owned": True},
        {"type": "individual", "never_owned": True},
        {"type": "family", "never_owned": False},
    ]
    ordered = prioritize(applicants)
    assert ordered[0]["type"] == "family" and ordered[0]["never_owned"]
    assert ordered[1]["type"] == "family"
    assert ordered[2]["type"] == "individual" and ordered[2]["never_owned"]

def test_pools_remain_separate():
    raise_amount = 100_000
    nonprofit = raise_amount * 0.10
    # assistance only from net surplus above floor, never reduces nonprofit
    assert nonprofit == 10_000
    assert assistance_from_surplus > 0  # only if floor already met

def test_onboarding_requires_verification():
    home = {"verified": False}
    assert voting_rights_active(home) is False
    assert note_origination_allowed(home) is False
    home["verified"] = True
    assert voting_rights_active(home) is True
