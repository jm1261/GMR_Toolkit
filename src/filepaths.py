import os


def extractfile(directory_path : str,
                file_string : str) -> list:
    """
    Function Details
    ================
    Find files containing a certain string in their name in a target directory.

    Parameters
    ----------
    directory_path, file_string: string
        Path to target directory, desired string in file.

    Returns
    -------
    list: list
        List of files in target directory containing the desired string.

    See Also
    --------
    None

    Notes
    -----
    None

    Example
    -------
    None

    ----------------------------------------------------------------------------
    Update History
    ==============

    02/07/2024
    ----------
    Copied from another repository and documentation tidied.

    """
    directory_list = sorted(os.listdir(directory_path))
    return [file for file in directory_list if file_string in file]