import os
import setuptools


def read(name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name)) as reader:
        return reader.read()


package = dict(
    name = 'pyreto-object',
    version = read('VERSION.txt'),
    author = 'Dan Gittik',
    author_email = 'dan.gittik@gmail.com',
    description = next(line for line in read('README.md').splitlines() if line.strip() and not line.startswith('#')),
    long_description = read('README.md'),
    license = 'MIT',
    url = 'https://github.com/dan-gittik/object',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    packages = setuptools.find_packages(),
    install_requires = read('requirements.txt').splitlines(),
    tests_require = ['pytest'],
)


if __name__ == '__main__':
	setuptools.setup(**package)
