from turtle import Turtle
import pandas
import numpy as np
# manages game operations
FONT = ("Arial", 10, "bold")
class GameManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.read_csv()
        self.score = 0
        self.total_states = 28
        self.pu()
        self.hideturtle()
        self.correct_answers = []

        
    def check_answer(self,value):
        if value in self.states_list:
            return True
        else:
            return False
        
    def write_state(self, value):
        row = self.data[self.data["state"].str.lower() == value]
        position = (np.float32(row.x)[0],np.float32(row.y)[0])
        print(position)
        print(type(position))
        self.goto(position)
        self.write(row["state"].item())
        self.score += 1
        self.correct_answers.append(row["state"].item())

    
    def read_csv(self):
        self.data = pandas.read_csv("28_states.csv")
        self.states_list = [state.lower() for state in self.data.state.tolist()]

    def generate_csv(self):
        missing_states = [state for state in self.data.state.tolist() if state not in self.correct_answers]
        new_csv = pandas.DataFrame(missing_states)
        new_csv.to_csv("states_to_learn.csv")
        

    
    

    

