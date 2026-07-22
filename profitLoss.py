actual_cost=float(input("please enter the actual product price:"))
selling_cost=float(input("please enter selling price:"))

if(selling_cost>actual_cost):
    amount=selling_cost-actual_cost
    print("total profit= {0}", format(amount) )

else:
    print("No profit.")