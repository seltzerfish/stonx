from datetime import datetime


def market_closing_soon():
    return (
        int(datetime.utcnow().strftime("%H")) == 21
        and int(datetime.utcnow().strftime("%M")) >= 50
    )
