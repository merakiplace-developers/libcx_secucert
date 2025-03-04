from setuptools import setup, find_packages

setup(
    name="libcx_secucert_py39_x64",
    version="3.0.0",
    packages=find_packages(),
    package_data={
        'libcx_secucert': ['libs/*.so', 'libs/*.egg-info'],
    },
    include_package_data=True,
)
