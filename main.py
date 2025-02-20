# TASK: Create a high score tracker that keeps the top 5 scores.

# Define a function that takes a list of scores and a new score
def get_score(score_list:str, new_score:str):
# Append the new score to the list
    score_list.append(new_score)
# Sort the list in descending order
    score_list.sort(reverse=True)
# Keep only the top 5 scores
    return score_list[:5]
# Return the updated list
# Start with an empty high scores list
high_scores=[]
# Use a loop to let the user enter scores until they type -1
while True:
    new_score=int(input("enter the score, or enter -1 to stop "))
    if new_score==-1:
        break
    else:
       high_scores=get_score(high_scores,new_score)
# Call the function with each new score and display the updated top 5 scores
print (high_scores)