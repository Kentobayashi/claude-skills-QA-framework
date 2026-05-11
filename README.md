# claude-skills-QA-framework

> **Automated quality assurance for Claude Skills — tests trigger accuracy, output quality, false positives, and consistency via the Anthropic API.**

---

## What is this?

A lightweight Python framework that automatically evaluates Claude Skills across four quality dimensions:

| Dimension | What it tests | Max score |
|---|---|---|
| **T — Trigger Quality** | Do the right prompts activate the skill? | 5 pts |
| **FP — False Positives** | Does the skill stay silent when it shouldn't activate? | 5 pts |
| **O — Output Quality** | Does the output meet the defined quality criteria? | 5 pts |
| **K — Consistency** | Does the skill produce consistent results across runs? | 5 pts |
| **Total** | | **20 pts** |

**Thresholds:**
- ≥16/20 ✅ Released — ready for production
- 11–15  ⚠️ Fix needed
- ≤10    🔴 Rebuild from scratch

Results are exported as a formatted XLSX file with color-coded scores.

---

## How it works

```
skill_eval_runner.py        ← Main runner — runs all tests via Anthropic API
skill_eval_data.py          ← Your skill definitions with test cases
skills/                     ← Your local skill library (SKILL.md files)
```

For each skill, the runner:
1. Reads the `SKILL.md` from your local library
2. Sends 3 positive trigger prompts → checks if the skill activates
3. Sends 2 negative trigger prompts → checks for false positives
4. Generates a full output using the main model
5. Uses an LLM judge to score the output against your criteria
6. Runs a second output generation to measure consistency
7. Writes everything to a formatted Excel report

---

## Setup

### 1. Clone this repo

```bash
git clone https://github.com/Kentobayashi/claude-skills-QA-framework.git
cd claude-skills-QA-framework
```

### 2. Install dependencies

```bash
pip install anthropic openpyxl pyyaml
```

### 3. Set your Anthropic API key

**Windows CMD:**
```cmd
set ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Windows PowerShell:**
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

**macOS / Linux:**
```bash
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

For a permanent setup on Windows, use:
```powershell
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-your-key-here", "User")
```

### 4. Set your skill library path

Open `skill_eval_runner.py` and set `REPO_PATH` to your local skill library folder:

```python
REPO_PATH = Path("./skills")   # Default: skills/ folder in this repo
```

Your skills should follow this structure:
```
skills/
├── core-skills/
│   └── my-skill/
│       └── SKILL.md
└── light-skills/
    └── another-skill/
        └── SKILL.md
```

### 5. Define your skills in skill_eval_data.py

The `skill_eval_data.py` file contains example entries. Replace them with your own skills:

```python
SKILLS = [
    {
        "name": "my-skill",
        "category": "Core",               # Any label — used for filtering
        "folder": "core-skills/my-skill", # Path relative to REPO_PATH
        "trigger_pos": [
            "Prompt that should activate the skill",
            "Another trigger prompt",
            "A third trigger prompt",
        ],
        "trigger_neg": [
            "Prompt that should NOT activate the skill",
            "Another negative example",
        ],
        "output_criteria": (
            "Must contain: X, Y, Z. "
            "The output should do A and B. "
            "Vague or generic output scores low."
        ),
    },
]
```

---

## Usage

```bash
# Test all skills
python skill_eval_runner.py

# Test one specific skill
python skill_eval_runner.py --skill my-skill

# Test by category
python skill_eval_runner.py --category Core

# Dry run — check structure without API calls (free)
python skill_eval_runner.py --dry-run
```

---

## Cost & Time Estimates

| Scope | API Calls | Estimated Cost | Estimated Time |
|---|---|---|---|
| 1 skill | ~9 | ~$0.18 | ~2–3 min |
| 10 skills | ~90 | ~$1.80 | ~20–30 min |
| 36 skills | ~324 | ~$6.50 | ~75 min |

Costs depend on output length. The runner uses:
- `claude-haiku-4-5` for trigger detection and judging (cheap)
- `claude-sonnet-4-6` for output generation (quality)

You can change both models in `skill_eval_runner.py` under `CONFIGURATION`.

---

## Output

Results are saved as a formatted `.xlsx` file:

```
skill-eval-20260510-1849.xlsx
```

The file contains:
- Summary row (total skills, pass/fix/rebuild counts, average score)
- Color-coded score columns per skill
- Green/yellow/red gradient on the Total column
- Notes with the LLM judge's reasoning

---

## Folder Structure

```
claude-skills-QA-framework/
├── skill_eval_runner.py    # Main runner
├── skill_eval_data.py      # Skill definitions with test cases
├── skills/                 # Your skill library (add your SKILL.md files here)
│   └── (empty by default — add your own skills)
└── README.md
```

---

## Tips for good test cases

**trigger_pos** — Make prompts realistic and varied:
- Use different phrasings of the same intent
- Include context that a real user would provide
- At least one should be very specific, one more general

**trigger_neg** — Make them clearly unrelated:
- Different domain (tech vs. business vs. creative)
- Similar-sounding but different intent
- Avoid edge cases that could genuinely be ambiguous

**output_criteria** — Be specific:
- List concrete elements that must appear in the output
- Mention what scores low ("generic advice without examples scores low")
- Include framework names if the skill is based on a specific methodology

---

## License

Apache-2.0 — see [LICENSE](LICENSE) for details.

## Author

[Kentobayashi](https://github.com/Kentobayashi)

---

*Built for the [kaizen-consulting-skill](https://github.com/Kentobayashi/kaizen-consulting-skill) project and the broader Claude Skills ecosystem.*
