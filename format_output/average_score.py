def average(avgNum):
    return (avgNum)


if __name__ == '__main__':
    last_name = str(input("Enter last name:"))
    first_name = str(input("Enter first name:"))
    score1 = float(int(input("Enter score1:")))
    score2 = float(int(input("Enter score2:")))
    score3 = float(int(input("Enter score3:")))
    avgNum = (score1 + score2 + score3)/3
    average_scores = avgNum
    print(("Hello, {first_name} {last_name} this is {1:3f}.") \
            .format(first_name=first_name, last_name=last_name,  \
                   average_scores=average_scores))