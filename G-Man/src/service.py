from src import conf as constants


class PowerService:

    POWER = 200
    TURN_POWER  = 5
    MOVE_POWER = 10
    ONE_VALUE = 1
    

    def __init__(self, source):
        self.no_moves = 0
        self.no_turn = 0
        self.curr_x = source.x
        self.curr_y = source.y
        self.curr_dir = source.dir


    def calculate_no_moves(self, destination):

        self.no_moves = abs(self.curr_x - destination.x) + abs(self.curr_y - destination.y)
        
    def turn_in_x_direction(self, destination):

        if self.curr_dir == constants.NORTH or self.curr_dir == constants.SOUTH:
            if self.curr_x != destination.x:
                self.no_turn += self.ONE_VALUE
            elif self.curr_y != destination.y:
                self.no_turn += self.ONE_VALUE

    def turn_in_y_direction(self, destination):

        if self.curr_dir == constants.EAST or self.curr_dir == constants.WEST:
            if self.curr_y != destination.y:
                self.no_turn += self.ONE_VALUE
            elif self.curr_x != destination.x:
                self.no_turn += self.ONE_VALUE

    def calculate_no_turns(self, destination):

        self.turn_in_x_direction(destination)
        self.turn_in_y_direction(destination)

    def calculate_remaining_power(self):

        total_power_lost_by_moves = self.MOVE_POWER * self.no_moves
        total_power_lost_by_turns = (self.TURN_POWER * (self.no_turn + self.ONE_VALUE))
        
        total_power_lost = total_power_lost_by_moves + total_power_lost_by_turns
        return self.POWER - total_power_lost

    def calculate(self, destination):

        self.calculate_no_moves(destination)
        self.calculate_no_turns(destination)
        return self.calculate_remaining_power()