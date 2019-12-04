from setuptools import setup, find_packages
from os.path import join, dirname, abspath
import sys

long_description = ''

if 'upload' in sys.argv or '--long-description' in sys.argv:
    with open('README.md') as f:
        long_description = f.read()


def read_requirements(basename):
    reqs_file = join(dirname(abspath(__file__)), basename)
    with open(reqs_file) as f:
        return [req.strip() for req in f.readlines()]


def main():
    reqs = read_requirements('requirements.txt')
    test_reqs = read_requirements('requirements_test.txt')

    setup(
        name='hybridcontents',
        version='0.1.1',
        description="Hybrid Content Manager",
        long_description=long_description,
        author="viaduct.ai",
        author_email="engineering@viaduct.ai",
        packages=find_packages(include='hybridcontents.*'),
        license='Apache 2.0',
        download_url=
        'https://github.com/viaduct-ai/hybridcontents/archive/v0.1.1.tar.gz',
        include_package_data=True,
        zip_safe=True,
        url="https://github.com/viaduct-ai/hybridcontents",
        classifiers=[
            'Development Status :: 4 - Beta',
            'Framework :: IPython',
            'License :: OSI Approved :: Apache Software License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python',
        ],
        keywords=[
            'jupyterhub', 'pgcontents', 'hybridcontents', 'content manager',
            'hybridcontentmanager'
        ],
        install_requires=reqs,
        extras_require={
            'test': test_reqs,
        },
    )


if __name__ == '__main__':
    main()
