# Python Packaging helper
A Python Packaging helper CLI

### LEARN

[Learn about Python packaging](https://packaging.python.org/en/latest/)

[Simple packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)


## Installation

PIP from [PyPi.org](https://pypi.org/project/helpmepack/)
```
pip install helpmepack
```

Or download this developing branch:
```
pip install git+https://github.com/dviralfi/HelpMePack.git
```


## Usage

Please make sure you have your '.git' folder, and README.md, .gitignore, requirments.txt, LICENSE files - in your project directory.

All the other project files will be moved to the 'src' folder.
The program won't move your ignored files that you configured in '.gitignore' file.

Make sure you running in the Project Main Directory.


## 
Run Python (in cmd/bash) in your project directory

```
from helpmepack import helpmepack 
```

```
helpmepack.main()
```

[HelpMePack in PyPi](https://pypi.org/project/helpmepack/)