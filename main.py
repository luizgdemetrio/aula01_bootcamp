"""
1. O programa deve começar solicitando ao usuário que insira seu nome.
2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
"""

nome = input("Digite seu nome aqui: ")
salario = int(input("digite seu salario: "))
bonus = float(input("qual a porcentagem do seu bonus?: "))
calculoKPI = int(1000 + (salario * bonus))
mensagemfinal = print(f"Ola {nome}, o seu valor bonus foi de {calculoKPI}")
