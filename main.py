''' GERADOR DE SENHAS

- O usuário pode digitar a própria senha ou pedir uma senha aleatória.
- A senha deve ter no mínimo 8 caracteres.
- Um medidor classifica a senha como: Fraca, Boa ou Forte.'''

import secrets
import string

TAMANHO_MINIMO = 8
SIMBOLOS = "!@#$%&*()-_=+[]{};:,.<>?/"


def avaliar_senha(senha):
    # Dá uma pontuação à senha e retorna (classificação, pontos).
    pontos = 0

    # Pontos pelo tamanho
    if len(senha) >= 8:
        pontos += 1
    if len(senha) >= 12:
        pontos += 1

    # Pontos pela variedade de caracteres
    if any(c in string.ascii_lowercase for c in senha):
        pontos += 1
    if any(c in string.ascii_uppercase for c in senha):
        pontos += 1
    if any(c in string.digits for c in senha):
        pontos += 1
    if any(c in SIMBOLOS for c in senha):
        pontos += 1

    # Classificação final (pontuação máxima = 6)
    if pontos <= 3:
        return "Fraca", pontos
    elif pontos <= 5:
        return "Boa", pontos
    else:
        return "Forte", pontos


def gerar_senha(tamanho=12):
    # Gera uma senha aleatória com letras, números e símbolos.
    if tamanho < TAMANHO_MINIMO:
        tamanho = TAMANHO_MINIMO

    # Garante pelo menos um caractere de cada tipo
    senha = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(SIMBOLOS),
    ]

    # Completa o restante com caracteres de qualquer tipo
    todos = string.ascii_letters + string.digits + SIMBOLOS
    while len(senha) < tamanho:
        senha.append(secrets.choice(todos))

    # Embaralha para a posição dos caracteres não ser previsível
    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)


def mostrar_resultado(senha):
    # Mostra a senha e o resultado do medidor.
    classificacao, pontos = avaliar_senha(senha)
    print(f"\nSua senha: {senha}")
    print(f"Medidor de segurança: {classificacao} ({pontos}/6 pontos)\n")


def criar_senha_propria():
    # Pede ao usuário que digite a senha, exigindo o tamanho mínimo.
    while True:
        senha = input(f"Digite sua senha (mínimo {TAMANHO_MINIMO} caracteres): ")
        if len(senha) >= TAMANHO_MINIMO:
            return senha
        print(f"Senha muito curta! Use pelo menos {TAMANHO_MINIMO} caracteres.")


def criar_senha_aleatoria():
    # Pergunta o tamanho desejado e gera a senha.
    while True:
        entrada = input(f"Tamanho da senha (mínimo {TAMANHO_MINIMO}, padrão 12): ").strip()
        if entrada == "":
            return gerar_senha(12)
        if entrada.isdigit() and int(entrada) >= TAMANHO_MINIMO:
            return gerar_senha(int(entrada))
        print(f"Digite um número válido, igual ou maior que {TAMANHO_MINIMO}.")


def main():
    print("=== Criador de Senha Segura ===")

    while True:
        print("1 - Criar minha própria senha")
        print("2 - Gerar senha aleatória")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrar_resultado(criar_senha_propria())
        elif opcao == "2":
            mostrar_resultado(criar_senha_aleatoria())
        elif opcao == "3":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()