from importlib import import_module


def import_class(val):
    """
    Import a class from a string module path.

    Pattern borrowed from Django REST Framework.
    See rest_framework/settings.py#L170-L182
    """
    try:
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = import_module(module_path)
        return getattr(module, class_name)
    except (ImportError, AttributeError) as e:
        msg = "Could not import class '{}'. {}: {}.".format(
            val,
            e.__class__.__name__,
            e)
        raise ImportError(msg)
