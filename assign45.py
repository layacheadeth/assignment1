class user:
    def store():
        id=int(input("id: "))
        name=str(input("name: "))
        age=int(input("age: "))
class invoice(user):
    pass
    def order_shipping():
        items=[]
        amounts=[]
        prices=[]
        totals=[]
        n = int(input("n: "))
        for j in range (n):
            item=str(input("item: "))
            amount=int(input("amounts: "))
            price=float(input("price: "))
            total=amount*price
            items.append(item)
            amounts.append(amount)
            prices.append(price)
            totals.append(total)
        print("items: ", items)
        print("amount: ", amounts)
        print("price: ", prices)
        print("total: ", totals)
invoice.customer()
invoice.order_shipping()
