# class Activity
# action = "jumping"
# construcor
# printInfo
class Activity:
    def __init__(self, action):
        self.action = action

class Sportsman(Activity):

    def __init__(self, sport_id, sport_name, action): 
        self.sport_id = sport_id 
        self.sport_name = sport_name 
        super().__init__(action)
 
    def printinfo(self): 
        print(self.sport_id, self.sport_name, self.action) 
 
    def set_type(self, sport_type): 
        self.sport_type = sport_type 
 
    def get_type(self): 
        return self.sport_type 
 


class Teamsport(Sportsman): 

    def __init__(self, num_players, sport_id, sport_name, action): 
        super(  ).__init__(sport_id, sport_name, action) 
        self.num_players = num_players 
 
    def printinfo(self): 
        super().printinfo() 
        print(self.num_players) 
 
class Football(Teamsport): 
    def __init__(self, num_players, sport_id, sport_name, team_name, action): 
        super().__init__(num_players, sport_id, sport_name, action) 
        self.team_name = team_name 
     
    def printinfo(self): 
        super().printinfo() 
        print(self.team_name) 
 


foot = Football(2, "basketball", 5, "Generation of Miracles", "Jumping") 
foot.printinfo() 
foot.set_type("Indoor") 
print(foot.get_type())