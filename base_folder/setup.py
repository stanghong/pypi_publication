from setuptools import setup, find_packages
# from distutils.core import setup
import codecs
import os


VERSION = '0.0.8'
DESCRIPTION = 'quicklookts08'

# Setting up
setup(
    name="quicklookts07",
    version=VERSION,
    author="Hong Tang",
    author_email="<stanghong@gmail.com>",
    description=DESCRIPTION,
    url = 'https://github.com/stanghong/pypi_publication', 
   packages=find_packages('quicklookts07'),
    install_requires=['numpy','pandas', 'matplotlib' ],
    download_url = 'https://github.com/stanghong/pypi_publication/archive/refs/tags/v0.07.tar.gz',
    
    keywords=['python', 'timeseries','plot'],

    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
