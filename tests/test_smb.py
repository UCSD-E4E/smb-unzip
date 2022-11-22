"""Example test module
"""
import json
from tempfile import TemporaryDirectory
from pathlib import Path
import smb_unzip.smb_unzip as dut


def test_unzip():
    """Tests downloading and unzipping a file based on parameters from a json file

    The JSON file must meet the following schema:
    ```
    {
        "url": str, # URL of the file, for example, smb://example.com/share/file.zip
        "username": str, # Username for Samba share
        "password": str, # Password for Samba share in plaintext
        "verify": [
            str, # List of paths to verify existence of.  These should be relative to the zip root
        ]
    }
    ```
    """
    with open('smb_test_creds.json', 'r', encoding='ascii') as handle:
        params = json.load(handle)
    with TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        dut.smb_unzip(
            network_path=params['url'],
            output_path=tmp_path,
            username=params['username'],
            password=params['password']
        )
        for verify_pathname in params['verify']:
            verify_path = tmp_path.joinpath(verify_pathname)
            assert verify_path.exists()
