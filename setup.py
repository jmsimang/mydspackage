from setuptools import setup, find_packages

setup(
    name='mydspackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA sorting and recursion package',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/jmsimang/mydspackage',
    author='<Jabulani Msimango>',
    author_email='<ja.msimango@gmail.com>'
)
