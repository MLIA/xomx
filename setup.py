# Install with 'pip install -e .'

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="xomx",
    version="0.1.0",
    author="Nicolas Perrin-Gilbert",
    description="xomx: a python library for computational omics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/perrin-isir/xomx",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.1",
        "anndata>=0.7.6",
        "scipy>=1.4.1",
        "matplotlib>=3.1.3",
        "scikit-learn>=0.24.2",
        "joblib>=1.0.1",
        "requests>=2.23.0",
        "holoviews>=1.15.0",
        "bokeh>=2.4.3",
        "leidenalg>=0.8.8",
    ],
    license="LICENSE",
)
