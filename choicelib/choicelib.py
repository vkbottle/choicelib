import types
import typing

import pkg_resources

from .order import Order


def choice_in_order(
        module_names: typing.List[str],
        order: Order = Order.TO_RIGHT,
        do_import: bool = False
) -> typing.Union[str, types.ModuleType]:
    """ Finds out installed module from list based on order
    :param module_names: list of module names
    :param order: order from worst to best to be installed
    :param do_import: should module be imported
    :return: module if do_import else module_name
    """
    installed = [pkg.key for pkg in pkg_resources.working_set if pkg.key in module_names]
    if not installed:
        raise ModuleNotFoundError("No required module variation was found. List: {}".format(", ".join(module_names)))

    ordered_module_name = installed[order.value]
    return ordered_module_name if not do_import else __import__(ordered_module_name)
