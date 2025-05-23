from setuptools import setup, find_packages

setup(
    name='my-awesome-package',  # The name of your package
    version='0.1.0',            # The current version of your package
    author='Your Name',         # Your name or organization
    author_email='your.email@example.com', # Your email
    description='A small example Python package.', # A brief description
    long_description=open('README.md').read(), # Longer description from README.md
    long_description_content_type='text/markdown', # Type of the long description
    url='https://github.com/yourusername/my-awesome-package', # URL to your project's repository
    packages=find_packages(),   # Automatically find all Python packages in your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',    # Minimum Python version required
    install_requires=[          # List of dependencies required by your package
        # 'requests>=2.20.0',   # Example: if your package uses the 'requests' library
        # 'numpy',              # Example: another dependency
    ],
    # If your package includes non-Python files (e.g., data files, config files)
    # include_package_data=True,
    # package_data={
    #     'my_awesome_package': ['data/*.txt'], # Example: includes .txt files from a 'data' subfolder
    # },
)