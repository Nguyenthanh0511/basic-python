# # ví dụ 1
# number = int(input("Enter a number: "))
# #if [công việc điều kiện]:
# if number > 10:
#   print("The number is greater than 10.")
# else:
#   print("The number is not greater than 10.")














#ví dụ 2 điều kiện so sánh
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# if number1 > number2:
#   print("The first number is greater than the second number.")
# elif number1 < number2:
#   print("The first number is less than the second number.")
# else:
#   print("The two numbers are equal.")










# Ví dụ 3:Cách sử dụng câu lệnh if-else để thực hiện các hành động khác nhau dựa trên đầu vào của người dùng


# user_input = input("What would you like to do today? ")

# if user_input == "eat":
#   print("Let's go to the restaurant!")
# elif user_input == "watch a movie":
#   print("Let's go to the cinema!")
# elif user_input == "go for a walk":
#   print("Let's go to the park!")
# else:
#   print("I don't know what you want to do.")

#Phát triển bài toán Hành động người dùng
import random

user_input = input("What would you like to do today? ")

if user_input == "eat":
  possible_activities = ["Let's go to the restaurant!", "Let's order takeout!", "Let's cook at home!"]
  activity = random.choice(possible_activities)
  print(activity)
elif user_input == "watch a movie":
  possible_activities = ["Let's go to the cinema!", "Let's watch a movie at home!", "Let's go to a friend's house to watch a movie!"]
  activity = random.choice(possible_activities)
  print(activity)
elif user_input == "go for a walk":
  possible_activities = ["Let's go to the park!", "Let's go for a hike!", "Let's go for a walk around the block!"]
  activity = random.choice(possible_activities)
  print(activity)
else:
  print("I don't know what you want to do.")