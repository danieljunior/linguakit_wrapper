import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="linguakit_wrapper",
    version="0.0.1",
    author="Daniel Junior",
    author_email="danieljunior@id.uff.br",
    description="Wrapper Python to Linguakit binaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False,
    # install_requires=[],
)
