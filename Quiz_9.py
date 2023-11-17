class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        print(f"{self.name} {quantity}잔의 가격은 {total_price}원 입니다.")

#객체 만들기
Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

# 사용자에게 정보를 입력 받는 과정
selected_beverage = input("주문할 음료를 선택하세요 \n(커피, 녹차, 아이스티)\n-> ")
if selected_beverage == "커피":
    quantity = int(input("수량을 입력하세요\n-> "))
    if quantity > 0:
        coffee.calculate(quantity)
    else:
        print("한 개 이상의 음료를 주문해주세요.")
elif selected_beverage == "녹차":
    quantity = int(input("수량을 입력하세요\n-> "))
    if quantity > 0:
        green_tea.calculate(quantity)
    else:
        print("한 개 이상의 음료를 주문해주세요.")
elif selected_beverage == "아이스티":
    quantity = int(input("수량을 입력하세요: "))
    if quantity > 0:
        ice_tea.calculate(quantity)
    else:
        print("한 개 이상의 음료를 주문해주세요.")
else:
    print("올바른 음료를 선택하세요.")
