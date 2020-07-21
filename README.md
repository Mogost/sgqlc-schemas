[![PyPI version](https://badge.fury.io/py/sgqlc-schemas.svg)](https://badge.fury.io/py/sgqlc-schemas)
## About

This package was created so that when using [sgqlc (Simple GraphQL Client)](https://github.com/profusion/sgqlc "sgqlc (Simple GraphQL Client)") you do not need to create schemas for popular APIs.

## How to use

#### Installation

You can install this package either via the Python Package Index (PyPI) or from source.

To install using ``pip``:
```
$ pip install -U sgqlc-schemas
```

#### Import schema and simple query
```python
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from sgqlc_schemas import github_schema

op = Operation(github_schema.query_type)
op.viewer().login()
endpoint = HTTPEndpoint('https://api.github.com/graphql', {'Authorization': f'bearer {token}'})
data = endpoint(op)
```

## Current schemas

- [GitHub](http://github.com "GitHub")
- [Monday.com](http://monday.com "Monday.com")

## Contribution

This package welcomes any new contribution. Please create [pull requests on GitHub](https://github.com/Mogost/sgqlc-schemas/pulls "pull requests on GitHub").
