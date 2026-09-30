# core/data.py
# ─────────────────────────────────────────────────────────────
# Central data file. Update this to change portfolio content.
# No database needed — Django templates loop over these dicts.
#
# Case-study fields (role / problem / solution / features /
# architecture / learned) are all derived from the original
# project copy — edit freely, nothing is invented. Sections
# left as '' or [] are simply not rendered in the template.
# ─────────────────────────────────────────────────────────────

# ── Site-wide identity (used by every page via context processor) ──
PROFILE = {
    'name': 'Martin Kiuna',
    'first_name': 'Martin',
    'role': 'Software Engineer',
    'specialties': ['AI Systems', 'Security', 'Backend'],
    'tagline': (
        'I build intelligent, security-aware systems — ML-driven trading '
        'engines, autonomous threat-detection agents, and the Django & '
        'FastAPI backends behind them.'
    ),
    'location': 'Nairobi, Kenya',
    'email': 'kiunamartin2004@gmail.com',
    'github': 'https://github.com/RasMatoh',
    'linkedin': 'https://www.linkedin.com/in/martin-kiuna-964124341',
    'availability': 'Freelancing · open to new opportunities',
    'current_role': 'freelance developer',
    'current_employer': 'Bambastack Limited',
    'current_project': 'Majengo platform',
    'graduation': 'November 2026',
    'cv': 'img/martin-kiuna-cv.pdf',   # served from /static/
}

# ── Project categories (filters render from this — no dead tabs) ──
CATEGORIES = [
    {'slug': 'all',      'label': 'All'},
    {'slug': 'ai',       'label': 'AI / ML'},
    {'slug': 'security', 'label': 'Cybersecurity'},
    {'slug': 'trading',  'label': 'Trading'},
    {'slug': 'web',      'label': 'Web'},
    {'slug': 'ml',       'label': 'Machine Learning'},
]

