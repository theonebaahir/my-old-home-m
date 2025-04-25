medical = input("do you have a medical codition Y or N")
s = int(input("enter your attendance"))
if medical == "Y":
    print("allowed")
else: 
    if s >= 75 :
        print("you are allowed")
    else : 
        print("you are not allowed")
# electricity bill activity
units = int(input("enter the number of unts you used or mabye the units that you wasted"))
if units <= 50 :
    amount = units * 2.60
    surcharge = 25
elif units <= 100 :
    amount = units * 3.25
    surcharge = 35
    
elif units <= 200 :
    amount = units * 5.25
    surcharge = 45
    
else :
    units <= 100 
    amount = units * 8.45
    surcharge = 75
    
    
    
    
total = amount + surcharge 
print("electricity bill, ", total)
# is about customize your ride


    
    
    



    