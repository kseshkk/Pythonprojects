from participant import Participant
from captain import Captain
from decorators import log_action

class Tournament:
    _participants = list[Participant]

    def __init__(self):
        self._participants = []

    def has_participants(self):
        if not self._participants:
            print("Участников пока нет")
            return False
        return True

    def add_participant(self, participant: Participant):
        self._participants.append(participant)

    def show_participants(self):
        if not self.has_participants():
            return
    
        for i in range(len(self._participants)):
            print(f"{i+1}. {self._participants[i]}")
        
    def find_participant(self, name: str):
        for participant in self._participants:
            if participant._name.lower() == name.lower():
                return participant
        return None
    
    # @log_action
    def add_points_to_participant(self, name: str, points: int):
        participant = self.find_participant(name)
        if participant:
            participant.add_points(points)
        else:
            print("Участник не найден")

            
    # @log_action
    def remove_points_from_participant(self, name: str, points: int):
        participant = self.find_participant(name)
        if participant:
            participant.remove_points(points)  
            return participant._score
        return None


    def sort_by_rating(self):
        self._participants.sort(key=lambda x: x._score, reverse=True)

    def show_rating(self):
        if not self.has_participants(): 
            return
        
        self.sort_by_rating()
        for i in range(len(self._participants)):
            print(f"{i+1}. {self._participants[i]._name} — {self._participants[i]._score} баллов")   


    def get_winner(self):
        if not self.has_participants(): 
            return 

        return max(self._participants, key=lambda x: x._score)
    
    def show_debug_info(self):
        if not self.has_participants():
            return None

        for participant in self._participants:
            print(participant.__dict__)

    def __len__(self):
        return len(self._participants)
    

    def get_participant_score(self, name: str):
        participant = self.find_participant(name)
        return participant._score

    def remove_participant(self, name: str):
        participant = self.find_participant(name)
        if participant:
            self._participants.remove(participant)
            print(f"Участник {name} удалён")
        else:
            print("Такого участника нет")
