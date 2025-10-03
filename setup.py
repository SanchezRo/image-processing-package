from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="rodrigo_sanchez",
    author_email="zarigin51@hotmail.com",
    description="a simple image processing library",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SanchezRo/image-processing-package/blob/9c0d148bb90eea822bf45ded179ba087821fa672/setup.py#L17"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8 ',
)