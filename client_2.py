import jsonrpclib

server = jsonrpclib.Server('http://127.0.0.1:8008')

print(
'''
1. show candidates
2. add a new candidate
3. vote for a candidate
'''
)

n = int(input("choose your option: "))

while n != '-': 
    if n == 1: 
        print("candidates: ")
        for key, val in server.show_candidates().items(): 
            print(key, val)

    elif n == 2: 
        name = input("insert a name: ") 
        server.add_candidate(name)

    elif n == 3: 
        for key, _ in server.show_candidates().items(): 
            print(key)

        name = input("pick a candidate: ") 
        server.vote(name)

    n = int(input("choose your option: "))