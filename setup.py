import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="energyforecaster", # Replace with your own username
    version="0.0.1",
    author="Daniel Chai",
    author_email="dc8291@gmail.com",
    description="EnergyForecaster: Real-time solar generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UW-EnergyForecaster/EnergyForecasters",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
