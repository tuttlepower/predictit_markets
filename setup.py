from setuptools import setup, find_packages

setup(
    name="predictit_markets",  # Package name
    version="0.1.4", 
    author="Travis Tuttle",
    author_email="28586132+tuttlepower@users.noreply.github.com",
    description="A package for interacting with PredictIt markets",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tuttlepower/predictit_markets",
    packages=find_packages(),
    package_data={
        'predictit_markets': ['images/*.png']  # Include image files in the package
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
          'pandas',  # Add any dependencies your package needs
    ],
)
