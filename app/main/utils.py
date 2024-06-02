# Python imports
import inspect


# https://stackoverflow.com/a/24628710
foo_name = lambda: inspect.stack()[1][3]