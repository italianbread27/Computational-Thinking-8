slider_points = 0
glover_points = 0
neither_points = 0

answer1 = input("Do you prefer A going outside and sliding, B staying inside gloving or  C play sport ")
if answer1 == "A":
    slider_points += 1
elif answer1 == "B":
     glover_points += 1
elif answer1 == "C":
    neither_points += 1

answer2 = input("Do you prefer A showering, B no shower ")
if answer2 == "A":
     neither_points+= 1
elif answer2 == "B":
    glover_points += 1
    slider_points += 1
   
answer3 = input("Do you prefer A regular lights, B led lights or C no lights ")
if answer3 == "A":
     neither_points += 1
elif answer3 == "B":
    glover_points += 1
elif answer3 == "C":
    slider_points += 1

answer4 = input("Do you prefer A hanging with family, B hanging out over discord call ")
if answer4 == "A":
     neither_points += 1
elif answer4 == "B":
    glover_points += 1
    slider_points += 1

answer5 = input("Do you prefer A reddit or B tiktok or C discord ")
if answer5 == "B":
     neither_points += 1
elif answer5 == "C":
    glover_points += 1
elif answer5 == "A":
    slider_points += 1

if glover_points >= slider_points and glover_points >= neither_points:
    print("you are a natural glover")

if slider_points >= glover_points and slider_points >= neither_points:
    print("you are a natural slider!")

if neither_points >= slider_points and neither_points >= glover_points:
    print("Yove dissapointed me, your not a glover or a slider. what will i ever do with you.")



