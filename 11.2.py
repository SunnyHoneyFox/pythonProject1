def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = dir(obj)

    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    module = getattr(obj, '__module__', None)

    additional_info = {}
    if hasattr(obj, '__doc__'):
        additional_info['doc'] = obj.__doc__
    if hasattr(obj, '__name__'):
        additional_info['name'] = obj.__name__ if hasattr(obj, '__name__') else None
    if hasattr(obj, '__dict__'):
        additional_info['dict'] = obj.__dict__

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'additional_info': additional_info
    }

    return info


if __name__ == "__main__":
    for_example = introspection_info('example')
    print(for_example)
