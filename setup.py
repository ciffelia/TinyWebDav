from setuptools import setup

version = '1.0'

setup(
    name='TinyWebDav',
    version=version,
    author='Lai ChuJiang',
    py_modules = ['webdav'],
    url='https://github.com/andrewleech/TinyWebDav',
    download_url='https://github.com/andrewleech/TinyWebDav/archive/gh-pages.zip',
    description='A Single File,Tiny, Python WebDav Server. Original package from https://github.com/wolf71/TinyWebDav',
    install_requires=["six"],
)