user_names = ["Cynthia", "James", "John", "Peter", "Luke", "Mary", "Maria",
              "Jane", "Paul", "Simon", "Andrew", "Solo", "Lucy"]
user_name = input("Enter Username:").lower()
if user_name in user_names:
    print("Access Granted")
else:
    print("Access Denied")