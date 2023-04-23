A = input("Valor de A: ")
A = float(A)

B = input("Valor de B: ")
B = float(B)

C = input("Valor de C: ")
C = float(C)

D = input("Valor de D: ")
D = float(D)

if A > B and A > C and A > D:
    print(str(A) + " é o maior número")
elif B > A and B > C and B > D:
    print(str(B) + " é o maior número")
elif C > A and C > B and C > D:
    print(str(C) + " é o maior número")
else:
    print(str(D) + " é o maior número")

if A < B and A < C and A < D:
    print(str(A) + " é o menor número")
elif B < A and B < C and B < D:
    print(str(B) + " é o menor número")
elif C < A and C < B and C < D:
    print(str(C) + " é o menor número")
else:
    print(str(D) + " é o menor número")