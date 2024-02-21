import copy
import random

class Hat:
    
    #Creates the hat object and populates a list with the string of each ball collor
    def __init__(self, ** hats):
        self.contents = list()
        self.removed_balls = list()
        temp = ''

        #Generating a big string with all the colors v times
        for k, v in hats.items():
            temp += f"{k} "*v
        
        #Spliting the string and assigning to the hat
        for color in temp.split():
            self.contents.append(color)

    #Randomicaly removes strings from the object's 
    #list of contents and put in the removed list
    def draw(self, number_of_balls):
        
        #Giving all the balls
        if number_of_balls >= len(self.contents):
            return self.contents

        #Picking random balls
        for i in range(0, number_of_balls):
            size = len(self.contents)
            position = random.randint(0, size - 1)
            removed_ball = self.contents.pop(position)
            self.removed_balls.append(removed_ball)
        return self.removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    hat_clone = copy.deepcopy(hat)
    expected_balls_list = list()
    temp = ''
    picked_balls = list()

    for k, v in expected_balls.items():
        temp += f"{k} "*v
            
    for color in temp.split():
        expected_balls_list.append(color)

    match = 0
    
    for i in range(0, num_experiments):
        picked_balls = hat_clone.draw(num_balls_drawn)

        if expected_balls_list in picked_balls:
            match += 1

    return match/num_experiments


random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

