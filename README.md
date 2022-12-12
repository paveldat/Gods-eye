# GOD'S EYE
God's EYE - Information Gathering Tool.
God's EYE is an Information Gathering Tool I made in python3.10.

## Library installation
All modules located in the `src` directory are APIs, so you can build a library from the sources and use it in your projects.

### 1. How to build a library from sources
1) Clone this repo
```shell
git clone https://github.com/paveldat/God-s-eye.git
```
2) Go to the cloned repository
```shell
cd God-s-eye
```
3) Install deb- and py-requirements
```shell
pip install -r py-requirements.txt
xargs sudo apt-get install <deb-requirements.txt
```
4) Run the following command
```shell
python3 -m build
```
5) Now you can install library
```shell
pip install dist/gods_eye-<version>-py3-none-any.whl
```

### 2. Installation from `releases`
1) Download `.whl` file form releases
2) Run the following command:
```shell
pip install <downloaded_file>.whl
```

## How to use
Now you can use this library. To connect a module to your project, just import it.
All modules can be found in the `src` directory.

Example:
```python
from clickjacking.clickjacking import ClickJacking
```

It is not difficult to guess that the following template is used here:
`from <directory>.<filename> import <class_name>`

Be careful, we don't use the `src` directory anymore.