# Todo list

## Main task

[x] Implementar um versão básica do PSO
    [x] Implementar uma classe Particle
    [x] Implementar uma classe SearchSpace para representar o espaço de busca
[] Implementar utilizando o Design Pattenrs Stratagy as estratégias para atualização da velocidade e posição
    [] Decidir/ Implementar a forma como estes strategies serão alternados
        - Se por parâmetro do tipo texto no construtor de Particle, utilizando um 'switch' em um método builder dentro da classe
        - Se por injeção de dependência: de alguma forma setar uma estratégia dentro da classe no construtor ou por um método set: E se o método setup fosse chamado logo após a chamada o run?
        - E se quem atualizasse a velocidade e a posição fosse a classe SearchSpace, quem também definiria a estratégia a ser utilizada e os parâmetros, vide que o métodos de atualização da posição e velocidade estão já utilizando parâmetros vindos desta classe
[] Decidir quais informações serão interessantes para analisar o log das simulações
[] Implementar um modo de medir o tempo de execução das buscas

## Refactoring

[] Limitar a posição das partículas para o espaço de busca definido
[x] Passar as funções de benchmark para um arquivo em separado
[x] SearchSpace será responsável por atualizar a posição e velocidade das partículas e decidirá qual estratégia utilizar