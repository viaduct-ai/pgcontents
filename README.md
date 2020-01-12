HybridContents
======================

The `HybridContentManager` was originally created by [Quantopian](https://www.quantopian.com/) as part of [pgcontents](https://github.com/quantopian/pgcontents); however, the usage of `HybridContentsManager` was restricted to the compatibility requirements of [pgcontents](https://github.com/quantopian/pgcontents). These restrictions included `postgres` dependencies and no support for the latest [notebook](https://pypi.org/project/notebook/) version (>6).

At [Viaduct](https://viaduct.ai) we used [pgcontents](https://github.com/quantopian/pgcontents) exclusively for the `HybridContentsManager` and wanted to extend its functionality, so we created this fork [hybridcontents](https://github.com/viaduct-ai/hybridcontents).

See related [pgcontents](https://github.com/quantopian/pgcontents) issues:
- https://github.com/quantopian/pgcontents/issues/66
- https://github.com/quantopian/pgcontents/issues/50
- https://github.com/quantopian/pgcontents/issues/28

Getting Started
---------------
**Prerequisites:**
 - A Python installation with [Jupyter Notebook](https://github.com/jupyter/notebook) >= 4.0.

**Installation:**

#### [pip](https://pypi.org/project/hybridcontents/)
```bash
pip install hybridcontents
```
#### [Anaconda](https://anaconda.org/viaduct/hybridcontents)
```bash
conda install -c viaduct hybridcontents
```
#### [conda-forge](https://github.com/conda-forge/hybridcontents-feedstock)
See instructions [here](https://github.com/conda-forge/hybridcontents-feedstock#installing-hybridcontents)

Featues
-----
- Mix and match different content managers for different directories 
- Easily move files between different content managers (i.e local files to s3 backed manager) 
- Path validation to keep consistent naming scheme and/or prevent illegal characters

Usage
-----
For a detailed example see, [hybrid_manager_example.py](https://github.com/viaduct-ai/hybridcontents/blob/master/examples/hybrid_manager_example.py)

The following code snippet creates a HybridContentsManager with two directories with different content managers. 

```python
c = get_config()

c.NotebookApp.contents_manager_class = HybridContentsManager

c.HybridContentsManager.manager_classes = {
    "": FileContentsManager,
    "shared": S3ContentsManager
}

# Each item will be passed to the constructor of the appropriate content manager.
c.HybridContentsManager.manager_kwargs = {
    # Args for root FileContentsManager
    "": {
        "root_dir": read_only_dir
    },
    # Args for the shared S3ContentsManager directory
    "shared": {
        "access_key_id": ...,
        "secret_access_key": ...,
        "endpoint_url":  ...,
        "bucket": ...,
        "prefix": ...
    },
}

def only_allow_notebooks(path):
  return path.endswith('.ipynb')

# Only allow notebook files to be stored in S3
c.HybridContentsManager.path_validators = {
    "shared": only_allow_notebooks
}
```


Testing
-------
To run unit tests, 

```bash
tox
```

This will run all unit tests for python versions 2.7, 3.6, 3.7 and jupyter notebook versions 4, 5, and 6.

### Publishing a Release

1. Create a new release on Github
2. Update the version in `setup.py`
3. Run ./scripts/pip_publish.sh
4. Update the version `meta.yaml`
5. Update the [sha256 in meta.yaml](https://github.com/conda-forge/staged-recipes/wiki/Frequently-asked-questions#2-how-do-i-populate-the-hash-field)
6. Run ./scripts/anaconda_publish.sh
7. Update on Conda Forge
