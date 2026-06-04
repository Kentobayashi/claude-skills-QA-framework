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
    # prosma Skill Library
    # ─────────────────────────────────────────────────────────────
    {
        "name": "humanizer",
        "category": "Core",
        "folder": "humanizer",
        "trigger_pos": [
            "Kannst du diesen Text humanisieren? Er klingt zu sehr nach ChatGPT.\n\nIn der heutigen schnelllebigen digitalen Welt spielt die Fähigkeit, fokussiert zu arbeiten, eine zunehmend entscheidende Rolle. Zudem stellt die nahtlose Integration moderner Tools einen wesentlichen Mehrwert dar und trägt maßgeblich zur ganzheitlichen Optimierung der Arbeitsprozesse bei.",
            "This text sounds too polished and AI-generated. Can you make it sound more human?\n\nAI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolving landscape of software development. These groundbreaking tools—nestled at the intersection of research and practice—are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.",
            "Bitte entferne die KI-Spuren aus diesem Absatz – er ist zu glatt geschrieben.\n\nDas idyllisch im Herzen der Altstadt gelegene Unternehmen besticht durch seine einzigartige Unternehmenskultur und verzaubert seine Mitarbeitenden mit einem beeindruckenden Arbeitsumfeld. Darüber hinaus fungiert es als Plattform für facettenreichen fachlichen Austausch und stellt somit einen wegweisenden Meilenstein in der modernen Arbeitswelt dar.",
        ],
        "trigger_neg": [
            "Erstell mir eine neue Planner-Karte für das laufende Projekt.",
            "Translate this paragraph from German to English.",
        ],
        "output_criteria": (
            "Must detect the language of the provided text (German or English) and apply the matching pattern catalog. "
            "Must produce a first rewrite that visibly removes AI writing patterns. "
            "Must include a brief self-critique section identifying remaining AI tells. "
            "Must produce a second, final rewrite based on the self-critique. "
            "For German input: must address patterns like Nominalstil, KI-Lieblingswörter, "
            "Partizipialphrasen, and hollow openers. "
            "For English input: must address patterns like significance inflation, -ing endings, "
            "AI vocabulary words, and em dash overuse. "
            "Output must not itself sound AI-generated. "
            "Generic rewrites without visible pattern removal score low."
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
