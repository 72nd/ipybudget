import setuptools

setuptools.setup(
    name="ipybudget",
    version="0.1.0",
    author="72nd",
    author_email="msg@frg72.com",
    packages=setuptools.find_packages(),
    install_requires=[
        "money==1.3.0",
        "vdom==0.6",
    ],
)
