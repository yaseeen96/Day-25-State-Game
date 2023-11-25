import turtle
from game_manager import GameManager

screen = turtle.Screen()

screen.title("Indian States Game")
image = "blank_states_img.gif"
game_title = "Guess the State"


screen.addshape(image)
turtle.shape(image)
screen.setup(width=420, height=500)

manager = GameManager()


game_is_on = True


while game_is_on:
    answer = screen.textinput(title=game_title, prompt="What's another state's name?")

    # check answer
    if manager.check_answer(answer):
        manager.write_state(answer)
    game_title = f"{manager.score} / {manager.total_states} correct"

    # condition to complete game
    if manager.score == manager.total_states:
        game_is_on = False

    if answer == "exit":
        manager.generate_csv()
        break

    


