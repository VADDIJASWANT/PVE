# setup.py
from setuptools import setup, find_packages

setup(
    name="pve",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pve = pve.cli:main",
        ],
    },
    install_requires=[],
    author="Vaddi Jaswant",
    author_email="vaddijaswant@gmail.com",
    description="A simple tool to manage Python virtual environments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VADDIJASWANT/PVE",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)