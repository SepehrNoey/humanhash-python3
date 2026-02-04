# setup.py
from setuptools import setup
import os

setup(
    name='humanhash',
    version='0.0.2',
    description='Human-readable representations of digests.',
    long_description=open('README.md', encoding='utf-8').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    author='Sepehr Noey',
    author_email='sepehr.nk.81@gmail.com',
    url='https://github.com/SepehrNoey/humanhash-python3',
    py_modules=['humanhash'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