PROJECTS = [
    {
        'id': 'trading-assistant',
        'image': 'img/projects/trading-assistant.png',   # preview image; delete this line to fall back to the emoji icon
        'title': 'AI-Powered Smart Trading Assistant',
        'short_desc': 'Cryptocurrency trading assistant using LSTM neural networks and technical indicators with paper trading simulation.',
        'full_desc': (
            'Final-year dissertation project. A multi-user crypto trading platform '
            'that generates buy/sell signals using LSTM models trained on OHLCV data. '
            'Features Admin and Trader roles, a 10-table normalized PostgreSQL schema, '
            'and a real-time paper trading engine backed by FastAPI.'
        ),
        'impact': '68% signal accuracy on BTC/ETH pairs across LSTM + RSI/MACD indicators.',
        'stack': ['Python', 'FastAPI', 'LSTM', 'PostgreSQL', 'Binance API', 'React'],
        'categories': ['ai', 'trading', 'ml'],
        'icon': '🤖',
        'banner_class': 'banner-ai',
        'github': 'https://github.com/RasMatoh/AI-TRADING-ASSISTANT',
        'demo': '',
        'featured': True,

        # ── Case study (derived from the copy above) ──
        'role': 'Sole developer · final-year dissertation project',
        'problem': (
            'Crypto markets emit a continuous stream of OHLCV data, but raw price '
            'history alone doesn’t produce actionable decisions. The challenge was '
            'turning that stream into reliable buy/sell signals — and validating '
            'them without risking real capital.'
        ),
        'solution': (
            'A multi-user trading platform that trains LSTM models on OHLCV data '
            'and fuses their output with RSI and MACD technical indicators. Every '
            'signal can be executed against a real-time paper trading engine, so '
            'strategies are proven in simulation before touching live funds.'
        ),
        'features': [
            'LSTM models trained on OHLCV market data',
            'RSI + MACD indicators fused with model output',
            'Multi-user platform with Admin / Trader roles',
            'Real-time paper trading engine (FastAPI)',
            'Normalized 10-table PostgreSQL schema',
            '68% signal accuracy measured on BTC/ETH pairs',
        ],
        'architecture': [
            'Signal layer — LSTM inference combined with technical-indicator checks',
            'Trading engine — FastAPI service executing simulated orders in real time',
            'Data layer — PostgreSQL, 10 normalized tables for users, roles and trades',
            'Market data — Binance API feeds; React frontend for the trader view',
        ],
        'learned': (
            'Designing a schema that both an ML pipeline and a live trading engine '
            'can trust, and keeping model output cleanly separated from execution '
            'logic so either side can evolve independently.'
        ),
    },
    {
        'id': 'threat-detection',
        'image': 'img/projects/threat-detection.png',   # preview image; delete this line to fall back to the emoji icon
        'title': 'Cybersecurity Threat Detection Agent',
        'short_desc': 'Autonomous AI agent that monitors network traffic and classifies threats in real-time.',
        'full_desc': (
            'An autonomous agent that ingests network traffic data, runs it through '
            'ML-based classifiers, and produces incident reports with severity levels. '
            'Combines rule-based and ML-driven detection pipelines for five attack categories.'
        ),
        'impact': 'Reduced simulated threat detection time by 70% vs manual review.',
        'stack': ['Python', 'Scikit-learn', 'Wireshark', 'Nmap', 'Flask'],
        'categories': ['security'],
        'icon': '🔐',
        'banner_class': 'banner-sec',
        'github': 'https://github.com/RasMatoh/cybersentinel',
        'demo': '',
        'featured': True,

        # ── Case study ──
        'role': 'Sole developer',
        'problem': (
            'Manually reviewing network traffic doesn’t scale — attacks hide in '
            'volume. Detection needed to run continuously, classify threats into '
            'known attack categories, and surface incidents with severity so a '
            'human only reviews what matters.'
        ),
        'solution': (
            'An autonomous agent that ingests traffic data and runs it through two '
            'complementary pipelines — deterministic rules for known patterns and '
            'Scikit-learn classifiers for everything else — producing incident '
            'reports with severity levels across five attack categories.'
        ),
        'features': [
            'Autonomous, continuous traffic ingestion',
            'Hybrid detection: rule-based + ML classifiers',
            'Incident reports with severity levels',
            'Coverage of five attack categories',
            '70% faster detection than manual review (simulated)',
        ],
        'architecture': [
            'Ingestion — packet-level data captured with Wireshark; recon with Nmap',
            'Detection — Scikit-learn classifiers beside a rule-based pipeline',
            'Reporting — Flask service rendering incidents with severities',
        ],
        'learned': (
            'Why hybrid detection wins in practice: rules catch the known with '
            'zero false-positive cost, models catch the novel — and the reporting '
            'layer is what actually makes either one useful.'
        ),
    },
    {
        'id': 'binance-bot',
        'image': 'img/projects/binance-bot.png',   # preview image; delete this line to fall back to the emoji icon
        'title': 'Binance Automated Trading Bot',
        'short_desc': 'Python bot executing live and paper trades using RSI, MACD, and Bollinger Band strategies.',
        'full_desc': (
            'Connects to Binance via REST and WebSocket APIs to execute trades '
            'based on configurable technical indicator strategies. Includes stop-loss, '
            'take-profit logic, and a backtesting module for strategy validation.'
        ),
        'impact': 'Automated execution improving decision speed by 60% over manual trading.',
        'stack': ['Python', 'Binance API', 'TA-Lib', 'Pandas', 'WebSockets'],
        'categories': ['trading', 'ai'],
        'icon': '📈',
        'banner_class': 'banner-fin',
        'github': 'https://github.com/RasMatoh/Crypto-trading-bot',
        'demo': '',
        'featured': True,

        # ── Case study ──
        'role': 'Sole developer',
        'problem': (
            'Indicator-based strategies only work if execution is immediate — '
            'watching charts manually introduces delay and emotion. The bot needed '
            'to watch live markets and act on signals faster and more consistently '
            'than a human, with risk controls it never bypasses.'
        ),
        'solution': (
            'A Python trading bot connected to Binance over REST and WebSockets. '
            'Configurable RSI, MACD and Bollinger Band strategies fire trades the '
            'moment conditions are met, always guarded by stop-loss and take-profit '
            'logic, with a backtesting module to validate strategies on history first.'
        ),
        'features': [
            'Live market data over WebSocket, execution over REST',
            'Configurable RSI, MACD and Bollinger Band strategies',
            'Mandatory stop-loss / take-profit risk controls',
            'Backtesting module for strategy validation',
            'Paper and live trading modes',
            '60% faster decisions than manual trading',
        ],
        'architecture': [
            'Market feed — Binance WebSocket stream normalized with Pandas',
            'Signals — TA-Lib indicators behind a strategy interface',
            'Execution — order placement with stop-loss / take-profit attach',
            'Validation — backtester replaying historical candles',
        ],
        'learned': (
            'That the unglamorous parts — reconnect handling, risk checks that '
            'cannot be skipped, and honest backtests — are what separate a toy '
            'script from a system you can leave running.'
        ),
    },
    {
        'id': 'loan-expert-system',
        'image': 'img/projects/loan-expert-system.png',   # preview image; delete this line to fall back to the emoji icon
        'title': 'Loan Approval Expert System',
        'short_desc': 'Rule-based expert system for automated loan approval using forward chaining inference.',
        'full_desc': (
            'Implements a knowledge base and forward-chaining inference engine in Python '
            'to evaluate loan applications. Each decision comes with a transparent, '
            'auditable explanation — no black box. Also implemented in Prolog.'
        ),
        'impact': '95%+ eligibility decisions with full rule-trace explanations.',
        'stack': ['Python', 'Prolog', 'Forward Chaining', 'Expert Systems'],
        'categories': ['ai'],
        'icon': '🧠',
        'banner_class': 'banner-ml',
        'github': 'https://github.com/martinkiruna/loan-expert-system',   # update
        'demo': '',
        'featured': False,

        # ── Case study ──
        'role': 'Sole developer · implemented in both Python and Prolog',
        'problem': (
            'Automated credit decisions usually mean a black box — an applicant '
            'gets an answer with no reason. Eligibility screening needed to be '
            'fully auditable: every approval or rejection traceable to the exact '
            'rules that produced it.'
        ),
        'solution': (
            'A classic expert system: an explicit knowledge base of eligibility '
            'rules and a forward-chaining inference engine that evaluates each '
            'application. Every decision ships with its full rule trace, making '
            'the outcome explainable by construction rather than by post-hoc '
            'interpretation.'
        ),
        'features': [
            'Explicit knowledge base of eligibility rules',
            'Forward-chaining inference engine',
            'Full rule-trace explanation for every decision',
            'Dual implementation: Python engine and Prolog',
            '95%+ of applications decided with auditable traces',
        ],
        'architecture': [
            'Knowledge base — declarative rules, separate from the engine',
            'Inference — forward chaining deriving eligibility from facts',
            'Explanations — every fired rule recorded into the decision trace',
            'Parity check — same rule set implemented in Prolog to cross-validate',
        ],
        'learned': (
            'Symbolic AI hasn’t lost its place: when a decision must be explained '
            'to a human, a rule trace beats any model explanation technique — and '
            'separating knowledge from inference is what keeps the system maintainable.'
        ),
    },
    {
        'id': 'movie-booking',
        'image': 'img/projects/movie-booking.png',   # preview image; delete this line to fall back to the emoji icon
        'title': 'Movie Ticket Booking System',
        'short_desc': 'Full-stack Django app for cinema ticket reservations with seat selection and admin dashboard.',
        'full_desc': (
            'A complete cinema booking platform built with Django. Features seat '
            'selection, booking management, payment flow, and an admin dashboard. '
            'Race-condition-safe concurrent reservation logic ensures no double bookings.'
        ),
        'impact': 'Concurrent seat reservation with zero double-booking conflicts under load.',
        'stack': ['Django', 'PostgreSQL', 'HTML/CSS', 'JavaScript'],
        'categories': ['web'],
        'icon': '🎟️',
        'banner_class': 'banner-web',
        'github': 'https://github.com/RasMatoh/movie_ticket_booking',
        'demo': '',
        'featured': False,

        # ── Case study ──
        'role': 'Sole developer · full-stack',
        'problem': (
            'Booking systems fail at concurrency: two customers paying for the '
            'same seat is the bug that matters. The platform needed seat selection, '
            'payment and administration — with reservations that stay correct '
            'under simultaneous load.'
        ),
        'solution': (
            'A complete Django cinema platform: interactive seat selection, a '
            'booking pipeline with payment flow, and an admin dashboard for '
            'screenings and reservations. Concurrent bookings are made safe at '
            'the database level, so double-booking is impossible rather than rare.'
        ),
        'features': [
            'Interactive seat selection',
            'Booking management with payment flow',
            'Admin dashboard for screenings and reservations',
            'Race-condition-safe concurrent reservations',
            'Zero double-booking conflicts under load',
        ],
        'architecture': [
            'Application — Django (models, views, templates)',
            'Data integrity — PostgreSQL transactional reservation logic',
            'Frontend — server-rendered HTML/CSS with JavaScript seat-picker',
        ],
        'learned': (
            'Correctness under concurrency is designed in the data layer, not '
            'patched in the view — atomic transactions turn an entire class of '
            'bugs into a non-problem.'
        ),
    },
]

