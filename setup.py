from setuptools import setup

setup(
    name='excel_parser',
    version='0.1',
    py_modules=['excel_parser'],
    install_requires=[
        'pandas',
        'openpyxl',
        'prettytable',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'excel-parser=excel_parser:print_colored_table',
        ],
    },
)
