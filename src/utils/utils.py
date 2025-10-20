from datetime import datetime


def get_today_str() -> str:
    """Get current date in a human-readable format."""
    now = datetime.now()
    return now.strftime(f"%a %b {now.day}, %Y")