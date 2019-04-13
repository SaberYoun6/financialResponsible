from django.shortcuts import render


from django.http import HttpResponse 

# Create your views here.




def inDex(request):
    HttpReponse("The end of the world as we know it and I feel fine...")
'''    
userBudget = float(input("Please enter how much you have budget " ))

more Expenses = "y"
userTotalExpensses = 0

While moreExpenses =="y"
        userExpense = float(input("Enter an expense:" ) )
        userTotalExpenses += userExpense
        moreExpenses = Input ( "Do you have more expenses?: Type  y" +
                               "for yes, any key for no: " )

print()
 if userTotalExpenses > userBudget
   print("You were over budget of", "$" + format(userBudget, ",.2f"), \
          "by", "$" + format(userTotalExpenses - userBudget,",.2f" ))
elif userBudget > userTotalExpenses:
    print("you were underyour budget of","$" + format(userBudget,"'.2f'")),\
          "by" , "$" + format (userBudget - userTotalExpenses,",.2f") )
else:
    print("You used exactly your budget of",\
            "$" + format(userBudget , ",.2f"),".")
'''
