from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

server = SimpleJSONRPCServer(('http://127.0.0.1', 8008))

class Voting:

    def __init__(self):
        self.vote_dict = {"bhedil": 1000000, "jansut": 10e4}
    
    def add_candidate(self, name):
        self.vote_dict[name] = 0

    def vote(self, name): 
        self.vote_dict[name] += 1

    def show_candidates(self): 
        lst = {}
        for i, k in self.vote_dict.items():
            lst[i] = k 
        return lst

class Voting_2(Voting): 
    pass

vote = Voting_2() # instansiasi objek

# register fungsi sama procedure
server.register_function(vote.add_candidate)
server.register_function(vote.show_candidates)
server.register_function(vote.vote)

server.serve_forever() # server dijalankan