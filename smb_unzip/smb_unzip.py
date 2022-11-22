"""SMB Unzip to local module
"""
import zipfile
from pathlib import Path
from tempfile import TemporaryFile
from typing import Optional
from urllib.parse import urlparse

from smb.SMBConnection import SMBConnection


def smb_unzip(
        network_path: str,
        output_path: Path,
        *,
        username: Optional[str] = None,
        password: Optional[str] = None) -> None:
    """Unzips the file located at network_path to output_path

    Args:
        network_path (str): Network path of zip file
        output_path (Path): Local path to unzip to
        username (Optional[str], optional): Username for server. Defaults to None.
        password (Optional[str], optional): Password for server. Defaults to None.

    Raises:
        ConnectionError: Raised on connection/authentication error
    """
    url_parts = urlparse(network_path)
    smb = SMBConnection(
        username=username,
        password=password,
        my_name='',
        remote_name=url_parts.hostname.split('.')[0]
    )

    if not smb.connect(url_parts.netloc):
        raise ConnectionError

    with TemporaryFile() as handle:
        smb.retrieveFile(
            service_name=Path(url_parts.path).parts[1],
            path=Path(*Path(url_parts.path).parts[2:]).as_posix(),
            file_obj=handle
        )
        handle.seek(0)
        with zipfile.ZipFile(handle, 'r') as zip_handle:
            zip_handle.extractall(path=output_path.as_posix())
