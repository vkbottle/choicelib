import typing

import importlib.util

from .order import Order


def choice_in_order(
    module_names: typing.List[str],
    order: Order = Order.TO_RIGHT,
    do_import: bool = False,
    default: typing.Optional[str] = None,
) -> typing.Union[str, typing.Any]:
    """ Finds out installed module from list based on order
    :param module_names: list of module names
    :param order: order from worst to best to be installed
    :param do_import: should module be imported
    :param default: default module name [deprecated]
    :return: module if do_import else module_name
    """
    default_name = default or module_names[0]
    installed = [
        module_name
        for module_name in module_names
        if importlib.util.find_spec(module_name) is not None
    ]
    if not installed and default is None:
        raise ModuleNotFoundError(
            "No proper module was installed. "
            "List: {}".format(", ".join(module_names))
        )

    ordered_module_name = installed[order.value] if installed else default_name
    return ordered_module_name if not do_import else __import__(ordered_module_name)
