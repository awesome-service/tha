import setuptools

with open("README.md", encoding="utf-8") as f:
  long_description = f.read()

setuptools.setup(
  name="tha-fork",
  version="0.1.4",
  description="A Khmer Text Normalization and Verbalization Toolkit.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/seanghay/tha",
  author="Seanghay Yath",
  author_email="seanghay.dev@gmail.com",
  license="Apache License 2.0",
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Natural Language :: English",
  ],
  python_requires=">3.5",
  packages=setuptools.find_packages(),
  package_dir={"tha_fork": "tha_fork"},
  install_requires=[
    "urlextract",
    "phonenumbers",
    "regex",
    "ftfy",
  ],
)
