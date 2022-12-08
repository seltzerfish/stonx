from datetime import datetime


# returns true if the market will close within 10 minutes
def market_closing_soon():
    hour = int(datetime.utcnow().strftime("%H"))
    minute = int(datetime.utcnow().strftime("%M"))

    if hour == 20:
        return True
    if hour == 19 and minute >= 50:
        return True
    return False


def within_market_hours():
    day = int(datetime.utcnow().strftime("%w"))
    hour = int(datetime.utcnow().strftime("%H"))
    minute = int(datetime.utcnow().strftime("%M"))
    if day == 0 or day == 6:
        return False
    if hour > 19:
        return False
    if hour < 13:
        return False
    if hour == 13 and minute < 30:
        return False
    return True
