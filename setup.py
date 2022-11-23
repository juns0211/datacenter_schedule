from setuptools import setup, find_packages

setup(
    name='datacenter_schedule',
    version='0.0.15',
    description='數據中心系統專用排程器工具',
    py_modules=['clean', 'params', 'storage'],
    packages=find_packages(),
    package_data={'utils':['config.yaml']}
)