import reprlib
from pprint import pprint as pp
import inspect
import sys

import itertools

import time
from sorted_set import SortedSet as
from project.python_Beyond_The_Basics.sorted_set import SortedSet as SortedSet

def dump(obj):
    pp("Type")
    pp("====")
    pp(type(obj))
    pp("")

    pp("Documentation")
    pp("="*len("Documentation"))
    pp(inspect.getdoc(obj))
    pp("")

    pp("Attributes")
    pp("="*len("Attributes"))
    all_attr_names = SortedSet(dir(obj))
    method_names = SortedSet(filter(lambda attr_name: callable(getattr(obj, attr_name)), all_attr_names))
    assert method_names <= all_attr_names
    attr_names = all_attr_names - method_names
    attr_name_and_values = [(name, reprlib.repr(getattr(obj, name))) for name in attr_names ]
    print_table(attr_name_and_values, "Name", "Values")

    pp("")

    pp("Methods")
    pp("=" * len("Methods"))
    methods = (getattr(obj, method_name) for method_name in method_names)
    methods_name_and_doc = [(full_sig(method), brief_doc(method)) for method in methods]
    print_table(methods_name_and_doc, "Name", "Values")
    pp("")


def full_sig(method):
    try:
        return method.__name__ + str(inspect.signature(method))
    except ValueError:
        return method.__name__ + "(...)"


def brief_doc(obj):
    doc = obj.__doc__
    if doc is not None:
        lines = doc.splitlines()
        if len(lines)> 0:
            return lines[0]
    return ""

def print_table(rows_of_columns, *headers):
    num_cols = len(rows_of_columns[0])
    num_headers = len(headers)
    if num_headers != num_cols:
        raise TypeError("Expected {} header "
                        "Arguments got {}".format(num_cols, num_headers))

    rows_of_columns_with_header = itertools.chain([headers], rows_of_columns)
    column_of_rows = list(zip(*rows_of_columns_with_header))
    column_widths = [max(map(len, column)) for column in column_of_rows]
    column_specs = ("{{:{w}}}".format(w=width) for width in column_widths)
    format_spec = " ".join(column_specs)
    print(format_spec.format(*headers))
    rules = ("-" * width for width in column_widths)
    print(format_spec.format(*rules))
    for rows in rows_of_columns:
        print(format_spec.format(*rows))


if __name__ == "__main__":
    c = 12
    dump(c)