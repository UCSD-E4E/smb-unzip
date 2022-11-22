# smb-unzip
This package provides a way to easily download and unzip a `.zip` file into the specified directory

# Example Usage

```
from pathlib import Path

from smb_unzip.smb_unzip import smb_unzip

smb_unzip(
    network_path='smb://example.com/share/path/file.zip',
    output_path=Path('.'),
    username='username',
    password='password',
)
```

For the above example, if file.zip contained the following structure:
```
file.zip
  > folderA
    - file1
    - file2
  - file3
```

Then we would have the resulting structure:
```
.
> folderA
  - file1
  - file2
- file3
```

## Developers
This package should be developed using VS Code.
1. Clone this repository
2. Open `smb-unzip.code-workspace` with VS Code.
3. Create a python virtual environment for this project (we suggest `venv`, so do `python3 -m venv .venv` and select that environment for this project)
4. Install this package as editable (`python -m pip install -e .`)
5. Enable linting and testing (`python -m pip install pylint pytest`)
6. Configure your test parameters
    1. Create `${workspaceFolder}/smb_test_creds.json`
    2. Put the following information into `${workspaceFolder}/smb_test_creds.json`:
    ```
    {
        "url": "smb://example.com/share/path/file.zip",
        "username": "username",
        "password": "password",
        "verify": [
            "folder/file"
        ]
    }
    ```