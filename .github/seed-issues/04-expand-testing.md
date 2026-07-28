**Title:** [Phase 2] Expand testing to proper pytest + more coverage

**Labels:** phase-2, testing, security

**Body:**

Current tests live in `tests/test_pilot.py` as ad-hoc scripts (14 tests passing).

We need to:
- Convert to a real pytest structure (`tests/test_*.py`)
- Add fixtures for EnhancedHome, Timelock, Protocol, etc.
- Increase coverage for edge cases (zero participation, full paydown, recall with exactly 3/5 votes, over-allocation attempts, etc.)
- Add property-based or hypothesis tests if feasible
- Integrate with the CI workflow

**References:**
- `specs/testing_plan.md`
- `prototypes/pilot_simulation.py`
- Current `tests/test_pilot.py`

**Acceptance criteria:**
- `pytest` command runs the full suite cleanly
- At least 25+ tests
- CI passes on every push

**Milestone:** Phase 2 - Testing & Hardening
