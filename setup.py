from setuptools import setup

setup(name='money',
      version='0.1',
      description='Implementation of Fowler\s Money',
      url='https://github.com/luka-mladenovic/fowlers-money',
      author='Luka Mladenovic',
      author_email='',
      license='MIT',
      packages=['money'],
      install_requires=[
          'pyyaml',
      ],
      zip_safe=False)
