from setuptools import setup, find_packages


def load_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip().split('==')[0] for line in f]


setup(
    name='weather',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements(),
    entry_points={
        'console_scripts': [
            'weather = weather.main:main',
        ]
    },
)
