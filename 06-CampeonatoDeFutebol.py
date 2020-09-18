numTimes = int(input())
jogos = numTimes * (numTimes - 1)
dadosPartidas = []
times = {}

for i in range(jogos):
    dadosPartidas.append(input().split())

for i in range(0, jogos, 2):

    if dadosPartidas[i][0] not in times:
        times[dadosPartidas[i][0]] = [0, 0, 0, 0]

    if dadosPartidas[i][3] not in times:
        times[dadosPartidas[i][3]] = [0, 0, 0, 0]

# pontuação e número de vitórias
for i in range(jogos):

    if dadosPartidas[i][1] > dadosPartidas[i][4]:
        times[dadosPartidas[i][0]][0] += 3
        times[dadosPartidas[i][0]][1] += 1

    elif dadosPartidas[i][1] < dadosPartidas[i][4]:
        times[dadosPartidas[i][3]][0] += 3
        times[dadosPartidas[i][3]][1] += 1

    else:
        times[dadosPartidas[i][0]][0] += 1
        times[dadosPartidas[i][3]][0] += 1

# Saldo de gols:
for i in range(jogos):

    if dadosPartidas[i][1] > dadosPartidas[i][4]:
        times[dadosPartidas[i][0]][2] = times[dadosPartidas[i][0]][2] + int(dadosPartidas[i][1]) - int(
            dadosPartidas[i][4])
        times[dadosPartidas[i][3]][2] = times[dadosPartidas[i][3]][2] - int(dadosPartidas[i][1]) + int(
            dadosPartidas[i][4])

    elif dadosPartidas[i][1] < dadosPartidas[i][4]:
        times[dadosPartidas[i][0]][2] = times[dadosPartidas[i][0]][2] + int(dadosPartidas[i][1]) - int(
            dadosPartidas[i][4])
        times[dadosPartidas[i][3]][2] = times[dadosPartidas[i][3]][2] - int(dadosPartidas[i][1]) + int(
            dadosPartidas[i][4])

# Gols-pró:
for i in range(jogos):
    times[dadosPartidas[i][0]][3] = times[dadosPartidas[i][0]][3] + int(dadosPartidas[i][1])
    times[dadosPartidas[i][3]][3] = times[dadosPartidas[i][3]][3] + int(dadosPartidas[i][4])

for i in sorted(times):
    print(i, ":", times[i])