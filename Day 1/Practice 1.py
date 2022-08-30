Hours = input("Enter Start~End Hours (00~24) :")
Days = int(input("Enter Days:"))
Rate = int(input("Enter Rate:"))

Hour = int(Hours.split("~")[1]) - int(Hours.split("~")[0])

Week_Pay = Hour * Rate * Days

print("Your Pay is", Week_Pay,"Won.")
