# file_object = open("pi_digits.txt")
# contents = file_object.read()
# print(contents)

# file_object.close()
#-------------
# with open("pi_digits.txt") as file_object:
#     contents = file_object.read()

# print(contents.rstrip())
#--------------
# file_path = 'D:\\KI_5\\Python-PTIT\\python\\pi_digits.txt'

# with open(file_path) as file_object:
#     contents = file_object.read()

# print(contents.rstrip())

#-------------
# file_path = 'D:\\KI_5\\Python-PTIT\\python\\pi_digits.txt'

# with open(file_path) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)


#-----------

# while True:
#     name = input()
#     if name == "quit":
#         break
#     with open("guest.txt", "a") as f:
#         f.write(name + "\n")

# while True:
#     s = input("lý do bạn thích học lập trình: ")
#     if s == "":
#         break
#     with open("responses.txt", "a") as f:
#         f.write(s + "\n")

# ------------
# while True:
#     s = input()
#     if s  == "quit":
#         break
#     try:
#         print(int(s))
#     except ValueError:
#         print("not valid")

# def count(file):
#     try:
#         with open(file) as f:
#             s = f.read()
#         print(len(s.split()))
#     except FileNotFoundError:
#         print(f"{file} khong ton tai")

# file_list = ['guest.txt', 'd.txt']
# for i in file_list:
#     count(i)

#--------------
import json
m = {"hello": 56, "at" : 23 , "test" : 43, "this" : 43}
m = dict(sorted(m.items()))

with open("d.json", "w") as f:
    json.dump(m, f)