from datetime import datetime


# returns true if the market will close within 10 minutes
def market_closing_soon():
    return (
        int(datetime.utcnow().strftime("%H")) == 20
        and int(datetime.utcnow().strftime("%M")) >= 50
    )
