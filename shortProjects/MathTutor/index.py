import random, math, time

def math_tutor():
    try:
        num_of_practices = int(input("How many practice question would you like to do? "))
        range_of_num = int(input("How high should the numbers be?"))
    except UnboundLocalError:
        print("That was not a valid number. Try again...")
        return 0
    except ValueError:
        print("That was not a valid number. Try again...")
        return 0
    num_of_corrects = 0

    all_answers = []
    
    start = time.time()
    for q in range(num_of_practices):
        timestamp = time.time()
        
        first_num = math.floor(random.random()*range_of_num + 1)
        second_num = math.floor(random.random()*range_of_num + 1)
        ans = first_num * second_num
        try:
            your_ans = int(input(f"{first_num} * {second_num} = "))
        except ValueError:
            your_ans = -1
        if ans == your_ans:
            num_of_corrects += 1
        q += 1
        end = time.time()
        all_answers.append((f"{first_num} * {second_num} = {ans}", f"{first_num} * {second_num} = {your_ans}", f"{round((end - timestamp),1)}s"))
        

    print("Thanks for playing")
    for question in all_answers:
        if question[0] == question[1]:
            print(f"{question[0]} / time: {question[2]}")
        else:
            print(f"{question[0]} / time: {question[2]} \n {question[1]} (your answer)")
    print(f"You answered {num_of_corrects}/{num_of_practices} questions correctly. That is {round((num_of_corrects/num_of_practices*100), 1)}%. \n You finished within {round((end - start), 1)}s")

math_tutor()