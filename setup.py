from setuptools import setup
from codecs import open
from os import path

package_name = "MidLine"

root_dir = path.abspath(path.dirname(__file__))


def _requirements():
    return [
        name.rstrip() for name in open(
            path.join(
                root_dir,
                'requirements.txt')).readlines()]


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=package_name,
    version='11.0.0',
    description='Wrapper for reproducing LINE app API requests.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/66ed3gs/midLine',
    author='66ed3gs',
    author_email='66ed3gs@gmail.com',
    license='MIT',
    keywords='LINE',
    packages=[package_name],
    install_requires=_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
)
