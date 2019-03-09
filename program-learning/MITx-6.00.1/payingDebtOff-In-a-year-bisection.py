#6.00.1 week2 problem set 2 problem 3
#Paying debt off in a tear using bisection
#2019.3.9 Cost me ? hours...
#I don't actually understand this yet, so if i remember i'll come back later on.

balance = float(input('balance:'))
annualInterestRate = float(input('air:'))

initbalance = balance
monthlyInterestRate = annualInterestRate / 12
lower = balance / 12
upper = (balance * (1 + monthlyInterestRate) ** 12) / 12
epsilon = 0.01
time = 0
while abs(balance) > epsilon:
    time += 1
    monthlyPayment = (upper + lower) / 2
    balance = initbalance
    for i in range(12):
        balance = (balance - monthlyPayment) * ( 1 + monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPayment
    elif balance < -epsilon:
        upper = monthlyPayment
    else:
        break
print(time)
print("Lowest Payment:", round(monthlyPayment, 2))
