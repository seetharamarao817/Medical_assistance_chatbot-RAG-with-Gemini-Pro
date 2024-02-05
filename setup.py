from setuptools import find_packages,setup

setup(
    name='Medical_assistance_chatbot',
    version='0.0.1',
    author='Seetha Rama Rao',
    author_email='akashay8179@gmail.com',
    install_requires=["langchain","python-dotenv","PyPDF2"],
    packages=find_packages()
)