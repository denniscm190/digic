from setuptools import setup


setup(
    name='digic',
    version='0.0.1',
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'digic = digic.cli:cli_group',
        ],
    },
)
