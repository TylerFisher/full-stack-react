from setuptools import find_packages, setup

setup(
    name='full-stack-react-example',
    version='0.0.0-alpha',
    description='',
    url='https://github.com/The-Politico/full-stack-react-example',
    author='POLITICO interactive news',
    author_email='interactives@politico.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests', 'example']),
    include_package_data=True,
    install_requires=[],
    extras_require={
        'test': ['pytest'],
    },
)
