"""
Secret Sharing
==============
"""

from setuptools import setup

setup(
    name='secretsharing',
    version='0.2.6',
    url='https://github.com/onenameio/secret-sharing',
    license='MIT',
    author='Halfmoon Labs',
    author_email='hello@halfmoon.io',
    description=("Tools for sharing secrets (like Bitcoin private keys), "
                 "using shamir's secret sharing scheme."),
    packages=[
        'secretsharing',
    ],
    zip_safe=False,
    install_requires=[
        'six',
        'utilitybelt', 'Crypto'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)