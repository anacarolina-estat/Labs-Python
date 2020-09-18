n = int(input("Escolha um numero entre 0 e 49: "))

if n > 49 or n < 0:
    print("Numero invalido.")

lista_palavras = ["perfeitamente", "liberdade", "enfermidade","significado",
                  "outono", "chuva", "ilha","infinito", "solidariedade", "ameixa",
                  "felicidade", "arte", "paternidade","criatividade", "virtude",
                  "guerra","democracia", "teatro", "saudade", "adeus","paz",
                  "honestidade", "horizonte", "sabedoria","sossego", "maternidade",
                  "esperteza","primavera", "coragem", "igualdade","navio", "montanha",
                  "queijo","gentileza", "tempestade", "joalheria","paralelogramo",
                  "melancolia", "trem","inverno", "amizade", "atriz","computador",
                  "borboleta", "aeroporto", "nascimento", "uva", "oceano",
                  "orquestra","melancia"]

print("Palavra: ", end='')

for i in range(len(lista_palavras[n])):
    print("_ ", end='')
