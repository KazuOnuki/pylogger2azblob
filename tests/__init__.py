# ref: <https://docs.pytest.org/en/latest/explanation/goodpractices.html#tests-as-part-of-application-code>
# -----
# Note
# In prepend and append import-modes, if pytest finds a "a/b/test_module.py" test file while recursing into the filesystem it determines the import name as follows:
# determine basedir: this is the first “upward” (towards the root) directory not containing an __init__.py. If 
# e.g. both a and b contain an __init__.py file then the parent directory of a will become the basedir.
# -----