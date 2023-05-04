from pythonforandroid.recipe import CythonRecipe


class PyProjRecipe(CythonRecipe):
    version = '3.5.0'
    url = 'https://github.com/pyproj4/pyproj/archive/refs/tags/3.5.0.zip'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False


recipe = PyProjRecipe()
