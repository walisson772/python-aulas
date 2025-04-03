def count_semana(semanas):
    DIAS = 7
    return semanas * DIAS;

semanas = int(input("Digite a quantidade de semanas: "))
print(count_semana(semanas))