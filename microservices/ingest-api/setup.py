from setuptools import find_packages, setup


def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name="Ingest API",
    version="0.0.1",
    author="Kariman",
    description="Microsserviço para ingestão de dados de uma API",
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
