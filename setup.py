from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='weworkbot',
    version='0.0.1',

    description='A framework for creating bot for wechat work',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MakDon/we-work-bot',
    author='Makdon',
    author_email='makdon@makdon.me',

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='wechat bot',
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=['requests'],
)
