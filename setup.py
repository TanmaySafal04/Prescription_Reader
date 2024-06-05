from setuptools import find_packages,setup

setup(
    name='PRESCRIPTION_READER',
    version='0.0.1',
    author='Tanmay safal',
    author_email='tanmaysafal.4@gmail.com',
    install_requires=["gTTS","langchain","streamlit","python-dotenv","PyPDF2","paddlepaddle","paddleocr","streamlit","transformers","langsmith","langchain_community"],
    packages=find_packages()
)