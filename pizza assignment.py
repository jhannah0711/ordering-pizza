#Author :Hannah Jinhee Jeong
#Date   :June 3rd, 2020
#Purpose:ordering pizza program by own

#function for printing toppoings that customer chose
def print_toppings_list(list_name):
    for i in range (1,len(list_name),2):
        if list_name[i]=="1":
            print(list_name[i-1], "olive(s)", end=(""))
        elif list_name[i]=="2":
            print(list_name[i-1], "mushroom(s)", end=(""))
        elif list_name[i]=="3":
            print(list_name[i-1], "green paper(s)", end=(""))
        elif list_name[i]=="4":
            print(list_name[i-1], "hot papper(s)", end=(""))
        elif list_name[i]=="5":
            print(list_name[i-1], "onion(s)", end=(""))
        elif list_name[i]=="6":
            print(list_name[i-1], "pineapple(s)", end=(""))
        elif list_name[i]=="7":
            print(list_name[i-1], "anchovy(s)", end=(""))
        elif list_name[i]=="8":
            print(list_name[i-1], "ham", end=(""))
        elif list_name[i]=="9":
            print(list_name[i-1], "sausage", end=(""))
        elif list_name[i]=="10":
            print(list_name[i-1], "pepperoni", end=(""))
        elif list_name[i]=="11":
            print(list_name[i-1], "bacon(s)", end=(""))

        #varify to place , or and between the toppings. 
        if len(list_name)==i+3:
            print(" and", end=(" "))
        elif len(list_name)!=i+1:
            print(",", end=(" "))

#function for input validation exept for the number of pizza
def input_validation (input_value, comparision):
    if comparision=="num":
        while not input_value.isnumeric() or input_value=="0":
            input_value=input("\nInvalid input! You have to input number over 0."
                              "\nPlease try again: ")
    else:
        while input_value!=comparision:
            for i in range (len(comparision)):
                if input_value==comparision[i]:
                    return input_value
            print("\nInvalid input! You have to input",comparision)
            input_value=input("Please try again: ")
    return input_value

# all variables
#list: list_pizza, list_each_pizza, list_toppings
#input: size, topping, change, change_type, how_many_topping, how_many_pizza,
#       another_pizza, delivery
#price: price_size, price_topping, price_all_pizza, price_topping_total, 
#       price_total, price_discount, price_final, hst, price_without_tax
#comparision: comparision_y_n, comparision_size, comaprision_topping,
#             comparision_change_type
#else: pizza_num, totalnum_pizza

list_pizza=[]
pizza_num=0
another_pizza="y"
totalnum_toppings=0
price_all_pizza=0
comparision_y_n=["y","Y","yes","Yes","n","N","no","No"]

