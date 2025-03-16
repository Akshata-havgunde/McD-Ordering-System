import time
print("Hello, Welcome to McDonald's...!")
time.sleep(2)
print("--"*60)
print("Welcome to McDonald's – your safety and satisfaction are our top priorities.")
print("Browse our menu and let us know what delicious treat you'd like to order today!")
print("--"*60)

time.sleep(2)
food_items={1:"Burger",2:"Beverages",3:"Chicken & Sandwiches",4:"Breakfast",5:"Desserts & Shakes",6:"Happy Meal",7:"McCafe Drinks",8:"Snacks & Sides",0:"Exit"}
order_list=[]
add_more='y'
bill=0
order=0
while add_more=='y':
    for key, value in food_items.items():
        print("Enter", key, " for ", value)
    print("--" * 60)
    # time.sleep(2)
    def ordr():
        global order_list,bill,order
        order = int(input("Please type what you would like to taste...!--->"))

        print("--" * 60)
        if order==0:
            print('Thank you...!')
            print("--" * 60)
            print("Your order contains:")
            for i in order_list:
                print(i)
            print("--" * 60)
            print("Your total order amount is:", bill)
            print("--" * 60)
            return
        elif order in food_items:

            if order == 1:
                brgr={1:"Big Mac",2:"McDouble",3:"Cheeseburger",4:"Double Cheeseburger",5:"Hamburger",6:"Go Back"}
                brgr1={1:99,2:199,3:149,4:199,5:249,6:0}
                for key, value in brgr.items():
                    print("Enter", key, " for ", value)
                print("--" * 60)
                def brg():
                    global order_list,bill
                    o = int(input("Please type what you would like to taste...!--->"))
                    print("--" * 60)
                    if o not in brgr:
                        print("Please enter the correct input:")
                        brg()
                    elif brgr[o]=="Go Back":
                        pass
                    elif o in brgr:
                        order_list += [brgr[o]]
                        bill += brgr1[o]
                        return
                    # else:
                    #     print("Please enter the correct input:")
                    #     brg()
                brg()

                # for key in range(0,len(brgr)):
                # if o in brgr:
                #     order_list+=[brgr[o]]
                #     bill+=brgr1[o]


            elif order == 2:
                bvrgs = {1: "Coca-Cola", 2: "Sprite", 3: "Fanta", 4: "Dr Pepper", 5: "Diet Coke", 6: "Chocolate Shake",
                         7: "Vanilla Shake", 8: "Starberry Shake", 9: "Hot Chocolate", 10: "Iced Tea", 11: "Water",12:"Go Back"}
                bvrgs1 = {1: 99, 2: 99, 3: 79, 4: 109, 5: 129, 6: 149, 7: 149, 8: 179, 9: 99, 10: 69, 11: 30, 12:0}
                for key, value in bvrgs.items():
                    print("Enter", key, " for ", value)
                print("--" * 60)
                def bvr():
                    global order_list, bill
                    o = int(input("Please type what you would like to taste...!--->"))
                    print("--" * 60)
                    if o not in bvrgs:
                        print("Please enter the correct input:")
                        bvr()
                    elif bvrgs[o]=="Go Back":
                        pass
                    elif o in bvrgs:
                        order_list+=[bvrgs[o]]
                        bill+=bvrgs1[o]

                bvr()
                # add_more = input('Do you want to add more items on your table, press y/n--->')
                # if add_more=="N" or 'n':
                #     break


            elif order == 3:
                c_s = {1: "Crispy Chiken Sandwich", 2: "Spicy CCS", 3: "Deluxe CCS", 4: "Piece Chicken McNuggets",
                       5: "McChicken", 6: "Fliet-O-Fish",7:"Go Back"}
                c_s1 = {1: 149, 2: 199, 3: 249, 4: 399, 5: 149, 6: 99,7:0}
                for key, value in c_s.items():
                    print("Enter", key, " for ", value)
                print("--" * 60)
                def cs():
                    global order_list,bill
                    o = int(input("Please type what you would like to taste...!--->"))
                    print("--" * 60)
                    if o not in c_s:
                        print("Please enter the correct input:")
                        cs()
                    elif c_s[o]=="Go Back":
                        pass
                    elif o in c_s:
                        order_list += [c_s[o]]
                        bill += c_s1[o]
                        return

                cs()

            elif order == 4:
                breakfast = {1: "Egg McMuffin", 2: "Sausage McMuffin", 3: "Sausage McGriddles", 4: "Big Breakfast",
                             5: "Hotcakes", 6: "Sausage Buritto", 7:"Go Back"}
                breakfast1 = {1: 99, 2: 119, 3: 149, 4: 199, 5: 89, 6: 99,7:0}
                for key, value in breakfast.items():
                    print("Enter", key, " for ", value)
                print("--" * 60)
                def bf():
                    global order_list,bill
                    o = int(input("Please type what you would like to taste...!--->"))
                    print("--" * 60)
                    if o not in breakfast:
                        print("Please enter the correct input:")
                        bf()
                    elif breakfast[o]=="Go Back":
                        pass
                    elif o in breakfast:
                        order_list += [breakfast[o]]
                        bill += breakfast1[o]
                        return

                bf()



            elif order == 5:
                d_s = {1: "Hot Fudge Sundae", 2: "McFlurry with M&m's Candies", 3: "Kiddie Cone", 4: "Hot Caramel Sundae",
                       5: "McFlurry with OREO Cookies", 6: "Choclate Shake", 7: "Vanilla Shake", 8: "Strawberry Shake",9:"Go Back"}
                d_s1 = {1: 99, 2: 119, 3: 149, 4: 199, 5: 89, 6: 99, 7: 149, 8: 149, 9: 0}
                for key, value in d_s.items():

                    print("Enter", key, " for ", value)
                print("--" * 60)

                def ds():
                    global order_list, bill
                    o = int(input("Please type what you would like to taste...!--->"))
                    print("--" * 60)
                    if o not in d_s:
                        print("Please enter the correct input:")
                        ds()
                    elif d_s[o]=="Go Back":
                        pass
                    elif o in d_s:
                        order_list += [d_s[o]]
                        bill += d_s1[o]
                        return


                ds()


            elif order == 6:
                h_m = {1: "Hamburger Happy Meal", 2: "4 Piece Chicken McNuggets Happy Meal",
                       3: "6 Piece Chicken McNuggets Happy Meal",4:"Go Back"}
                h_m1 = {1: 149, 2: 249, 3: 299,4:0}
                for key, value in h_m.items():
                    print("Enter", key, " for ", value)
                print("--" * 60)

                def hm():
                    global order_list, bill
                    o = int(input("Please type what you would like to taste...!--->"))
                    print("--" * 60)
                    if o not in h_m:
                        print("Please enter the correct input:")
                        hm()
                    elif h_m[o]=="Go Back":
                        pass
                    elif o in h_m:
                        order_list += [h_m[o]]
                        bill += h_m1[o]
                        return


                hm()

            elif order == 7:
                Mc_Drinks = {1: "Hot Chocolate", 2: "Cappucino", 3: "Mocha", 4: "Latte", 5: "Iced Coffee",
                             6: "Starberry Banana Smoothie", 7: "Premium Roast Coffee",8:"Go Back"}
                Mc_Drinks1 = {1: 149, 2: 199, 3: 129, 4: 119, 5: 89, 6: 199, 7: 199,8:0}
                for key, value in Mc_Drinks.items():
                    print("Enter", key, " for ", value)
                print("--" * 60)

                def mcd():
                    global order_list, bill
                    o = int(input("Please type what you would like to taste...!--->"))
                    print("--" * 60)
                    if o not in Mc_Drinks:
                        print("Please enter the correct input:")
                        mcd()
                    elif Mc_Drinks[o]=="Go Back":
                        pass
                    elif o in Mc_Drinks:
                        order_list += [Mc_Drinks[o]]
                        bill += Mc_Drinks1[o]
                        return

                mcd()

            elif order == 8:
                snacks = {1: "French Fries", 2: "Apple Slides", 3: "Pink Lemonade Slushie", 4: "Blue Raspberry Slushie",
                          5: "Fruit Slushie",6:"Go Back"}
                snacks1 = {1: 89, 2: 99, 3: 99, 4: 119, 5: 119,6:0}
                for key, value in snacks.items():
                    print("Enter", key, " for ", value)
                print("--" * 60)

                def snac():
                    global order_list, bill
                    o = int(input("Please type what you would like to taste...!--->"))
                    print("--" * 60)
                    if o not in snacks:
                        print("Please enter the correct input:")
                        snac()
                    elif snacks[o]=="Go Back":
                        pass
                    elif o in snacks:
                        order_list += [snacks[o]]
                        bill += snacks1[o]
                        return

                snac()

        else:
            print("Please enter the correct input:")
            ordr()
    ordr()


    def am():  # doubt
        global add_more
        if order==0:
            add_more='n'
            return

        add_more = input('Do you want to add more items on your table, press y/n--->')
        print("--" * 60)
        if add_more == 'y':
            pass
        elif add_more == 'n':
          print('Thank you, your order is placed...')
            print("--" * 60)
            print("Your order contains:")
            for i in order_list:
                print(i)
            print("--" * 60)
            print("Your total order amount is:", bill)
            print("--" * 60)
        else:
            print("Please provide correct input")
            print("--" * 60)
            am()
    am()


# print(bill)
# print(order_list)
