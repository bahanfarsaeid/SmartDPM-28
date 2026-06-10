from setuptools import setup, find_packages

setup(
    name="smartdpm-28",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={"smartdpm_28": ["data/*.npy"]},
    description="SmartDPM-28: A cleaned and standardized 28x28 pressure-map dataset derived from MIT-BIH for sleep posture classification.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Ali",
    license="MIT",
    url="https://github.com/yourusername/SmartDPM-28",
    python_requires=">=3.7",
)
