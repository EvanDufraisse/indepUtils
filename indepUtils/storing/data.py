#
# Created on Sat Apr 30 2022
#
# Copyright (c) 2022 CEA - LASTI
# Contact: Evan Dufraisse,  evan.dufraisse@cea.fr. All rights reserved.
#

import gzip
import json
import pickle
import os
from ..tools.vars import retrieve_name_variable


def save(object: "object", name = None, path_folder :"str" = "./", create_path = True, versioning = False):
    '''

    :param python_object: object to save
    :return:
    '''
    #TODO: Implement versionning

    if versioning:
        raise NotImplemented
    
    absolute_path = os.path.abspath(path_folder)
    if not(os.path.isdir(absolute_path)):
        if create_path:
            os.makedirs(absolute_path, exist_ok=True)
        else:
            raise ValueError(f"Path {absolute_path} does not exist and not allowed to create it")
    
    if name is None:
        names = retrieve_name_variable(object, all=True)
        print(names)
        name = names[-1]

    name = name + ".pkl" if not(name.endswith(".pickle") or name.endswith(".pkl")) else name

    outfile = os.path.join(absolute_path, name)
    pickle.dump(object, open(outfile, "wb"))
    return {"name":name, "path":absolute_path, "versioning": versioning}


def load(name, path="./", versioning=False):
    '''

    :param name: name of the file to load
    :param path:
    :return: a python object
    '''
    if versioning:
        raise NotImplemented
    
    
    found = False
    for s in ["", ".pkl", ".pickle"]:
        if os.path.isfile(os.path.join(path,name+s)):
            name += s
            found = True
            break
    if not(found):
        raise ValueError(f"Pickle file {os.path.join(path,name)} wasn't found.")
    outfile = open(os.path.join(path,name), 'rb')
    file = pickle.load(outfile)
    outfile.close()
    return file
