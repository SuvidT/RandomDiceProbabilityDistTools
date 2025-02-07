from pprint import pprint
from collections import defaultdict

def diceProbability(numDice, diceType):
    
    outcome_counts = defaultdict(float)
    total_rolls = diceType ** numDice
    
    def roll_dice(dice_left, current_sum):
        if dice_left == 0:
            outcome_counts[current_sum] += 1 / total_rolls  
            return
        for face in range(1, diceType + 1):
            roll_dice(dice_left - 1, current_sum + face)
    
    roll_dice(numDice, 0)
    
    return outcome_counts

pprint(diceProbability(2, 6))
pprint(diceProbability(1, 20))