# Anotações sobre métodos em string

## Indexing ans Slice

s[:]

s[start: end : step]

s[::-1] reverte um string

## Operadores

foo + bar

foo * 5

'z' in 'abc'
'z' not in 'xyz'

## Built-in functions

- chr() converte um inteiro em caracter
- ord() converte um caracter em um inteiro
- len()
- str()

## Interpolação

n = 5, m = 4

prod = n * m

f'The product of {n} and {m} is {prod}'


## Case conversion

- foo.capitalize()
- foo.lower()
- foo.upper()
- foo.swapcase()
- foo.title()

# Find and Replace

s.count(<sub> [, <start>[, <end>]])

s.endswith(<suffix> [, <start>[, <end>]]) 

s.startswith(<prefix> [, <start>[, <end>]])

s.find(<sub> [, <start>[, <end>]])

s.rfind(<sub> [, <start>[, <end>]])

s.index(<sub> [, <start>[, <end>]])

s.rindex(<sub> [, <start>[, <end>]])

## Classification

s.isalnum() # is alphanumeric ?

s.isalpha()

s.isdigit()

s.isidentifier() # is a valid python identifier ?

s.islower()

s.isupper()

s.isprintable()

s.isspace() # \n \t \r

s.istitle()

## Formatting

s.center(<width>[, <fill>])

s.expandtabs(tabsize=8) # replace \t by white space

s.ljust(<width>[, <fill>])

s.lstrip([<chars>])

s.rjust(<width>[, <fill>])

s.rstrip([<chars>])

s.zfill(<width>) # pads a string on the left with zeros

s.replace(<old>, <new>[, <count>])

s.strip([<chars>])

## Converting between string and iterables

s.join(<iterable>)
    ', '.join(['foo', 'bar', 'baz', 'qux'])
    ':'.join('corge') # results 'c:o:r:g:e'

s.partition(<separator>) # divides a string based on a separator. Retorna uma tupla

s.split(sep=',', maxsplit=-1) # splits a string into a list of substring

s.rsplit(sep='.', maxsplit=-1)

s.splitlines([keepends]) # | True or 1

## Bytes Object

b = b'foo bar baz'

type(b)

bytes(<string>, <encoding>)

b = bytes('foo.bar', 'utf8)

bytes(<size>)

## References

Real Python: [Strings and Characters Data in Python](https://realpython.com/python-strings/) Acessado em <18/07/2018>