#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='passwordcrypto',
    version='1.1.0',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    author='Muxutruk',
    description='A package to help make an encrypted password manager',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Use 'text/plain' if README is not in markdown
    test_suite='tests',
    keywords=['password', 'cryptography', 'security'],
    url='https://github.com/Muxutruk2/passwordcrypto2',

    install_requires=[
        "cryptography"
    ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
    ],
)
