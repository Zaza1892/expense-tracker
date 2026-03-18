expenses = [] #store user inputs

try :
  with open ("expenses.txt","r") as file:
    for line in file:
      name,amount=line.strip().split(",")
      expenses.append({"name":name,"amount":float(amount)})
except FileNotFoundError:
  pass 

def add_expense(expenses):

  name=input("Enter an expense: ") # ask user for an input 
 
  amount=float(input("Amount: "))  #this asks the user for an amount 
  
  expense={"name":name,"amount":amount}  # the element added by user 
  print(expenses) # print the full list 
  expenses.append(expense) # add the element to the list 



def show_expenses(expenses):
    
   print("\n Your expenses: ") # prints expenses on a new line
   for i ,expense in enumerate(expenses,start=1): # look at the elements in the list and print out the elements with a corresponding number , starting from 1 
    print(f"{i}.{expense['name']} - {expense['amount']}") # print the expenses name  and amount 


def show_total(expenses):

   print("show total") 

   total=0 # initialise total 
   for expense in expenses: #loop through list elements
    total+=expense["amount"] # increment total 

   print(f"\nTotal spent:{total}") # print overall total 

def del_expense(expenses):
  print("\n Your expenses: ")
  
  for i ,expense in enumerate(expenses,start=1):
     print(f"{i}.{expense['name']}-{expense['amount']}")
     
  delete_arr=int(input("Enter expense to delete: ")) # if choice is 5 display all elements from list and prompt user to choose one to delete

  expenses.pop(delete_arr-1) # use pop function to remove item in list 

  print("Expense deleted ")

while True : # until the user types 4 the program will keep running 
 
 print("Expense tracker: ")
 print("1. Add expense")
 print("2. View expenses")
 print("3. Show total")
 print("4. Exit")
 print("5. Delete expense")

 choice =input("Choose an option: ") # ask user to choose an option 

 if choice=="1":
   add_expense(expenses)

 

 elif choice =="2":

  show_expenses(expenses)


 elif choice=="3":
  show_total(expenses)

 elif choice=="4":
   print("Goodbye")
   break # if choice is 4 end program 
 

 elif choice=="5":
    del_expense(expenses)

 else:
   print("invalid choice")
  





with open("expenses.txt","w") as file : #open text file 
    for expense in expenses:
      file.write(f"{expense['name']},{expense['amount']}\n") # write data to txt file