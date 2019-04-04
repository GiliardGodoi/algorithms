# JSON

Função básica: converter dicionários em strings no formato Json e vice e versa.

## Importação e Uso básico

```python
import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
```

### Dump

```python
import json
json.dump(obj, fp, *,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    indent=None,
    separators=None,
    default=None,
    sort_keys=False, **kw
)
```

### Dumps

```python
import json
json.dumps(obj, *,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    indent=None,
    separators=None,
    default=None,
    sort_keys=False, **kw
)
```

### Load

```python
import json
json.load(fp, *,
    cls=None,
    object_hook=None,
    parse_float=None,
    parse_int=None,
    parse_constant=None,
    object_pairs_hook=None, **kw
 )
```

### Loads

```python
import json
json.loads(s, *,
    encoding=None, 
    cls=None, 
    object_hook=None,
    parse_float=None,
    parse_int=None,
    parse_constant=None,
    object_pairs_hook=None,
    **kw
)
```

## Encoders and Decoder