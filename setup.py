from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='average_cambridge_assessment',
    version='0.0.1',
    description='Small Program to extract scores from certificate in advanced englisch pdf and calculate average score in each CEFR level',
    long_description=long_description,
    license='MIT',
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    author='Klaas Vogel',
    author_email='klaasvogel@hotmail.com',
    keywords=['excel', 'pdf', 'scraper', 'average', 'CEFR', 'Cambridge', 'certificate', 'advanced', 'English'],
    url='https://github.com/KlaasVogel/average_cambridge_assessment'
)