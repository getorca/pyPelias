import pathlib2
import setuptools

# The directory containing this file
HERE = pathlib2.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="pyPelias",
    version="0.1.0",
    author="Lawrence Stewart",
    author_email="lawrence@lawrencestewart.ca",
    description="A simple python wrapper for the Pelias API for geocoding and reverse geocoding",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/getorca/pyPelias",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
