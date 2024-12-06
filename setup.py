from setuptools import setup, find_packages

setup(
    name="EmmanoelCardoso",  # Nome do módulo (deve ser único no PyPI)
    version="0.1.0",         # Versão inicial
    author="Emmanoel Cardoso",  # Seu nome
    description="Um módulo de exemplo com funções básicas.",  # Breve descrição
    packages=find_packages(),  # Detecta os pacotes automaticamente
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Versão mínima do Python
)
