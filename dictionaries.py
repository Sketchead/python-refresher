user_dict = {"username": "atx", "email": "atx@example.com", "age": 26}

print(user_dict["username"])  # Output: atx

user_dict["age"] = 27  # Update the age
print(user_dict)  # Output: {'username': 'atx', 'email': '

del user_dict["email"]  # Remove the email key-value pair
print(user_dict)  # Output: {'username': 'atx', 'age': 27}

for x, y in user_dict.items():
    print(x, y)  # Output: username atx, age 27

user_dict2 = user_dict.copy()  # Create a copy of the dictionary
user_dict2["username"] = "new_user"  # Update the username in the copied
user_dict2.pop("age")
print(user_dict2)  # Output: {'username': 'new_user'}
