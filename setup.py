from setuptools import setup, find_packages

setup(
    name="devops-lab2-app",
    version="0.1.0",
    author="mirojek",
    description="Aplikacja DevOps.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        "tests": ["pytest"],
    },
    entry_points={
        "console_scripts": [
            "myapp=src.myapp.app:welcome"
        ]
    },
)