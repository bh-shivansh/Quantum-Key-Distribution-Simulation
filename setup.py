from setuptools import setup, find_packages

setup(name='qkdsim',
      version='1.0',
      description='Quantum Key Distribution Simulation Library',
      author='Shivansh Bhardwaj',
      author_email='shbhardwaj020@gmail.com',
      url='https://github.com/bh-shivansh/Quantum-Key-Distribution-Simulation',
      packages=find_packages(),
      install_requires=[
          'qit',
          'pycrypto'
          ]
      )
      
