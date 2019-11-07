import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyPelias",
    version="0.1.0",
    author="Lawrence Stewart",
    author_email="lawrence@lawrencestewart.ca",
    description="A simple python wrapper for the Pelias API for geocoding and reverse geocoding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/getorca",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
