from statistics import mean

"""Return average of three numbers program """
def average():
    score1 = int(input("Input score1:"))
    score2 = int(input("Input score2:"))
    score3 = int(input("Input score3:"))
    num_avg = mean([score2, score2, score3])
    average_score = num_avg
    return average_score

def get_fname():
    return (input("Please enter your first name:")).capitalize()

def get_lname():
    return (input("Please enter your last name:")).capitalize()


if __name__ == '__main__':
   #
   first_name = get_fname()
       #str.capitalize(input("Please enter your first name:"))
   last_name = get_lname()
   age = int(input("Please enter your age:"))
average_score = str(round(average(),2))
print(f'{last_name}, {first_name}, age: {age}, average grade: {average_score}')

#can also add a negative number
#average of negative numbers is calculated accurately
#when adding string for age python gives an error
