import setuptools

setuptools.setup(
    name="jukebox",
    version="0.0.1",
    author="Evgeny Petrov",
    packages=setuptools.find_packages(),
    install_reuires=[
        "pygame",
        "spidev",
        "mfrc522"
        ]
)
