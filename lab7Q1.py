#Q.1
def average(scores):
    summ = 0
    for score in scores:  
        summ += score
    return summ / len(scores)

def highest(scores):
    return max(scores)

def lowest(scores):
    return min(scores)
scores = [] 
print("Enter the student's scores,if you finish write 'done': ")
while True:
    score = input("Score: ")
    if score == 'done':     
        print("Average:", average(scores))
        print("Highest:", highest(scores))
        print("Lowest:", lowest(scores))
        break
    try:
        scores.append(float(score)) 
    except ValueError:
        print("that's not a number! Please enter a number")

