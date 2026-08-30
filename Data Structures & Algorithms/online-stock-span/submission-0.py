class StockSpanner:
    # 100 80 60 70
    def __init__(self):
        self.st = []
        self.count = 0

    def next(self, price: int) -> int:

        self.count += 1
        
        while self.st and price >= self.st[-1][0]:
            self.st.pop()
        
        self.st.append((price, self.count))

        if len(self.st) == 1:
            return self.count
        
        return self.st[-1][1] - self.st[-2][1]



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)