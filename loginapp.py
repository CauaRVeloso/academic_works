login_usuario = input("Qual é o seu login?: ")

usuario = ["cauã", "felipe", "isadora", "carlos", "caio", "pedro", "ana"]
senha = [ 51234, 54321, 29313, 93413, 32145, 89271, 27813]

while True:
    if login_usuario in usuario:
        senha_usuario = int(input("Qual é a sua senha?: "))
        if senha_usuario in senha:
            break
    else:
        print("Seu usuário não consta na nossa base de dados!")
        login_usuario = input("Qual é seu login?: ")

print(f'Seja bem vindo a sua conta {login_usuario}!')
