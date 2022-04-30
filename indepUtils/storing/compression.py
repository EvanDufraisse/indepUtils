#
# Created on Sat Apr 30 2022
#
# Copyright (c) 2022 CEA - LASTI
# Contact: Evan Dufraisse,  evan.dufraisse@cea.fr. All rights reserved.
#

from typing import Iterator
import gzip
import json
try:
    import zstandard as zst
    ZST_AV = True
except ImportError:
    ZST_AV = False


class GzipJsonlIterator(Iterator):
    """Return an iterator over the values of a jsonline gz

    Args:
        Iterator (_type_): _description_
    """

    def __init__(self, path, to_bytes=True, encoding="utf-8", labels = None):
        self.path = path
        self.iter = iter(gzip.open(path))
        self.to_bytes = to_bytes
        self.labels = labels
        self.encoding = encoding


    def __iter__(self):
        return self


    def __next__(self):
        if self.to_bytes:
            return next(self.iter)
        elif self.labels is None:
            return json.loads(next(self.iter).decode(self.encoding))
        else:
            j = json.loads(next(self.iter).decode(self.encoding))
            return {key:value for key, value in j.items() if key in self.labels}


class ZstJsonlIterator(Iterator):
    #TODO: Implement
    def __init__(self, path, to_bytes=True, encoding="utf-8", labels = None):
        raise NotImplemented
        if not(ZST_AV):
            raise ImportError(name="zstandard")

        self.path = path
        self.iter = iter(gzip.open(path))
        self.to_bytes = to_bytes
        self.labels = labels
        self.encoding = encoding
        self.decompressor = zst.ZstdDecompressor()
