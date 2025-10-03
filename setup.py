from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-sanchez",
    version="0.0.1",
    author="rodrigo_sanchez",
    author_email="zarigin51@hotmail.com",
    description="a simple image processing library",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SanchezRo/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8 ',
)
pypi-AgENdGVzdC5weXBpLm9yZwIkNjRiODg2YTctY2U5OC00ZTUwLTg5NzgtZWE4MTI3NzMzYjVkAAIqWzMsImUxZDM5ZGYyLTc1YTctNDQ2NS1hZmRlLTM0YTYwMTQyNjRiMyJdAAAGIL7axa-UmlmnBFG03CThewgGxRLYUJcDofS7z48hIILJ
 