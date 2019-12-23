import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quanlyhoctap_goi-hoangthuhacnttk62",
    version="0.0.1",
    author="HoangThuHa",
    author_email="hoangha27499@gmail.com",
    description="A small manage-app package",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://https://github.com/belowacloud/quanlyhoctap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)