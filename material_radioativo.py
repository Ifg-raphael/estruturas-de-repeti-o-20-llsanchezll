# Sua solução aqui
massa = float(input('Digite a massa inicial do material radioativo (em gramas): '))
tempo = 0

while massa >= 0.5:
    massa /= 2
    tempo += 50

horas = tempo // 3600
tempo %= 3600
minutos = tempo // 60
segundos = tempo % 60

print(f"{horas}h {minutos}m {segundos}s")