import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccorp-yaml-include-relative-path",
    version="0.1.0",
    author="Yuri A. Mikhaylov",
    author_email="it@mikhailov.xyz",
    description="Exactly ccorp-yaml-include package with a bug fix and support of relative paths for included aliases",
    long_description_content_type="text/x-rst",
    long_description=long_description,
    url="https://github.com/mrkram/ccorp_yaml_include",
    packages=['ccorp.ruamel.yaml.include'],
    install_requires=['ruamel.yaml'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)