import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken_disease_classification_project"
AUTHOR_USER_NAME = "Seemagurudarshan"
SRC_REPO = "CnnClassifier"
AUTHOR_EMAIL = "seemagurudarshan@gmail.com"


setuptools.setup(
    name='CnnClassifier',
    version=__version__,
    author="Seemagurudarshan",
    author_email="seemagurudarshan@gmail.com",
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Seemagurudarshan/Chicken_disease_classification_project/issues",
    project_urls={
        "Bug Tracker": f"https://github.com/Seemagurudarshan/Chicken_disease_classification_project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)