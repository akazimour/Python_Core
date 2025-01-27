from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:

    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    filtered_data = []
    for d in data:
        func = selector
        selected_dict = func(d)

        for filter in filters:
            func_filter = filter
            filtered_dict = func_filter(selected_dict)
            selected_dict = filtered_dict

        if len(filtered_dict) != 0:
            filtered_data.append(filtered_dict)

    return filtered_data



def select(*columns: str) -> ModifierFunc:

    """Return function that selects only specific columns from dataset"""

    def SELECT(data):
        return {k: data[k] for k in columns}

    return SELECT




def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""


    def FILTER(data):
        if column in data.keys():
            if data[column] in values:
                return data
        return {}

    return FILTER




def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    return value


if __name__ == "__main__":
    print(test_query())

