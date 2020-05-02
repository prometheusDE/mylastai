import setuptools

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='mylastai',
      version='0.1.0',
      description='Do machine learning and talk about it.',
      url='https://mylast.ai',
      author='Andreas Backhaus',
      author_email='andreas.backhaus@mylast.ai',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
        'nvidia-dali==0.21.0',
        'nvidia-dali-tf-plugin==0.21.0',
        'tensorflow==2.1.0',
        'onnx==1.6.0',
        'mxnet-cu101mkl==1.6.0',
        'opencv-python==4.2.0.34',
        'pillow==7.1.2',
        'matplotlib==3.2.1',
        'numpy==1.18.3',
        'utils==1.0.1'
      ],
      zip_safe=False
      )


