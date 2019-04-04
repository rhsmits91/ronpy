import logging

import ronpy
from ronpy.decorators import validate_annotation

def test_validate_annotation(caplog):
    @validate_annotation()
    def some_func(a, b: dict, c: str='a', d: int=1, e: list=[1, 2]):
        return a, b, c, d, e

    result = some_func('a', {}, 'b', 2)
    expected_types = (str, dict, str, int)
    for p, t in zip(result, expected_types):
        assert isinstance(p, t)
    
    assert caplog.record_tuples == [
        ('ronpy', logging.WARNING, 
         'Parameter `a` cannot be validated as no annotation is set. ' 
         'Continuing...'),
    ]
