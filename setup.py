from setuptools import setup, find_packages

setup(
    name='romanutils',
    version='0.1.0',
    author='Your Name',
    description='A Python library for Roman numeral manipulation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/romanutils',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)