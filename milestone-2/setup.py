import io

from setuptools import find_packages
from setuptools import setup

setup(
    name="sre-api",
    version="1.0.0",
    description="Contains the solution of one2n SRE bootcamp api-server",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Flask==3.0.3",
        "mysql-connector==2.2.9",
        "psycopg2-binary==2.9.9",
        "python-dotenv==1.0.1"
    ]
)