"""
Claude Skills QA Framework – Eval Test Data
─────────────────────────────────────────────
Define your skills here. Each entry requires:

    name            str   — matches the skill folder name
    category        str   — "Core" or "Light" (or any label you prefer)
    folder          str   — path relative to REPO_PATH where SKILL.md lives
    trigger_pos     list  — 3 prompts that SHOULD activate the skill
    trigger_neg     list  — 2 prompts that should NOT activate the skill
    output_criteria str   — what a good output must contain (used by LLM judge)

Scoring thresholds:
    ≥16/20  ✅  Released — ready for production
    11-15   ⚠️  Fix needed
    ≤10     🔴  Rebuild from scratch

Cost estimate: ~$0.18 per skill, ~2-3 min per skill with 8000 output tokens.
"""

SKILLS = [

    # ─────────────────────────────────────────────────────────────
    # prosma Skill Library — profilpilot (consultant short-profile tailoring)
    # Note: consultant names and internal phrasing are genericized for this
    # public example. The canonical, fully-specified definition lives in the
    # prosma skill repo.
    # ─────────────────────────────────────────────────────────────
    {
        "name": "prosma_profilpilot",
        "category": "Core",
        "folder": "prosma_profilpilot",
        # trigger_pos[0] also drives the output- and consistency-runs.
        "trigger_pos": [
            "Wir haben eine Ausschreibung für eine Projektleitung / PMO im öffentlichen Sektor "
            "(Steuerung einer M365-Migration, Lieferantensteuerung, Stakeholdermanagement). "
            "Bitte passe das Berater-Kurzprofil von [Berater:in] darauf an und gib mir die "
            "copy-paste-fertigen Texte für alle Folien.",
            "Ich brauche das Kurzprofil von [Berater:in] für eine Prozessberatungs-"
            "Ausschreibung angepasst — kannst du das machen?",
            "Für eine:n neue:n Kolleg:in gibt es noch keine Berater-Datenbank. "
            "Kannst du anhand der alten Kurzprofile eine anlegen?",
        ],
        "trigger_neg": [
            "Erstell mir eine neue Planner-Karte für das laufende Projekt.",
            "Wie modelliere ich diesen End-to-End-Prozess sauber in BPMN 2.0?",
        ],
        "output_criteria": (
            "Must produce copy-paste-ready German texts for a consultant short-profile "
            "(PowerPoint) tailored to a specific tender: a title/role slide, a personal "
            "profile, a 'best-fit candidate' section, a main project, and a project-reference "
            "table. Must write in third person, avoid empty buzzwords and marketing clichés, "
            "and back every claim with a concrete approach rather than a generic statement. "
            "Must not invent facts (certificates, customers, dates, numbers) that aren't given "
            "— it asks back or marks them as to-complete instead. "
            "Generic, interchangeable profile text or invented specifics score low."
        ),
    },

    # ─────────────────────────────────────────────────────────────
    # EXAMPLE SKILL 1 — Replace with your own skills
    # ─────────────────────────────────────────────────────────────
    {
        "name": "example-negotiation-skill",
        "category": "Core",
        "folder": "core-skills/example-negotiation-skill",
        # trigger_pos: 3 prompts that should activate this skill
        "trigger_pos": [
            "How do I prepare for a difficult salary negotiation with my manager?",
            "The client wants a 20% discount – how do I respond strategically?",
            "Help me develop a negotiation strategy for tomorrow's contract discussion.",
        ],
        # trigger_neg: 2 prompts that should NOT activate this skill
        "trigger_neg": [
            "What is the best cloud architecture for a scalable web app?",
            "How do I write a Python script to process CSV files?",
        ],
        # output_criteria: what must the output contain to score well
        "output_criteria": (
            "Must contain: concrete negotiation tactics (e.g. anchoring, BATNA, mirroring), "
            "a clear preparation checklist, and specific language examples. "
            "Generic advice without actionable techniques scores low."
        ),
    },

    # ─────────────────────────────────────────────────────────────
    # EXAMPLE SKILL 2 — Replace with your own skills
    # ─────────────────────────────────────────────────────────────
    {
        "name": "example-content-writer-skill",
        "category": "Light",
        "folder": "light-skills/example-content-writer-skill",
        "trigger_pos": [
            "Help me write a LinkedIn article about AI trends in the consulting industry.",
            "I need an outline for a blog post about remote team management.",
            "Give me feedback on this draft section of my whitepaper on digital transformation.",
        ],
        "trigger_neg": [
            "How do I extract text from a PDF file using Python?",
            "What is the difference between SQL and NoSQL databases?",
        ],
        "output_criteria": (
            "Must contain: a structured outline (hook, intro, main sections, conclusion), "
            "audience and tone considerations, and at least one concrete content suggestion. "
            "Asking clarifying questions instead of delivering content scores low."
        ),
    },

    # ─────────────────────────────────────────────────────────────
    # EXAMPLE SKILL 3 — Replace with your own skills
    # ─────────────────────────────────────────────────────────────
    {
        "name": "example-change-management-skill",
        "category": "Light",
        "folder": "light-skills/example-change-management-skill",
        "trigger_pos": [
            "We're rolling out a new CRM for 150 employees. How do I structure the change process?",
            "Half our team is resisting the new tool adoption. What change management approach should I use?",
            "Help me build a communication plan for a major organizational restructuring.",
        ],
        "trigger_neg": [
            "How do I refactor this Python function to be more readable?",
            "What is the CAP theorem in distributed systems?",
        ],
        "output_criteria": (
            "Must contain: stakeholder segmentation, a phased rollout approach, "
            "a communication framework with specific messages, and risk mitigation tactics. "
            "Generic change management theory without project-specific application scores low."
        ),
    },

]

# ─────────────────────────────────────────────────────────────────
# HOW TO ADD YOUR OWN SKILLS:
#
# 1. Copy one of the blocks above
# 2. Set "name" to your skill folder name (must match the folder)
# 3. Set "folder" to the path relative to REPO_PATH
#    Example: if REPO_PATH = "./skills" and your SKILL.md is at
#             "./skills/core-skills/my-skill/SKILL.md"
#             then folder = "core-skills/my-skill"
# 4. Write 3 trigger_pos prompts that should activate the skill
# 5. Write 2 trigger_neg prompts that should NOT activate it
# 6. Define output_criteria: what must a good response contain?
# ─────────────────────────────────────────────────────────────────
