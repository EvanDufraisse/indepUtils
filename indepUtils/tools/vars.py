#
# Created on Sat Apr 30 2022
#
# Copyright (c) 2022 CEA - LASTI
# Contact: Evan Dufraisse,  evan.dufraisse@cea.fr. All rights reserved.
#

import inspect

def retrieve_name_variable(var, idx=-1, all=False):
    """Retrieve the idx th name of content assigned to a variable

    Args:
        var (var): python variable
        idx (int, optional): index of variable name to return. Defaults to -1.
        all (bool, optional): return all variable names found. Defaults to False.

    Returns:
        list[str]/str: list of variable names or name
    """
    callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
    vars = [var_name for var_name, var_val in callers_local_vars if id(var_val) == id(var)]
    if len(vars) == 0:
        return None
    elif all:
        return vars
    return vars[idx]

