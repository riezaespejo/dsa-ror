

def print_menu4():
    print("********************************")
    print("*           1.Play             *")
    print("*           2.How to Play      *")
    print("*           3.Back             *")
    print("********************************")

print_menu4()
option=input("Make a choice||...")
if option == "1":
    
    from stack import create_game
    
elif option == "2":
    print("4 in a row RULES:")
    
    print("\nChoice the number and press enter over the row you wish to drop your piece in.")
    
    print("\nThe first player that can connect four pieces vertically or horizontally will get the points \n")
  

elif option == "3":
  from menu import print_menu1
