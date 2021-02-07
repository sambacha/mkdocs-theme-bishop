from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="bishop",
    version=VERSION,
    url='https://github.com/manifoldfinance/mkdocs-theme-bishop',
    license='BSD',
    description='Minimal theme for MkDocs',
    author='Sam Bacha',
    author_email='sam@manifoldfinance.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'bishop = bishop',
        ]
    },
    zip_safe=False
)
