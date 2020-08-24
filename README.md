# choicelib - choose requirement from list

Simple example:

```python
from choicelib import choice_in_order

json = choice_in_order(["json", "ujson", "hyperjson", "orjson"])
```

```python
json # "json"
```

After installing ujson:

```shell script
pip install ujson
```

```python
json # "ujson"
```
