from setuptools import setup


def load_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip().split('==')[0] for line in f]


setup(
    name='weather',
    version='0.1',
    py_modules=['main'],
    install_requires=load_requirements(),
    entry_points={
        'console_scripts': [
            'weather = main:main',
        ]
    },
)
