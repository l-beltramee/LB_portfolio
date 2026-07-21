# Jogo da Velha
## Como Jogar

1. O tabuleiro será exibido com números de 1 a 9 representando cada posição
2. Digite o número da posição onde quer colocar seu X
3. O computador fará sua jogada automaticamente
4. O jogo continua até alguém vencer ou dar um empate

### Posições do Tabuleiro
```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

## Como Executar

### Requisitos
- Python 3.x instalado no seu computador

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/l-beltramee/LB_portfolio.git
```

2. Navegue até a pasta do jogo:
```bash
cd LB_portfolio/Jogos
```

3. Execute o jogo:
```bash
python jogo_da_velha.py
```

## Exemplo de Jogo

```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Digite onde quer colocar: 5
[1, 2, 3]
[4, 'X', 6]
[7, 8, 9]

(Computador joga...)
```

## Status

- Computador joga aleatoriamente
- Verificação de vitória (linhas, colunas e diagonais)
- Detecção de empate

## Melhorias Futuras

- IA mais inteligente para o computador
- Interface gráfica
- Placar de pontuação

## Autor

Criado por Luccas Beltrame
