#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Setup pycls."""

from setuptools import find_packages, setup


def readme():
    """Retrieves the readme content."""
    with open("README.md", "r") as f:
        content = f.read()
    return content


setup(
    name="lidar-bonnetal",
    version="0.1.1",
    description="A codebase for 3D point cloud semantic segmentation",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/WoojuLee24/lidar-bonnetal",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["numpy", "opencv-python", "simplejson", "yacs"],
)
