from setuptools import setup, find_packages

setup(
    name='analisador_feedback',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'spacy',
        'textblob',
        'streamlit',
    ],
    entry_points={
        'console_scripts': [
            'analisador_feedback=app:main',
        ],
    },
    description='Um analisador de feedback utilizando SpaCy e TextBlob.',
    author='Cauã Perboni',
    url='https://github.com/seu_usuario/analisador_feedback',
)
