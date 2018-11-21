[![](https://img.shields.io/pypi/pyversions/slicedict.svg?longCache=True)](https://pypi.org/pypi/slicedict/)
[![](https://img.shields.io/pypi/v/slicedict.svg?maxAge=3600)](https://pypi.org/pypi/slicedict/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/slicedict.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/slicedict.py/)

#### Install
```bash
$ [sudo] pip install slicedict
```

#### Functions
function|description
-|-
`slicedict.slice(d, keys)`|return dictionary with given keys

#### Examples
```python
>>> import slicedict

>>> medatata = dict(name="pkgname", version="1.0.0", somekey="value")
>>> slicedict.slice(medatata, ["name", "version"])
{'version': '1.0.0', 'name': 'pkgname'}
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>