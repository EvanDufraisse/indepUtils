#
# Created on Sat Apr 30 2022
#
# Copyright (c) 2022 CEA - LASTI
# Contact: Evan Dufraisse,  evan.dufraisse@cea.fr. All rights reserved.
#
from typing import Iterator

class BatchIterator(Iterator):
    """Batch iteration implementation

    Args:
        Iterator (Iterator): iterator to transform into batch iterator
        Batch_size (int) : size of batch
        Drop_last (bool) : whether to drop last batch if doesn't respect desired size
    """

    def __init__(self, iterator, batch_size = None, drop_last = False):
        self.iterator = iterator
        self.batch_size = batch_size
        self.drop_last = drop_last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        l = []
        for _ in range(self.batch_size):
            try:
                l.append(next(self.iterator))
            except StopIteration:
                if len(l) > 0:
                    if self.drop_last and len(l) < self.batch_size:
                        raise StopIteration
                    else:
                        return l
                else:
                    raise StopIteration


class ProcessingIterator(Iterator):
    """Allow to iterate over an iterator with an intermediate processing function

    Args:
        Iterator (Iterator): iterator to iterate
        Processing_func (function): function implementing the __call__ method
    """

    def __init__(self, iterator, processing_func):
        self.iterator = iterator
        self.processing_func = processing_func

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.processing_func(next(self.iterator))

class EmptyIterator(Iterator):
    """Empty iterator that raises StopIteration at the first __next__ call
    """
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

class MergeIterator(Iterator):
    """Return an unique iterator from several iterators

    """


    def __init__(self, list_of_iterators):
        self.list_of_iterators = [EmptyIterator()] + list_of_iterators
        self.index = 0
        self.current_iterator = self.list_of_iterators[self.index]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.current_iterator)
        except StopIteration:
            self.index += 1
            if self.index >= len(self.list_of_iterators):
                raise StopIteration
            else:
                self.current_iterator = self.list_of_iterators[self.index]
                return next(self)
