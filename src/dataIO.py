from datetime import datetime


def parse_date(date_string : str) -> datetime:
    """
    Function Details
    ================
    Parse time stamp information in various formats.

    Parameters
    ----------
    date_string: string
        Date and time string.

    Returns
    -------
    datetime: datetime
        Date and time as a datetime object.

    See Also
    --------
    datetime strptime

    Notes
    -----
    Add new timestamp formats to the top for loop.

    Example
    -------
    None.

    ----------------------------------------------------------------------------
    Update History
    ==============

    09/07/2024
    ----------
    Documentation updated.

    """
    for fmt in ("%d/%m/%Y %H:%M", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    raise ValueError(f"time data {date_string} does not match any known format")


def convert_datetime(date_time: datetime) -> float:
    """
    Function Details
    ================
    Convert datetime into seconds.

    Parameters
    ----------
    date_time: datetime
        Date and time as a datetime object.

    Returns
    -------
    time: float
        Time in seconds.

    See Also
    --------
    parse_date

    Notes
    -----
    None.

    Example
    -------
    None.

    ----------------------------------------------------------------------------
    Update History
    ==============

    09/07/2024
    ----------
    Created.

    """
    time = date_time.timestamp()
    return time


def zeros_times(time: int,
                t_0 : int):
    """
    Function Details
    ================
    Zero time to some initial time.

    Parameters
    ----------
    time, t_0: int
        Time value to zero, initial time.

    Returns
    -------
    Corrected_time: int
        Time from zero point.

    See Also
    --------
    None.

    Notes
    -----
    None.

    Example
    -------
    None.

    ----------------------------------------------------------------------------
    Update History
    ==============

    09/07/2024
    ----------
    Created.

    """
    corrected_time = time - t_0
    return corrected_time