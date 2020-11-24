"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    A = int(input("Digite um número inteiro\n"))
    B = int(input("Digite um número inteiro\n"))
    C = float(input("Digite um número real\n"))
    A1 = 2 * A + 0.5 * B
    B1 = 3 * A + C 
    C1 = C ** 3 
    print(f"Valor da opção 1: {A1}.\nValor da opção 2: {B1}.\nValor da opção 3: {C1}.")

if __name__ == '__main__':
    main()
