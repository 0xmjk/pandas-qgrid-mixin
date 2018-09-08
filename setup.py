from setuptools import setup

setup(
        name='pandas-qgrid-mixin',
        install_requires=['pandas', 'qgrid', 'ipython>=4.0.0'],
        version='0.1',
        description='pandas/ipython mix-in to use qgrid as default DataFrame display method',
        url='http://github.com/0xmjk/pandas-qgrid-mixin',
        license='Apache-2.0',
        packages=['pandas_qgrid_mixin'],
        zip_safe=False)
