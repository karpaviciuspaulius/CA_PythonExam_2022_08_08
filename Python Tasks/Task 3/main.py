# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}


def showObjectKeys(obj):
    values = []
    for i in obj:
        values.append(obj[i])
    return values


print(showObjectKeys(audi))