print ("Welcome to Pizza Land!")
#loop for ordering another pizza
while another_pizza!="n" and another_pizza!="N":
    list_each_pizza=[]
    change_type="all"
    change="yes"
    while change=="yes" or change=="Yes" or change=="y" or change=="Y":

        if change_type=="size" or change_type=="all":
            size=input("\nHere are the prices for our pizzas\n\n"
                       "Small - $6.95\n"
                       "Medium - &8.49\n"
                       "Large - $10.29\n"
                       "X-large - $13.49\n\n"
                       "What size pizza would you like? (S/M/L/XL)? ")

            comparision_size=["s", "S", "small", "Small",
                              "m", "M", "medium", "Medium",
                              "l", "L", "large", "Large",
                              "xl", "XL", "Xl", "x-l", "X-L",
                              "x-large", "X-Large", "X-large"]
    
            size=input_validation(size,comparision_size)
            
            if size == "s" or size == "S" or size == "small" or size == "Small":
                size="small"
                price_size=6.95
                price_topping=1.25
                print ("\nEach topping is $"+str(price_topping))
                
            elif size == "m" or size == "M" or size == "medium" or size == "Medium":
                size="medium"
                price_size=8.49
                price_topping=1.50
                print ("\nEach topping is $"+str(price_topping))
                
            elif size == "l" or size == "L" or size == "large" or size == "Large":
                size="large"
                price_size=10.29
                price_topping=1.75
                print ("\nEach topping is $"+str(price_topping))
                
            else:
                size="x-large"
                price_size=13.49
                price_topping=2.00
                print ("\nEach topping is $"+str(price_topping))

            price_topping_total = price_topping*totalnum_toppings

        if change_type=="topping" or change_type=="all":
            topping=input("\nHere are your choices for toppings.\n\n"
                          "Type 12 when you are finished entering the toppings\n"
                          "1. Olives\n"
                          "2. Mushrooms\n"
                          "3. Green Peppers\n"
                          "4. Hot Peppers\n"
                          "5. Onions\n"
                          "6. Pineapple\n"
                          "7. Anchovies\n"
                          "8. Ham\n"
                          "9. Sausage\n"
                          "10. Pepperoni\n"
                          "11. bacons\n"
                          "12. No (more) toppings please!\n\n"
                          "Please choose a toppings please! ")

            comparision_topping=["1","2","3","4","5","6","7","8","9","10","11","12"]
            list_toppings=[]
            totalnum_toppings=0

            while topping!="12":
                topping=input_validation(topping, comparision_topping)

                if topping!="12":
                    how_many_topping=input("\nHow many do you want? ")
                    how_many_topping=input_validation(how_many_topping, "num")
                    totalnum_toppings = totalnum_toppings+int(how_many_topping)
                    list_toppings.append(how_many_topping)
                    list_toppings.append(topping)
                    topping=input("\nPlease choose a toppings please! ")

            price_topping_total = price_topping*totalnum_toppings
           
        if change_type=="number of pizza" or change_type=="all":
            how_many_pizza=input("\nHow many this pizza do you want? ")
            how_many_pizza=input_validation(how_many_pizza, "num")
            
        price_total = (price_topping_total+price_size)*int(how_many_pizza)

        print()
        print(how_many_pizza, size, "pizza(s) with", end=(" "))
              
        print_toppings_list(list_toppings)
        print(" is/are $"+str(round(price_total,2)))


        #check if customer wants to change order
        change=input("\nDo you want to change your order?(y/n) ")
        change=input_validation(change, comparision_y_n)
        if change=="yes" or change=="Yes" or change=="y" or change=="Y":
            comparision_change_type=["size", "topping", "number of pizza", "all"]
            change_type=input("\nWhich part do you want to change?"
                             "(size/topping/number of pizza/all) ")
            change_type=input_validation(change_type,comparision_change_type)

    another_pizza=input("\nWould you like to order another pizza?(y/n) ")
    another_pizza=input_validation(another_pizza, comparision_y_n)

    list_each_pizza.append(how_many_pizza)
    list_each_pizza.append(size)
    list_each_pizza.append(list_toppings)
    list_each_pizza.append(price_total)
    list_pizza.append(list_each_pizza)
    price_all_pizza=price_all_pizza+price_total

print()

# list_pizza[list_each_pizza[how_many_pizza, size,
#            list_toppings[how_many_topping, topping], price_total]
            
price_without_tax=0
pizza_num=pizza_num+int(how_many_pizza)
price_without_tax=price_without_tax+price_all_pizza

delivery=input("Is this for delivery?(y/n)"
               "\nA delivery charge is $3.50 ")
delivery=input_validation(delivery, comparision_y_n)

print("\nHere is your final bill")
for i in range (len(list_pizza)):
    print(list_pizza[i][0],list_pizza[i][1],"pizza(s) with", end=(" "))
    print_toppings_list(list_pizza[i][2])
    print(": $"+str(round(list_pizza[i][3],2)))

if delivery=="y" or delivery=="Y":
    price_without_tax=price_without_tax+3.50
    print("delivery charge:\t$3.50")
else:
    print("pick-up order")

if pizza_num>=4:
    price_discount=price_without_tax*0.85
    print("volume discout 15%:\t$-"+ str(round(price_without_tax*0.15,2)))
    hst=price_discount*0.13
    price_final=price_discount*1.13

else:
    hst=price_without_tax*0.13
    price_final=price_without_tax*1.13

print("HST:\t\t\t$" + str(round(hst,2)) +
      "\nfinal total:\t\t$" + str(round(price_final,2)))
