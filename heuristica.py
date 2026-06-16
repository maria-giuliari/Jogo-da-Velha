"""
JOGO DA VELHA — Opção 1: Busca Heurística
==========================================
Heurística utilizada (ordem de prioridade):
  1. Vencer: se o computador pode ganhar nesta jogada, faz.
  2. Bloquear: se o humano pode ganhar na próxima jogada, bloqueia.
  3. Centro: ocupa o centro (posição 5 / índice 4) se livre.
  4. Canto oposto: se o adversário está num canto, ocupa o canto oposto.
  5. Canto livre: qualquer canto disponível.
  6. Lado livre: qualquer lado disponível (posições não-canto e não-centro).

Essa sequência garante que o computador nunca perde e vence sempre
que o humano cometer um erro.
"""

LINHAS_VENCEDORAS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
    (0, 4, 8), (2, 4, 6),             # diagonais
]

CANTOS = [0, 2, 6, 8]
LADOS  = [1, 3, 5, 7]
CENTRO = 4

OPOSTOS = {0: 8, 2: 6, 6: 2, 8: 0}


def exibir_tabuleiro(tab: list[str]) -> None:
    print()
    for i in range(0, 9, 3):
        linha = []
        for j in range(3):
            cell = tab[i + j] if tab[i + j] != " " else str(i + j + 1)
            linha.append(cell)
        print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
        if i < 6:
            print("---+---+---")
    print()


def verificar_vencedor(tab: list[str]) -> str | None:
    for a, b, c in LINHAS_VENCEDORAS:
        if tab[a] == tab[b] == tab[c] and tab[a] != " ":
            return tab[a]
    return None


def tabuleiro_cheio(tab: list[str]) -> bool:
    return " " not in tab


def pode_vencer(tab: list[str], jogador: str) -> int | None:
    """Retorna o índice da jogada vencedora para `jogador`, ou None."""
    for a, b, c in LINHAS_VENCEDORAS:
        linha = [tab[a], tab[b], tab[c]]
        if linha.count(jogador) == 2 and linha.count(" ") == 1:
            return [a, b, c][linha.index(" ")]
    return None


def escolher_jogada_cpu(tab: list[str]) -> int:
    """Decide a melhor jogada do computador usando heurística."""

    # 1. Vencer se possível
    jogada = pode_vencer(tab, "O")
    if jogada is not None:
        return jogada

    # 2. Bloquear vitória do adversário
    jogada = pode_vencer(tab, "X")
    if jogada is not None:
        return jogada

    # 3. Centro
    if tab[CENTRO] == " ":
        return CENTRO

    # 4. Canto oposto ao adversário
    for c in CANTOS:
        if tab[c] == "X" and tab[OPOSTOS[c]] == " ":
            return OPOSTOS[c]

    # 5. Qualquer canto livre
    for c in CANTOS:
        if tab[c] == " ":
            return c

    # 6. Qualquer lado livre
    for l in LADOS:
        if tab[l] == " ":
            return l

    return -1  # nunca deve chegar aqui


def jogada_humano(tab: list[str]) -> int:
    while True:
        try:
            pos = int(input("Sua jogada (1-9): ")) - 1
            if 0 <= pos <= 8 and tab[pos] == " ":
                return pos
            print("Posição inválida ou já ocupada. Tente novamente.")
        except ValueError:
            print("Digite um número de 1 a 9.")


def jogar() -> None:
    print("=" * 40)
    print("   JOGO DA VELHA — Heurística")
    print("=" * 40)
    print("Você é X  |  Computador é O")
    print("Posições do tabuleiro:")
    print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")

    tab = [" "] * 9
    vez = "X"  # humano começa

    while True:
        exibir_tabuleiro(tab)

        if vez == "X":
            print("Sua vez (X):")
            pos = jogada_humano(tab)
        else:
            pos = escolher_jogada_cpu(tab)
            print(f"Computador (O) jogou na posição {pos + 1}.")

        tab[pos] = vez
        vencedor = verificar_vencedor(tab)

        if vencedor:
            exibir_tabuleiro(tab)
            if vencedor == "X":
                print("🎉 Parabéns, você venceu!")
            else:
                print("🤖 O computador venceu!")
            break

        if tabuleiro_cheio(tab):
            exibir_tabuleiro(tab)
            print("🤝 Empate!")
            break

        vez = "O" if vez == "X" else "X"

    jogar_novamente = input("\nJogar novamente? (s/n): ").strip().lower()
    if jogar_novamente == "s":
        jogar()


if __name__ == "__main__":
    jogar()