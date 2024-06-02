# Python imports
import inspect
import os


# https://stackoverflow.com/a/24628710
foo_name = lambda: inspect.stack()[1][3]


async def remove_file(file: str) -> None:
    """
    Remove file from project. 
    Parameters:
        file: path of file that would be deleted
    """
    os.remove(file)
