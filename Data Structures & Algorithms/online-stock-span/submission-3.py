class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        days = 1
        while self.st and self.st[-1][0] <= price:
            _, prev_days = self.st.pop()
            days += prev_days
        self.st.append((price, days))
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)