
rabbit = dict()

input = 444

rabbit["adult"] = input
rabbit["teen"] = 0
rabbit["baby"] = 0

for i in range(0,365,15):
    if i % 30 == 0 and i != 0:
        rabbit["baby"] = int(rabbit["baby"] * 0.75)
        rabbit["teen"] = int(rabbit["teen"] * 0.75)
        rabbit["adult"] = int(rabbit["adult"] * 0.75)
    temp_teen = rabbit["teen"]
    rabbit["teen"] = rabbit["baby"]
    rabbit["baby"] = int(rabbit["adult"] * 0.9)
    rabbit["adult"] += int(temp_teen * 0.7)

print str(rabbit["baby"] + rabbit["teen"] + rabbit["adult"])

