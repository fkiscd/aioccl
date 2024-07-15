from setuptools import find_packages, setup

VERSION = "2024.7"

setup(
  name = "aioccl",
  packages=find_packages(exclude=["tests", "misc"]),
  version=VERSION,
  license="Apache License, Version 2.0",
  description="A Python library for CCL API server",
  author="fkiscd",
  author_email = "fkiscd@gmail.com",
  url="https://github.com/fkiscd/aioccl",
  download_url="https://github.com/fkiscd/aioccl",
  install_requires=[
          "aiohttp>3",
          "aiohttp_cors>=0.7.0"
      ],
  include_package_data=True,
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: Apache Software License",
    "Topic :: Home Automation",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.12",
  ],
)
