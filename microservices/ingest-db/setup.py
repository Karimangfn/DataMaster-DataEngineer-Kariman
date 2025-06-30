from setuptools import find_packages, setup


def read_version():
    with open('VERSION') as f:
        return f.read().strip()


def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name="Ingest DB",
    version=read_version(),
    author="Kariman",
    description="Microsserviço para ingestão de dados de um Banco de Dados",
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'ingest-db = src.interfaces.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
