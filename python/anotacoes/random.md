# Random

[Generate Random Data with Python](https://realpython.com/python-random/)

**PRNG** - pseudorandom number generator

**TRNG** - true random number generator

**CSPRNG** - cryptographically secure PRNG

```python
    import random

    random.seed(444)

    random.random()         # -> [0.0, 1.0) [fechado, aberto)
    random.randint(0, 100)  # -> [0, 100] # número inteiro entre o intervalo fechado
    random.randrange(1,10)  # -> [1, 10) # [fechado, aberto)
    random.uniform(20,30)   # -> float [x,y] # continuous uniform distribution

    items = ['one', 'two', 'three', 'four', 'five']
    # choose sample with replacement
    random.choice(items)    # duplicates are possible
    # -----------S------------
    random.choices(items, k=2) # notice the 'S' in choices

    # without replacement
    random.sample(items, 4)

    # randomize a sequence
    random.shuffle(items)
```

### Generating a sequence of unique random strings of uniform length

```python
import string

def unique_strings(k: int, ntokens: int,
               pool: str=string.ascii_letters) -> set:
    """Generate a set of unique string tokens.

    k: Length of each token
    ntokens: Number of tokens
    pool: Iterable of characters to choose from

    For a highly optimized version:
    https://stackoverflow.com/a/48421303/7954504
    """

    seen = set()

    # An optimization for tightly-bound loops:
    # Bind these methods outside of a loop
    join = ''.join
    add = seen.add

    while len(seen) < ntokens:
        token = join(random.choices(pool, k=k))
        add(token)
    return seen

unique_strings(k=4, ntokens=5)
unique_strings(5, 4, string.printable)
```

### PRNGs for Arrays: numpy.random

```python
    import numpy as np
    np.random.seed(444)
    np.set_printoptions(precision=2)  # Output decimal fmt.

    # Return samples from the standard normal distribution
    # each data point is independent of the others
    np.random.randn(5) # return a np.array with 5 elements

    np.random.randn(5,6) # return a np.array with shape (5,6)

    # `p` is the probability of choosing each element
    np.random.choice([0, 1], p=[0.6, 0.4], size=(5,4))

    # NumPy's `randint` is [inclusive, exclusive), unlike `random.randint()`

    np.random.choice([True, False]) # slow way

    np.random.randint(0, 2, size=25, dtype=np.uint8).view(bool) # more faster way # and complicated
```

### Generating correlated data

Numpy's multivariate_normal function takes a covariance matrix into account.

    cov(X, Y) = corr(X, Y) * [std_x, std_y]

But the calculation is 

C = diag(S) . P . diag(S)

where S is a standard deviation matrix and P is correlation matrix

```python
def corr2cov(p: np.ndarray, s: np.ndarray) -> np.ndarray:
    """Covariance matrix from correlation & standard deviations"""
    d = np.diag(s)
    return d @ p @ d
```

O que significa isso @ ?

```python
>>> # Start with a correlation matrix and standard deviations.
>>> # -0.40 is the correlation between A and B, and the correlation
>>> # of a variable with itself is 1.0.
>>> corr = np.array([[1., -0.40],
...                  [-0.40, 1.]])

>>> # Standard deviations/means of A and B, respectively
>>> stdev = np.array([6., 1.])
>>> mean = np.array([2., 0.5])
>>> cov = corr2cov(corr, stdev)

>>> # `size` is the length of time series for 2d data
>>> # (500 months, days, and so on).
>>> data = np.random.multivariate_normal(mean=mean, cov=cov, size=500)
>>> data[:10]
array([[ 0.58,  1.87],
       [-7.31,  0.74],
       [-6.24,  0.33],
       [-0.77,  1.19],
       [ 1.71,  0.7 ],
       [-3.33,  1.57],
       [-1.13,  1.23],
       [-6.58,  1.81],
       [-0.82, -0.34],
       [-2.32,  1.1 ]])
>>> data.shape
(500, 2)
```

Check the inputs

```python
>>> np.corrcoef(data, rowvar=False)
array([[ 1.  , -0.39],
       [-0.39,  1.  ]])

>>> data.std(axis=0)
array([5.96, 1.01])

>>> data.mean(axis=0)
array([2.13, 0.49])

```

## CSPRNGs in Python

``os.urandom`` usede by modules ``secrete`` and ``uuid``

- Unix Operating system use special file at ``/dev/urandom``
- Windows used C++ function ``CryptGenRandom()``

```python
x = os.urandom(numBytes)  # number of bytes to return

x.hex() # give a string representation of hexadeximal number

type(x), len(x)
```

```python
binary = [f'{i:0>8b}' for i in range(256)]
binary[:16]

binary = [bin(i) for i in range(256)]

bites = bytes(range(256))
```

[Bites to int](https://github.com/realpython/materials/blob/master/random-data/bytes_to_int.py)

### SECRETS module

```python
import secrets

n = 16

# Generate secure tokens
secrets.token_bytes(n)

secrets.token_hex(n)

secrets.token_urlsafe(n)

# Secure version of 'random.choice()'
secrets.choice('rain')
```

### Shortly.py

```python
# shortly.py

from secrets import token_urlsafe

DATABASE = {}

def shorten(url: str, nbytes: int=5) -> str:
    ext = token_urlsafe(nbytes=nbytes)
    if ext in DATABASE:
        return shorten(url, nbytes=nbytes)
    else:
        DATABASE.update({ext: url})
        return f'short.ly/{ext}
```

```python
urls = (
    'https://realpython.com/',
    'https://docs.python.org/3/howto/regex.html'
)

for u in urls:
    print(shorten(u))

DATABASE # print
```

## [Universally Unique IDentifier UUID](https://tools.ietf.org/html/rfc4122.html)

```python
import uuid

uuid.uuid4()

tok = uuid.uuid4()

tok.bytes

len(tok.bytes)

len(tok.bytes) * 8

tok.hex

tok.int
```

- uuid1() -> take machine's host ID and current time by default. "guaranteed uniqueness across time"

- uuid3() and uuid5() -> namespace identifier and a name. Use MD5 or SHA-1

### SystemRandom

```python
# timed.py

import random
import timeit

# The "default" random is actually an instance of `random.Random()`.
# The CSPRNG version uses `SystemRandom()` and `os.urandom()` in turn.
_sysrand = random.SystemRandom()

def prng() -> None:
    random.randint(0, 95)

def csprng() -> None:
    _sysrand.randint(0, 95)

setup = 'import random; from __main__ import prng, csprng'

if __name__ == '__main__':
    print('Best of 3 trials with 1,000,000 loops per trial:')

    for f in ('prng()', 'csprng()'):
        best = min(timeit.repeat(f, setup=setup))
        print('\t{:8s} {:0.2f} seconds total time.'.format(f, best))

```