from selling_strats.selling_strategy_base import SellingStrategyBase
from constants import API


class TrailingStop(SellingStrategyBase):
    def __init__(self, trail_percent=5):
        super().__init__()
        self.trail_percent = trail_percent

    def update(self, position):
        if position.sell_order:
            return
        position.sell_order = API.submit_order(
            symbol=position.stock.data["symbol"],
            qty=position.qty,
            side="sell",
            type="trailing_stop",
            trail_price=self.get_percent_conversion(position),
            time_in_force="day",
        )

    def get_percent_conversion(self, position):
        return str(position.entry_price * (self.trail_percent / 100))
