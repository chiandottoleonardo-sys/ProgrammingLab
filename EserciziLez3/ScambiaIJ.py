def scambia(A, i, j):
    tpm = 0
    tpm = A[i]
    A[i] = A[j]
    A[j] = tpm


numeri = [20,18,34,56,22]

print("Prima dello scambio:", numeri)

scambia(numeri,0,3)

print("Dopo lo scambio", numeri)
