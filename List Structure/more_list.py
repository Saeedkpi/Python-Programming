rangpur_division = ["Dinajpur", "Nilphamari", "Rangpur", "Kurigram", "Lalmonirhat", "Gaibandha", "Panchagarh", "Thakurgaon"]

print(rangpur_division)

district = input("Enter the name of the District: ")

if district in rangpur_division:
    print(district, "is a member of Rangpur Division")
else:
    print(district, "is not a member of Rangpur Division")

print("Program Terminated")