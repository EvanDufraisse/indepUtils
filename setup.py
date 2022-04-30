import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indepUtils",
    version="0.0.1",
    author="Evan Dufraisse",
    author_email="edufraisse@gmail.com",
    packages=setuptools.find_packages(exclude=[]),
    description="utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GPT',
    python_requires='>=3.7',
    install_requires=[]
)
