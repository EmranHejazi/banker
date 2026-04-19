def jalali_year_from_date(date_string: str) -> int:
    """
    Input format: 1366-01-05
    Output: 1366
    """
    return int(date_string.split("-")[0])
