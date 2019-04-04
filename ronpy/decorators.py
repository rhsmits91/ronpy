"""
helper decorator functions
"""

import inspect

from .logger import logger


def validate_annotation(try_casting=False):
    """
    Uses a function's annotations to validate user passed parameters, and
    potentially cast them to the right datatypes (as given by the annotations).
    
    Parameters
    ----------
    try_casting : bool, optional
        [description] (the default is True, which [default_description])
    
    Raises
    ------
    e
        [description]
    ValueError
        [description]
    
    Returns
    -------
    [type]
        [description]
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            kwargs = inspect.getcallargs(func, *args, **kwargs)
            args, _, _, defaults, *_, annotations = inspect.getfullargspec(func)
            defaults = dict(zip(reversed(args), defaults))
            
            for k, v in kwargs.items():
                # check if the passed value is default value:
                if k in defaults and v is defaults[k]:
                    continue
                
                # check if there is no annotation:
                annotation = annotations.get(k, None)
                if annotation is None:
                    logger.warning(
                        f'Parameter `{k}` cannot be validated as no ' 
                        f'annotation is set. Continuing...'
                    )
                    continue
                
                # now check if passed value is of right type!
                if isinstance(v, annotation):
                    pass
                elif try_casting:
                    try:
                        v_new = annotation(v)
                        kwargs.update({k: v_new})
                        logger.info(
                            f'Value `{v}` for parameter `{k}` successfully '
                            f'turned into annotated type <{annotation}>.'
                        )

                    except (ValueError, TypeError) as e:
                        logger.critical(
                            f'Parameter `{k}` should be of type <{annotation}>'
                            f' but passed value `{v}` cannot be turned into '
                            f'<{annotation}>'
                        )
                        raise e
                else:
                    raise ValueError(
                        f'Parameter `{k}` should be of type <{annotation}>'
                        f' but passed value `{v}` cannot be turned into '
                        f'<{annotation}>'
                    )
            return func(**kwargs)
        return wrapper
    return decorator
