import jsonrpclib

server = jsonrpclib.Server('http://127.0.0.1:5000')

def menu():
    print(
'''
--------------------------------------------------------------------
-----            you may select one of the menu below.         -----
-----            [1] show candidates and total votes           -----
-----            [2] add a new candidate                       -----
-----            [3] vote for a candidate                      -----
-----            [-] exit                                      -----
--------------------------------------------------------------------
P.S. you may vote more than one time! 
'''
    )

print("-----                   welcome to VOTE DEK!                   -----")
menu()
n = int(input("\nselect your option: "))

while n != '-': 
    if n == 1: 
        print("--------------------------------------------------------------------")
        print("candidates of the best game category: ")
        for i, (k, v) in enumerate(server.show_candidates().items()):
            print(f"{i+1}. {k} {v}")
        print("--------------------------------------------------------------------")

    elif n == 2: 
        print("--------------------------------------------------------------------")
        name = input("your favorite game is not in the list? :(( \nworry not! you may insert a new game candidate! : ") 
        server.add_candidate(name)
        print("--------------------------------------------------------------------")

    elif n == 3: 
        print("--------------------------------------------------------------------")
        for i, (k, v) in enumerate(server.show_candidates().items()):
            print(f"{i+1}. {k} {v}")

        id_ = int(input("your game is losing? vote more for your fav game! : "))
        server.vote(id_)
        print("--------------------------------------------------------------------")

    menu()
    n = int(input("\nselect your option: "))