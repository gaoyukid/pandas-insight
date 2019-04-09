import os

__location__ = os.path.dirname(__file__)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pandas-insight',
    version='0.0.1',
    author='Yu Gao',
    author_email='gaoyu.kid@gmail.com',
    packages=['pandas_insight'],
    url='https://github.com/gaoyukid/pandas-insight/',
    license='MIT',
    description='Find joinable columns between two dataframes',
    install_requires=[
        "pandas>=0.19",
        "statsmodels>=0.9.0"
    ],
    include_package_data = False,
    classifiers=[
        'Development Status :: 1 - Development/Pilot',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Framework :: IPython',
        'Programming Language :: Python :: 3.7'

    ],
    keywords='pandas data-science data-analysis python jupyter ipython',

)