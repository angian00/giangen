setuptools.setup(
    name="giangen",
    version="0.3.0",
    author="Andrea Giancola",
    author_email="andrea.giancola@gmail.com",
    description="A dungeon generator",
    url="https://github.com/angian00/giangen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pillow',
    ]
)
