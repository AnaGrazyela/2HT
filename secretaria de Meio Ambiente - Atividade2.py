meio_ambiente = float(input("Digite o índice de poluição: --> "))
if meio_ambiente >= 0.05 and meio_ambiente <= 0.25:
    print("Aceitavél!")
elif meio_ambiente > 0.3 and meio_ambiente < 0.4:
    print("1°Grupo tem que suspender as suas atividades!")
elif meio_ambiente > 0.41 and meio_ambiente < 0.5:
    print("1° e 2° Grupo tem que suspender as suas atividades!")
else:
    print("Todos os grupos teram que encerrar suas atividades!")
