from .data import PROFILE, STATS


def site_profile(request):
    """Expose site-wide identity + stats to every template."""
    return {
        'profile': PROFILE,
        'stats': STATS,
    }
