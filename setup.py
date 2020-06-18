import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-email-verification",
    version="0.0.5.post1",
    author="Leone Bacciu",
    author_email="leonebacciu@gmail.com",
    description="Email confirmation app for django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeoneBacciu/django-email-verification",
    packages=setuptools.find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
