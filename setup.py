# External Libraries
from setuptools import setup, find_packages

version = "0.1.0"
description = "Official python wrapper for the lbots.org API"

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.readlines()

if __name__ == '__main__':
    setup(
        name="lbots",
        author="lbots",
        author_email="mail@lbots.org",
        maintainer="martmists",
        maintainer_email="mail@martmists.com",
        license="BSD-3",
        zip_safe=False,
        version=version,
        description=description,
        long_description=long_description,
        url="https://github.com/IzunaDevs/IzunaDSP",
        packages=find_packages(),
        install_requires=requirements,
        keywords=["lbots", "client", "api", "wrapper", "asyncio"],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Software Development :: Libraries :: Python Modules"
        ],
        python_requires=">=3.6")
