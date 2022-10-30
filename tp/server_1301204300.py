from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

server = SimpleJSONRPCServer(('localhost', 5000))

class Voting:

    def __init__(self):
        self.vote_dict = {"FIFA 23": 0, "PES 2023": 0, "Valorant": 0, "Overwatch 2": 0, "Minecraft": 0}
    
    def add_candidate(self, name):
        self.vote_dict[name] = 0

    def vote(self, idx): 
        name = list(self.vote_dict)[idx-1]
        self.vote_dict[name] += 1

    def show_candidates(self): 
        return self.vote_dict
        
        

# iseng coba inheritance
class Voting_2(Voting): 
    pass

vote = Voting_2() # instansiasi objek

# register fungsi sama procedure
server.register_function(vote.add_candidate)
server.register_function(vote.show_candidates)
server.register_function(vote.vote)

server.serve_forever() # server dijalankan