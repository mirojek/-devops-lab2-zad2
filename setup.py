from setuptools import setup, find_packages

setup(
    name="devops-lab2-app",
    version="0.1.0",
    author="mirojek",
    description="Prosta aplikacja dla DevOps",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={'': ['*']},
    install_requires=[],
    extras_require={
        "tests": ["pytest>=7.0"],
    },
    entry_points={
        "console_scripts": [
            "myapp=src.myapp.app:hello"
        ]
    },
)