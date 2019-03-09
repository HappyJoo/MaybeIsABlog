#6.00.1 week2 problem set 2 problem 2 
#Paying debt off in a tear
#2019.3.9 Cost me 1.5 hours...

balance = float(input('balance:'))
annualInterestRate = float(input('air:'))

initbalance = balance
monthlyInterestRate = annualInterestRate / 12
monthlyPayment = 0

while balance > 0:
    for i in range(12):
        balance = (balance - monthlyPayment) * ( 1 + monthlyInterestRate)
    if balance > 0 :
        monthlyPayment += 10
        balance = initbalance
    if balance <= 0:
        break
print("Lowest Payment:", monthlyPayment)
