# Program untuk menghitung bilangan faktorial menggunakan rekursi
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Menampilkan output
print(factorial(5))
