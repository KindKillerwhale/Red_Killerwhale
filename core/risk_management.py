class RiskManager:
    def __init__(self):
        pass

    def apply_stop_loss(self, order, stop_loss_price):
        if order['price'] <= stop_loss_price:
            return True
        return False

    def apply_take_profit(self, order, take_profit_price):
        if order['price'] >= take_profit_price:
            return True
        return False
