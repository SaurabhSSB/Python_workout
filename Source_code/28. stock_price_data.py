stock_prices= { "info": [600, 630, 630], "ril": [1430, 1490 ,1567], "mtl": [234, 180, 160]}
loop_ = "Yes"
while loop_ == "Yes":
    user_input = input("Enter the operation to be performed ( print/ add): ")
    if user_input== "print":
        print (stock_prices)
    else:
        stock_ticker= input("Enter the stock: ")
        if stock_ticker in stock_prices :
            print("The stock is already registered. ")
        else:
            value= int(input("Enter the number of data to be entered: "))
            list_stock_ticker= []
            for i in range(value):
                val= int(input(f"Enter the value of the {i}th data of the stock:- "))
                list_stock_ticker.append(val)
            stock_prices[stock_ticker]= list_stock_ticker
    loop_= input("Do you wish to continue ( Yes/ No): ")