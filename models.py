
class GameFull():
    def __init__(self, data):
        
        self.white_id = data['white']['id']
        self.black_id = data['black']['id']

        self.gameState = GameState(data['state'])

class GameState():
    def __init__(self, data):
        self.moves = data['moves']
        self.wtime = data['wtime']
        self.btime = data['btime']
        self.winc = data['winc']
        self.binc = data['binc']
        self.status = data['status'] # TODO: enum?

        self.move_list = [] if self.moves == "" else self.moves.split(" ")
        
        print("SDFSDFDSFDSFSDFDSFDSF", self.move_list)
        self.num_moves = len(self.move_list)
        self.is_finished = self.status not in {"created", "started"}
        


class ChatLine():
    def __init__(self, data):
        self.username = data['username']
        self.text = data['text']
        self.room = data['room'] # TODO: enum?