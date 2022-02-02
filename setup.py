from setuptools import setup
import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='digic',
    version='0.0.2',
    description='A privacy focused command line tool to track your crypto portfolio',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Dennis',
    author_email='dennisconcepcionmartin@gmail.com',
    url='https://digic.app',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Office/Business :: Financial :: Investment',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Operating System :: OS Independent',

    ],
    keywords='tracker portfolio privacy bitcoin ethereum blockchain price cryptocurrency',
    project_urls={
        'Documentation': 'https://docs.digic.app',
        'Source': 'https://github.com/denniscm190/digic',
        'Tracker': 'https://github.com/denniscm190/digic/issues',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
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
