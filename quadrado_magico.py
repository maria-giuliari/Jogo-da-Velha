"""
JOGO DA VELHA – Opção 2: Quadrado Mágico Lo Shu 

=================================================
Como a representação foi aplicada:
 
O Quadrado Mágico Lo Shu é uma matriz 3×3 onde cada número de 1 a 9 aparece exatamente uma vez e toda linha, coluna e diagonal soma 15:

    2 | 9 | 4
    7 | 5 | 3
    6 | 1 | 8

Mapeamento posição → valor Lo Shu:
  Posição visual:   Valor Lo Shu:
   1 | 2 | 3         2 | 9 | 4
   4 | 5 | 6   →     7 | 5 | 3
   7 | 8 | 9         6 | 1 | 8
 
Regra vencedora: três valores do mesmo jogador somam exatamente 15. 
(porque toda linha/coluna/diagonal do Lo Shu soma 15)
 
Estratégia do computador:
  1. Vencer: encontrar dois valores próprios cujo complemento para 15
             ainda está disponível → jogar esse complemento.
  2. Bloquear: mesmo raciocínio para os valores do adversário.
  3. Centro (valor 5): posição mais valiosa do Lo Shu.
  4. Canto livre: valores de canto (2,4,6,8) aumentam possibilidades.
  5. Qualquer posição livre.
 
Comparação com a Heurística:
  • A heurística é mais intuitiva de implementar — as regras espelham
    o raciocínio humano ("vencer → bloquear → centro → canto…").
  • O Lo Shu é matematicamente elegante: reduz o problema a somas de
    subconjuntos, sem precisar listar linhas vencedoras explicitamente.
  • Porém o Lo Shu exige entender a codificação numérica e a lógica de
    complemento, tornando-o levemente mais difícil de explicar a quem
    não conhece o quadrado mágico.
  • Ambas as abordagens resultam em um computador invencível quando
    implementadas corretamente.
"""

from intertools import combinations 

# Mapeamento: posição do tabuleiro (0-8) → valor no Lo Shu
LO_SHU = [2, 9, 4,
           7, 5, 3,
           6, 1, 8]
 
# Posição do centro e dos cantos no Lo Shu (por valor)
CENTRO_VALOR = 5
CANTOS_VALORES = {2, 4, 6, 8}
 
# Índice de cada valor Lo Shu → posição no tabuleiro
VALOR_PARA_IDX = {v: i for i, v in enumerate(LO_SHU)}
 
 
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
 
 
def valores_do_jogador(tab: list[str], jogador: str) -> list[int]:
    """Retorna os valores Lo Shu das posições ocupadas pelo jogador."""
    return [LO_SHU[i] for i, v in enumerate(tab) if v == jogador]
 
 
def valores_livres(tab: list[str]) -> list[int]:
    """Retorna os valores Lo Shu das posições livres."""
    return [LO_SHU[i] for i, v in enumerate(tab) if v == " "]
 
 
def jogada_vencedora_loshu(meus_valores: list[int],
                            livres: list[int]) -> int | None:
    """
    Verifica se existe um par de valores próprios cujo complemento
    para 15 está entre as posições livres. Retorna o valor Lo Shu
    da jogada vencedora ou None.
    """
    for a, b in combinations(meus_valores, 2):
        complemento = 15 - a - b
        if 1 <= complemento <= 9 and complemento in livres:
            return complemento
    return None
 
 
def verificar_vencedor(tab: list[str]) -> str | None:
    """Usa o Lo Shu: vencedor é quem tiver 3 valores somando 15."""
    for jogador in ("X", "O"):
        vals = valores_do_jogador(tab, jogador)
        if len(vals) >= 3:
            for trio in combinations(vals, 3):
                if sum(trio) == 15:
                    return jogador
    return None
 
 
def tabuleiro_cheio(tab: list[str]) -> bool:
    return " " not in tab
 
 
def escolher_jogada_cpu(tab: list[str]) -> int:
    """Decide a melhor jogada do computador usando Lo Shu."""
    meus_vals   = valores_do_jogador(tab, "O")
    adv_vals    = valores_do_jogador(tab, "X")
    livres      = valores_livres(tab)
 
    # 1. Vencer
    v = jogada_vencedora_loshu(meus_vals, livres)
    if v:
        return VALOR_PARA_IDX[v]
 
    # 2. Bloquear
    v = jogada_vencedora_loshu(adv_vals, livres)
    if v:
        return VALOR_PARA_IDX[v]
 
    # 3. Centro (valor 5 no Lo Shu)
    if CENTRO_VALOR in livres:
        return VALOR_PARA_IDX[CENTRO_VALOR]
 
    # 4. Canto livre (valores 2, 4, 6, 8)
    for v in livres:
        if v in CANTOS_VALORES:
            return VALOR_PARA_IDX[v]
 
    # 5. Qualquer posição livre
    return VALOR_PARA_IDX[livres[0]]
 
 
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
    print("=" * 42)
    print("   JOGO DA VELHA — Quadrado Mágico Lo Shu")
    print("=" * 42)
    print("Você é X  |  Computador é O")
    print("Posições do tabuleiro:")
    print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")
    print("\nQuadrado Lo Shu (valores internos):")
    print(" 2 | 9 | 4 \n---+---+---\n 7 | 5 | 3 \n---+---+---\n 6 | 1 | 8 ")
 
    tab = [" "] * 9
    vez = "X"
 
    while True:
        exibir_tabuleiro(tab)
 
        if vez == "X":
            print("Sua vez (X):")
            pos = jogada_humano(tab)
        else:
            pos = escolher_jogada_cpu(tab)
            print(f"Computador (O) jogou na posição {pos + 1} "
                  f"(valor Lo Shu: {LO_SHU[pos]}).")
 
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