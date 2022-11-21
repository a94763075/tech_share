class Krabby_patty_dna:
    # 建構式
    def __init__(self, bread_color, meet):
        self.bread_color = bread_color 
        self.meet = meet 
    # 方法(Method)
    def print_burger(self):
        print(f"漢堡皮顏色{self.bread_color} 漢堡肉{self.meet}")

    def set_status_raw(self):
        self.status = 1

    def set_status_cooked(self):
        self.status = 2

    def set_status_rot(self):
        self.status = 3