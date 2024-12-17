# combination methed

n = int(input("Enter the number of teams : "))
r = int(input("Enter the combo : "))

ntotal = 1
for x in range(1,n+1):
    ntotal = ntotal * x
    
n_r = n-r
n_rtotal = 1
for y in range(1,n_r+1):
    n_rtotal = n_rtotal * y
    

rtotal = 1
for z in range(1,r+1):
    rtotal = rtotal * z
    
combos = ntotal / (n_rtotal * rtotal)

print(f"your total combiantions is {int(combos)}")

team_name1 = input("what is your team 1 name : ")
team_name2 = input("what is your team 2 name : ")
team_name3  = input("what is your team 3 name : ")
team_name4 = input("what is your team 4 name : ")
a = 0
# COMBOS OF TEAMS 
# for i in range(0,5):
#     print(i, end=" ")
#     print("VS", end=" ")
#     print(a)
#     a
    
# FINALIST TEAMS SELECTION
# teams inputs
team_score1 = int(input("what is team 1 score: "))
team_point1 = int(input("what is team 1 point: "))

team_score2 = int(input("what is team 2 score: "))
team_point2 = int(input("what is team 2 point: "))

team_score3  = int(input("what is team 3  score: "))
team_point3  = int(input("what is team 3  point: "))

team_score4 = int(input("what is team 4 score: "))
team_point4 = int(input("what is team 4 point: "))

list1 = [team_point1,team_point2,team_point3,team_point4]
max_point1= max(list1)
list1.remove(max_point1)
max_point2= max(list1)

# condition if total points is greater than 6 than program crashed 
total_points = team_point1 + team_point2 + team_point3 + team_point4
if(total_points>6 or total_points<0):
    print("your total points is greater is 6 which is not possible")
    exit()



# condition if match 1 and 2
if(team_point1==team_point2 and team_point1==max_point2):
    if(team_score1>team_score2):
        max_point2 = team_name1
    elif(team_score2>team_score1):
        max_point2 = team_name2
# condition if match 4 and 3
elif(team_point3==team_point4 and team_point3==max_point2):
    if(team_score3>team_score4):
        max_point2 = team_name3
    elif(team_score4>team_score3):
        max_point2 = team_name4
# condition if match 1 and 3
elif(team_point1==team_point3 and team_point1==max_point2):
    if(team_score1>team_score3):
        max_point2 = team_name1
    elif(team_score3>team_score1):
        max_point2 = team_name3
# condition if match 4 and 1
elif(team_point1==team_point4 and team_point4==max_point2):
    if(team_score1>team_score4):
        max_point2 = team_name1
    elif(team_score4>team_score1):
        max_point2 = team_name4
# condition if match 2 and 3
elif(team_point2==team_point3 and team_point2==max_point2):
    if(team_score2>team_score3):
        max_point2 = team_name2
    elif(team_score3>team_score2):
        max_point2 = team_name3
# condition if match 2 and 4
elif(team_point2==team_point4 and team_point4==max_point2):
    if(team_score2>team_score4):
        max_point2 = team_name2
    elif(team_score4>team_score2):
        max_point2 = team_name4

if(max_point1==team_point1):
        max_point1=team_name1

elif(max_point1==team_point2):
        max_point1=team_name2

elif(max_point1==team_point3):
        max_point1=team_name3

elif(max_point1==team_point4):
        max_point1=team_name4

if(max_point2==team_point1):
        max_point2=team_name1

elif(max_point2==team_point2):
        max_point2=team_name2

elif(max_point2==team_point3):
        max_point2=team_name3

elif(max_point2==team_point4):
        max_point2=team_name4
# final print
print(f"{max_point1} and {max_point2} are in final")
