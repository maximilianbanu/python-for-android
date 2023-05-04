from pythonforandroid.recipe import CythonRecipe


class PyProjRecipe(CythonRecipe):
    version = '2.6.1'
    url = 'https://github.com/pyproj4/pyproj/archive/refs/tags/v2.6.1rel.zip'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False


recipe = PyProjRecipe()
