from setuptools import setup, find_packages

setup(
    name='Ukr_TAX_ID_Generator',
    version='1.0.0',
    packages=find_packages(),
    description='This package generates Ukraine TAX ID by user birthday',
    long_description=open('README.md').read(),
    author='Serhii Lozytskyi',
    url='https://github.com/lozik4/UkrTaxIdGenerator',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)