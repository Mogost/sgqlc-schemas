from distutils.core import setup

import setuptools

with open('README.md') as f:
    long_description = f.read()

setup(
    name='sgqlc_schemas',
    packages=setuptools.find_packages(),
    version='0.1.0',
    description='A set of schemas for sgqlc package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alexandr Artemyev',
    author_email='mogost@aartemyev.ru',
    license='MIT',
    url='https://github.com/Mogost/sgqlc-schemas',
    keywords=['sgqlc', 'schema', 'schemas', 'graphql', 'github', 'monday'],
    install_requires=['sgqlc'],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
