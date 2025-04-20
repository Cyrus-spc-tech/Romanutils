from setuptools import setup, find_packages

setup(
    name='romanutils',
    version='0.1.1',
    author='cyrus-spc-tech',
    description='A Python library for Roman numeral manipulation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Cyrus-spc-tech/Romanutils.git',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3'
    
    ],
    python_requires='>=3.6',
)