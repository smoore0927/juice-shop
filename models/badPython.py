import json

user_input = input("Enter text here")
query = "Select * FROM users WHERE username = '" + user_input + "';"
execute_query(query) #Exploitable