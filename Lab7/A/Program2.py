def get_sorted(scores): # Bubble Sort
    x = len(scores)
    for i in range(x):
        for v in range(0, x-i-1):
            if scores[v] > scores[v+1]:
                scores[v], scores[v+1] = scores[v+1], scores[v]
    return scores

def get_median(scores):
    sorted_scores = get_sorted(scores)
    length = len(sorted_scores)
    if length % 2 == 1:
        return sorted_scores[length // 2]
    else:
        return (sorted_scores[length // 2 - 1] + sorted_scores[length // 2]) / 2

golfers = []

while True:
    try:
        first_round = int(input("Enter the first round score or enter a negative number to stop: "))
        if first_round < 0:
            break
        second_round = int(input("Enter the second round score: "))
        name = input("Enter the player's name: ")
        golfers.append((name, first_round + second_round))
    except ValueError:
        print("Please enter valid scores.")
    
if golfers:
    scores = [v for i,v in golfers]
    median_score = get_median(scores)
    
    print(f"Median score is: {median_score}")
    print("Players who made the cut:")
    for golfer, score in golfers:
        if score >= median_score:
            print(f"{golfer} with score {score}")
    
    print("\nPlayers who did not make the cut:")
    for golfer, score in golfers:
        if score < median_score:
            print(f"{golfer} with score {score}")
else:
    print("Please enter in valid data to process.")
