class Krabby_patty_dna:
    # 建構式
    def __init__(self, bread_color, meet):
        self.bread_color = bread_color 
        self.meet = meet 
    # 方法(Method)
    def print_burger(self):
        print(f"漢堡皮顏色{self.bread_color} 漢堡肉{self.meet}")


red_krabby_patty = Krabby_patty_dna(bread_color = '紅色', meet = '蟹肉')
red_krabby_patty.print_burger()

yellow_krabby_patty = Krabby_patty_dna(bread_color = '黃色', meet = '蟹肉')
yellow_krabby_patty.print_burger()



