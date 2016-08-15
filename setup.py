# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="mailroom",
    description="A Python implementation to help the mailroom \
    create reports or send thank you notes.",
    version=0.1,
    author="Victor Benavente, James Canning",
    author_email="vbenavente@hotmail.com, fake@fake.com",
    license='MIT',
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    entry_points={
        'console_scripts': [
            "mailroom = mailroom:main"
        ]
    }
)
