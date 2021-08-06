Email = input("Enetr your email:")
a = Email.index("@")
username = Email[0:a]
domain_name = Email[a+1:]
print(f"your username is: {username} and your domain is: {domain_name}")