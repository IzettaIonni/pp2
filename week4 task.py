class Sportsman:

    def __init__(self, sport_id, sport_name): 
        self.sport_id = sport_id 
        self.sport_name = sport_name 
 
    def printinfo(self): 
        print(self.sport_id, self.sport_name) 
 
    def set_type(self, sport_type): 
        self.sport_type = sport_type 
 
    def get_type(self): 
        return self.sport_type 
 


class Teamsport(Sportsman): 

    def __init__(self, num_players, sport_id, sport_name): 
        super(  ).__init__(sport_id, sport_name) 
        self.num_players = num_players 
 
    def printinfo(self): 
        super().printinfo() 
        print(self.num_players) 
 
class Football(Teamsport): 
    def __init__(self, num_players, sport_id, sport_name, team_name): 
        super().__init__(num_players, sport_id, sport_name) 
        self.team_name = team_name 
     
    def printinfo(self): 
        super().printinfo() 
        print(self.team_name) 
 


foot = Football(2, "basketball", 5, "Generation of Miracles") 
foot.printinfo() 
foot.set_type("Indoor") 
print(foot.get_type())