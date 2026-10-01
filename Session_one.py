# print("Enter your name:")
# name = input()
# print("Your name is " + name)

# 0
# 0.0
# ""
# ''
# []
# {}
# ()
# set()
# None
# False

# +
# -
# *
# /
# //
# **
# %

# print(7 % 5)

# print(8//2)

# print(12/5)

# print(7 + 5)
# print(7 < 5)
# print(7 <= 5)
# print(7 >= 5)
# print(7 == 5)
# print(7 != 5) 


# and
# or
# not


# count = 0
# count += 1 # same as count = count + 1 -> 1
# count *= 5 # same as count = count * 5 -> 5
# "a" in "cat" # True -- membership: is 'a' found inside 'cat'?
# 3 not in [1, 2, 4] # True -- membership on a list
# a = [1, 2, 3]
# b = [1, 2, 3]
# a == b # True -- same VALUES
# a is b # False -- different OBJECTS in memory


# x = "winter"
# if x == "Summer":
#     print("It's summer!")
# elif x == "Winter":
#     print("It's winter!")
# else:
#     print("It's not summer or winter.")
    
# print("This will always print.")

# age = 34
# has_valid_id = True

# if age > 18:
#     if has_valid_id:
#         print("You can enter the club.")
#     else:
#         print("id required to enter the club.")
# else:
#     print("underage, you cannot enter the club.")


# Ternary (Conditional) Expression
# status = "Adult" if age >= 18 else "Minor"
# equivalent to:
# if age >= 18:
    # status = "Adult"
# else:
    # status = "Minor"



# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

# count = 0
# while count < 3:
#     print(count)
#     count += 1
#     # break
#     continue
#     print("This will never print because of the continue statement above.")


for i in range(1,11):
    if i % 2 == 0:
        print(i)
    # if i == 4:
    #     break 