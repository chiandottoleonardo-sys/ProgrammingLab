def tipo_triangolo(a, b, c):
    if (
        (a > 0 and b > 0 and c > 0)
        and (a + b > c)
        and (a + c > b)
        and (b + c > a)
    ):
        if a == b and b == c:
            return "Il triangolo è EQUILATERO (tutti i lati uguali)."
        elif a == b or b == c or a == c:
            return "Il triangolo è ISOSCELE (due lati uguali)."
        else:
            return "Il triangolo è SCALENO (tutti i lati diversi)."
    else:
        return "Con questi valori NON è possibile formare un triangolo."


a = float(input("Inserire un numero: "))
b = float(input("Inserire un numero: "))
c = float(input("Inserire un numero: "))
risultato = tipo_triangolo(a, b, c)
print(risultato)