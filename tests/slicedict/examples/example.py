#!/usr/bin/env python
import slicedict

keys = ["name", "version"]

medatata = dict(name="pkgname", version="1.0.0", somekey="value")
sliced = slicedict.slice(medatata, keys)
assert sliced == {'name': 'pkgname', 'version': '1.0.0'}
