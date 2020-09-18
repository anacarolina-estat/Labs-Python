notas_ac = [float(x) for x in input().split()]
soma = 0
for i in range(len(notas_ac)):
    aux = notas_ac[i]
    soma = soma + aux
    media_notas_ac = soma / len(notas_ac)
print("Media das atividades conceituais:", format(media_notas_ac, ".1f"))


def tupla_float_int(x):
    x = x[1:-1]  # remove parênteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])  # converte primeiro elemento para float
    i = int(x[1])  # converte segundo elemento para int
    return (f, i)  # retorna tupla


notas_lab = [tupla_float_int(x) for x in input().split()]
num2 = 0
dem2 = 0
for i in range(len(notas_lab)):
    num = notas_lab[i][0] * notas_lab[i][1]
    num2 = num2 + num
    dem = notas_lab[i][1]
    dem2 = dem2 + dem
    media_notas_lab = num2 / dem2
print("Media das tarefas de laboratorio:", format(media_notas_lab, ".1f"))

notas_provas = [float(x) for x in input().split()]
media_notas_provas = (2 * notas_provas[0] + 3 * notas_provas[1]) / 5
print("Media das provas:", format(media_notas_provas, ".1f"))

freq = int(input())

if freq >= 75:
    if media_notas_provas >= 5 and media_notas_lab >= 5:
        media_avaliativa = 0.6 * media_notas_provas + 0.3 * media_notas_lab + 0.1 * media_notas_ac
        media_final = max(5, media_avaliativa)
        print("Aprovado(a) por nota e frequencia.")
        print("Media final:", format(media_final, ".1f"))

    elif media_notas_provas < 2.5 or media_notas_lab < 2.5:
        media_final = min(media_notas_provas, media_notas_lab)
        print("Reprovado(a) por nota.")
        print("Media final:", format(media_final, ".1f"))

    else:
        exame = float(input())
        media_final = (min(media_notas_provas, media_notas_lab) + exame) / 2
        print("Nota no exame: ")

else:
    print("Reprovado(a) por frequencia.")
    media_final = min(media_notas_provas, media_notas_lab)
    print("Media final:", format(media_final, ".1f"))
