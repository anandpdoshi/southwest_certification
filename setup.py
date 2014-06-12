from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='southwest_certification',
    version=version,
    description='Southwest Certification ERPNext Extension',
    author='Anand Doshi',
    author_email='anand@frappe.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
