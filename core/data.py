# core/data.py
# ─────────────────────────────────────────────────────────────
# Central data file. Update this to change portfolio content.
# No database needed — Django templates loop over these dicts.
# ─────────────────────────────────────────────────────────────

PROJECTS = [
    {
        'id': 'trading-assistant',
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
        'github': 'https://github.com/RasMatoh/Crypto-trading-bot',   # update
        'demo': '',
        'featured': True,
    },
    {
        'id': 'threat-detection',
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
        'github': 'https://github.com/martinkiruna/threat-detection',    # update
        'demo': '',
        'featured': True,
    },
    {
        'id': 'binance-bot',
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
        'github': 'https://github.com/martinkiruna/binance-bot',          # update
        'demo': '',
        'featured': True,
    },
    {
        'id': 'loan-expert-system',
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
    },
    {
        'id': 'movie-booking',
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
        'github': 'https://github.com/martinkiruna/movie-booking',        # update
        'demo': '',
        'featured': False,
    },
]

SKILLS = {
    'Security': ['Kali Linux', 'Nmap', 'Wireshark', 'Metasploit', 'Burp Suite', 'CTF / Red Team'],
    'AI / ML':  ['Python', 'LSTM / TensorFlow', 'Scikit-learn', 'Pandas', 'NumPy', 'Prolog'],
    'Backend':  ['Django', 'FastAPI', 'PostgreSQL', 'REST APIs', 'WebSockets'],
    'Frontend': ['HTML', 'CSS', 'JavaScript', 'Django Templates'],
    'Tools':    ['Git', 'GitHub', 'Linux', 'VS Code', 'Postman'],
}

STATS = [
    {'number': '5+', 'label': 'Major Projects'},
    {'number': '3',  'label': 'CTFs Competed'},
    {'number': '4th','label': 'Year CS'},
]