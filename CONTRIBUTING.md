# Contributing to Sophia (Clarity Protocol)

Thank you for your interest in Sophia — the homeowner-governed residential credit and mutual support system.

This is the **people’s protocol**. Contributions should align with the core principles in the Presidential Packet and specs.

## How to Contribute

1. **Read the core docs first**
   - [README.md](README.md)
   - [specs/requirements_and_tokenomics.md](specs/requirements_and_tokenomics.md)
   - [launch/roadmap.md](launch/roadmap.md)
   - [specs/testing_plan.md](specs/testing_plan.md)

2. **Fork & Branch**
   - Fork the repo
   - Create a feature branch from `main`: `git checkout -b feature/your-idea`

3. **Make Changes**
   - Follow existing code style (simple, readable Python in prototypes and src).
   - Add or update ad-hoc tests in `tests/test_pilot.py` when changing behavior.
   - Keep non-profit 10% guard and founder recall mechanics intact.
   - When editing CI, templates, or docs, ensure changes support transparent, low-degradation governance.

4. **Test**
   ```bash
   python tests/test_pilot.py
   ```

   For CI changes, you can validate the workflow locally by checking YAML syntax or using `act` if available.

5. **Submit a Pull Request**
   - Use the PR template.
   - Reference relevant issues or roadmap items.
   - One focused change per PR when possible.

## Code of Conduct
Be respectful. This project prioritizes homeowner self-governance, protection of the vulnerable, and transparency. No institutional capture, no pump mechanics.

## Running Verification (for edits)
After certain code or script changes, an ad-hoc verification using a `hermes-verify-*.py` script in Temp is performed to confirm behavior (see past commits for examples). This is lightweight and focused on the changed files.

## Questions?
Open an issue with the "question" label or discuss in the repo Discussions tab (once enabled).

Participation is the path.
