"""
Author: Jagadeesh LakshmiNarasimhan

Created on 10-July-2022
"""

import os

"""
Author: Jagadeesh LakshmiNarasimhan
Created on 28-September-2021
"""


def install_packages():
    packages_list = ['pip', 'python-csv', 'requests', 'xlsxwriter']
    import pip
    for package in packages_list:
        pip.main(['install', package])