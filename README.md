# Jogo da Velha — IA vs Humano

<p align="center">
    <strong>Atividade de Implementação de Jogo da Velha</strong><br/>
    <strong>Algoritmos Avançados — Católica SC</strong><br/>
  Mariele Vieira e Maria A. Giuliari
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.16-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/HTML-Visualizacao-yellowgreen?logo=pygame" alt="Pygame"/>
</p>

<p align="center">
Implementações de computador jogando jogo da velha: uma usando **busca heurística** e outra usando o **Quadrado Mágico Lo Shu**.
</p>


---

## Arquivos

| Arquivo | Descrição |
|---|---|
| `opcao1_heuristica.py` | Jogo no terminal — IA com heurística |
| `opcao2_loshu.py` | Jogo no terminal — IA com Lo Shu |
| `jogo_da_velha.html` | Interface visual com os dois modos |

---

## Como rodar

**Terminal (Python):**
```bash
python3 opcao1_heuristica.py
# ou
python3 opcao2_loshu.py
```
Não requer nenhuma biblioteca externa — só Python 3.

**Navegador (HTML):**
Abra o arquivo `jogo_da_velha.html` diretamente no navegador. Sem servidor, sem dependências.

---

## Opção 1 — Heurística

O computador segue uma lista de prioridades a cada jogada:

1. **Vencer** — se há dois em linha e o terceiro está livre, completa
2. **Bloquear** — mesma lógica para impedir o adversário
3. **Centro** — ocupa a posição central se disponível
4. **Canto oposto** — se o adversário está num canto, ocupa o canto oposto (evita armadilha de dupla ameaça)
5. **Canto livre** — qualquer canto disponível
6. **Lado livre** — último recurso

Essa ordem garante que o computador **nunca perde**: vence quando o humano erra, e empata quando o humano joga perfeitamente.

---

## Opção 2 — Quadrado Mágico Lo Shu

O Quadrado Mágico Lo Shu é uma matriz 3×3 onde cada número de 1 a 9 aparece uma vez e toda linha, coluna e diagonal soma **15**:

```
2 | 9 | 4
7 | 5 | 3
6 | 1 | 8
```

Cada posição do tabuleiro recebe o valor Lo Shu correspondente. A regra é simples: **três valores do mesmo jogador que somam 15 = vitória** — o que equivale matematicamente a completar uma linha, coluna ou diagonal.

Para decidir a jogada, o computador busca o **complemento para 15** entre os pares de valores que já possui. Se `2 + 9 = 11`, o complemento é `4` — e se a posição com valor `4` estiver livre, é a jogada vencedora (ou de bloqueio, aplicando a mesma lógica ao adversário).

---

## Comparação entre as abordagens

| | Heurística | Lo Shu |
|---|---|---|
| Intuitividade | Alta — espelha o raciocínio humano | Média — exige conhecer o quadrado |
| Detecção de vitória | Lista explícita de 8 combinações | Soma de subconjuntos (sem lista) |
| Lógica central | Regras condicionais em sequência | Aritmética com `combinations` |
| Dificuldade de implementar | Mais fácil | Levemente mais difícil |
| Resultado prático | Invencível | Invencível |

Ambas chegam ao mesmo comportamento — o computador nunca perde. A diferença está na representação: a heurística é mais legível, o Lo Shu é mais elegante matematicamente.
