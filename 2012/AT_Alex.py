import sys

current_savings = float(sys.stdin.readline().strip())
years_till_retirement = int(sys.stdin.readline().strip())
investment_perc = float(sys.stdin.readline().strip()) / 100

monthly_income = []

for i in range(0, years_till_retirement):
    str_input = sys.stdin.readline().strip().split()
    monthly_income.append([float(str_input[0]), float(str_input[1])])

property_tax_perc = float(sys.stdin.readline().strip())
property_reg_fee_perc = float(sys.stdin.readline().strip())

num_condos = int(sys.stdin.readline().strip())
for i in range(0, num_condos):