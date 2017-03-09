"""Utils functions."""


def serialize_data(schema, items):
    """
    This method is responsible for serialization data.

    :param schema:
    :param items:
    :return:
    """
    data = []
    if items:
        result = schema.dump(items)
        data = result.data
    return data
