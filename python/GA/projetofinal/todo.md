# To do list

## Main tasks

### PSO

[x] Implementar um versão básica do **PSO**
    [x] Implementar uma classe *Particle*
    [x] Implementar uma classe SearchSpace para representar o espaço de busca
[x] Implementar estratégia de atualização da velocidade
    [x] Baseado em *Design Patterns Stratagy*
    [x] Estratégia *default* da literatura
    [x] Baseado em redução linear do parâmetro w
[x] Implementar estratégia para atualização da posição da particula
    [x] Atualização *default* encontrada na literatura
    [x] Baseado na média da velocidade da particula: essa classe também ficará responsável por calcular a média e o desvio médio da velocidade das particulas
[x] Decidir/ Implementar a forma como estes strategies serão alternados: no construtor do *SearchSpace* será passado um parâmetro para o tipo de estratégia que será adotado; o método *setup* instancia o tipo de estratégia de acordo com estes parâmetros; o método *setup* é chamado no inicializador do objeto.
[] Decidir quais informações serão interessantes para analisar o log das simulações
[] Implementar um modo de medir o tempo de execução das buscas

## Refactoring

[] Limitar a posição das partículas para o espaço de busca definido: responsabilidade do SearchSpace
[x] Passar as funções de benchmark para um arquivo em separado
[x] SearchSpace será responsável por atualizar a posição e velocidade das partículas e decidirá qual estratégia **utilizar**
[x] Calcular a velocidade média e desvio médio (de acordo com o artigo) na classe de atualização pela média das velocidades