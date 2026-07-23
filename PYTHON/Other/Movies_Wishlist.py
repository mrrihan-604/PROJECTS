# Movies Wishlist
movies_wishlist=["AVTAR","SALAR","D D L J","THE MONKEY KING"]
print("---------R K MOVIES----------")

def Wish_List():
    i=0
    print("----------------------------")
    print("   Your Wishlist...")
    for movies in movies_wishlist:
        print(f"* {movies}")
        i+=1
    if len(movies_wishlist) == 0:
        print("No Movies In Wishlist")
    print(f"You Have {i} Movies In Wishlist")


def Add_Wishlist():
    print("Enter Movie Names To Add \nType EXIT On The End")
    movie="Enter"
    while movie != "EXIT":
        if movie not in movies_wishlist or movie != "EXIT":
            movies_wishlist.append(movie)
            if "Enter" in movies_wishlist:
                movies_wishlist.remove("Enter")
        movie=input(">")

def Remove_Wishlist():
    print("Enter Movie Names To Remove \nType EXIT On The End")
    movie="Enter"
    while movie != "EXIT":
        if movie in movies_wishlist:
            movies_wishlist.remove(movie)
        movie=input(">")


def Clear_Wishlist():
    movies_wishlist.clear()


while True:
    print(">>>   Whats Your Chocie  <<<")
    print("----------------------------")
    print("> 1 : Show My Movies Wishlist ")
    print("> 2 : Add Movies To Wishlist")
    print("> 3 : Remove Movie From Wishlist")
    print("> 4 : Clear Entire Wishlist")
    print("> 5 : Leave Page")
    print("----------------------------")
    choice=int(input(">>>"))
    if choice == 1: Wish_List()
    elif choice == 2: Add_Wishlist()
    elif choice == 3: Remove_Wishlist()
    elif choice == 4: Clear_Wishlist()
    elif choice == 5: break
    else : print("Wrong Choice Enter Again")