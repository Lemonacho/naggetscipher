from setuptools import setup, find_packages

setup(
    name="naggetscipher",
    version="0.1.0",
    packages=find_packages(),
    description="Библиотека для шифрования и дешифрования текста методом 'Наггетс'",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Zaxece09",
    author_email="akkb704@gmail.com",
    url="https://github.com/Lemonacho/naggetscipher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)