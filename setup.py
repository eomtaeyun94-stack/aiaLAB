from setuptools import setup

setup(
    name="aialabhtml",
    version="0.1",
    py_modules=["aialabhtml"],
    entry_points={
        "console_scripts": [
            "aialabhtml=aialabhtml:main",
        ],
    },
    author="Your Name",
    description="PowerShell에서 HTML 코드를 입력하고 브라우저에서 바로 보는 툴",
    url="https://github.com/<GitHub유저명>/aialabhtml",
)

