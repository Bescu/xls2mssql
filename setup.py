from distutils.core import setup

setup(
    name = "xls2mssql",
    version = "0.0.8",
    packages = ["xls2mssql"],
    install_requires = ['xlrd', 'plac', 'adodbapi'],
    description = "Convert excel files following a particular schema into SQL Server database (MSSQL)",
    author = "Joshua Holbrook modified by Maxime Résibois",
    author_email = "josh.holbrook@gmail.com, maxime.resibois@gmail.com",
    url = "https://github.com/jesusabdullah/xls2db ; https://github.com/Bescu/xls2mssql",
    keywords = ["excel", "mssql"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7", #only one tested
        "Topic :: Other/Nonlisted Topic"
    ],
    scripts = ["./bin/xls2mssql"],
    long_description = """\
xls2mssql
======

This is a adaptation of the source code of Joshua Holbrook, xls2db in order to import a xls into a SQL Server database instead of a sqlite database.

Requirements
-----

The module Adodapi need to be installed

Documentation
-----

See the xls2db documentation to learn more about this module
    """
)
