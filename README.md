<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/slicedict.svg?maxAge=3600)](https://pypi.org/project/slicedict/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/slicedict.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/slicedict.py/actions)

### Installation
```bash
$ [sudo] pip install slicedict
```

#### Examples
```python
>>> import slicedict

>>> medatata = dict(name="pkgname", version="1.0.0", somekey="value")
>>> slicedict.slice(medatata, ["name", "version"])
{'version': '1.0.0', 'name': 'pkgname'}
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>