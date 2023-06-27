Principle=float(input("Enter Principle:"))
Rate=float(input("Enter Rate:"))
Time=float(input("Enter Time:"))
Amount=Principle*(1+Rate/100)**Time
C_I=Amount-Principle
print("The compound Interest is", C_I)