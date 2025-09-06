from setuptools import setup, find_packages

setup(
    name="ai_bias_evaluator",
    version="0.1.0",
    author="Alexander Maxwell,
    author_email="alexmaxdout@outlook.com,
    description="A tool to evaluate and mitigate bias in AI models with fairness metrics and dashboards.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR-USERNAME/ai-bias-evaluator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.25.0",
        "pandas>=2.1.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.2",
        "streamlit>=1.26.0",
        "pytest>=7.4.0",
        "fairlearn>=0.9.2"
    ],
    entry_points={
        "console_scripts": [
            "evaluate_bias=evaluator:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
