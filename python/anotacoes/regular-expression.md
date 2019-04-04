# Expressão regulares

Meta caracteres:
''' . ^ $ * + ? { } [ ] \ | ( ) '''

[ ] define um conjunto de caracteres. Exemplos [abc] [a-c] [0-9]. Metacaracteres dentro de um conjunto são tomados como caracteres normais. Exceção: ^

^ indica negação ou complemento. Por exemplo, [^5] encontra qualquer caracter exceto 5.

\ backslash. Caracter de escape. Pode representar conjuntos predefinidos, quando seguido por uma letra.

\d equivale a [0-9]

\D equivale a [^0-9]

\s equivale a [\t\n\r\f\v]

\S equivale a [^\t\n\r\f\v] white space character

\w equivale a [a-zA-Z0-9_]

\W equivale a [^a-zA-Z0-9_]

Pode ser incluidas dentro de uma classe, por exemplo, [\s,.]

Caracter especial . corresponde qualquer caracter exceto new line \n re.DOTALL

## Repeating Things

\* equivale a 0 (zero) ou mais repetições de uma classe. Equivalente a {0,}

\+ equivale a 1 ou mais repetições. Equivalente a {1,}

? equivale a 0 ou 1 repetições. Equivalente a {0,1}

{m,n} minimo de m, e máximo n repetições

## Compiling Regular Expressions

import re
p = re.compile('ab*')

re.IGNORECASE i

re.GLOBAL g

## Performing Matches

match() -> determina desde o começo da string

search() -> procura em qualquer posição

findall() -> retorna uma lista

finditer() -> retorna um iterator de match object

## Match Object

group() -> retorna a string

start() -> retorna a posição inicial

end() -> retorna a posição final

span() -> retorna uma tupla com a posição inicial e final

Evitar **'The Backslash Plague'** utilizar raw string in python: r'/parttner/'

## Module-Level Functions

re.match()

re.search()

re.findall()

re.sub()

## Modifying Strings

split()

sub()

subn() retorna a nova string e o número de substituições

[REGULAR EXPRESSION How To](https://docs.python.org/3/howto/regex.html#regex-howto)

[Regular Expression module](https://docs.python.org/3/library/re.html)