SKILLS = {
    'Security': ['Kali Linux', 'Nmap', 'Wireshark', 'Metasploit', 'Burp Suite', 'CTF / Red Team'],
    'AI / ML':  ['Python', 'LSTM / TensorFlow', 'Scikit-learn', 'Pandas', 'NumPy', 'Prolog'],
    'Backend':  ['Django', 'FastAPI', 'PostgreSQL', 'REST APIs', 'WebSockets'],
    'Frontend': ['HTML', 'CSS', 'JavaScript', 'Django Templates', 'React'],
    'Tools':    ['Git', 'GitHub', 'Linux', 'VS Code', 'Postman'],
}

STATS = [
    {'number': '5+', 'label': 'Major Projects'},
    {'number': '3',  'label': 'CTFs Competed'},
    {'number': 'BSc','label': 'Graduating Nov 2026'},
]

# ── Journey timeline (facts only; add entries as they become real) ──
TIMELINE = [
    {
        'period': 'Now',
        'title': 'Freelance Developer — Bambastack Limited',
        'org': 'Majengo platform',
        'desc': 'Freelance development on the Majengo platform, running alongside the final months of my degree.',
        'kind': 'now',
    },
    {
        'period': '2026',
        'title': 'BSc Computer Science',
        'org': 'Graduating November 2026',
        'desc': 'Coursework complete — dissertation built an LSTM-powered multi-user trading platform end to end.',
        'kind': 'education',
    },
    {
        'period': 'Focus',
        'title': 'Offensive Security & CTFs',
        'org': 'Self-directed',
        'desc': 'Red-team tooling (Kali, Burp, Metasploit) and capture-the-flag competitions — three CTFs competed so far.',
        'kind': 'security',
    },
    {
        'period': 'Focus',
        'title': 'AI-Driven Trading Systems',
        'org': 'Self-directed',
        'desc': 'From LSTM signal research to a live Binance-connected execution bot with backtesting and risk controls.',
        'kind': 'ai',
    },
]

# ── Areas currently being explored (from the About page) ──
LEARNING = [
    'Advanced Red Teaming',
    'Autonomous AI Agents',
    'Network Protocol Analysis',
    'Blockchain & DeFi Security',
]


def get_project(project_id):
    """Return a single project dict by id, or None."""
    return next((p for p in PROJECTS if p['id'] == project_id), None)


def related_projects(project, limit=2):
    """Projects sharing the most categories with `project` (excluding itself)."""
    scored = sorted(
        (p for p in PROJECTS if p['id'] != project['id']),
        key=lambda p: len(set(p['categories']) & set(project['categories'])),
        reverse=True,
    )
    return scored[:limit]
