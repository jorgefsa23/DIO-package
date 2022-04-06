from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="list_sort",
    version="0.0.1",
    author="Jorge Escobar",
    author_email="jorge.fsa23@gmail.com",
    description="Software Engineering student. This is my firt project of package for python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    setup_requires="wheel",
    url="https://github.com/jorgefsa23/",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)