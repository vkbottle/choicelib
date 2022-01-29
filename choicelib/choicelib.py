import typing
from importlib import import_module
from importlib.util import find_spec

from typing_extensions import Literal

from .order import Order


@typing.overload
def choice_in_order(
    module_names: typing.List[str],
    order: Order = Order.TO_RIGHT,
    do_import: Literal[True] = ...,
    default: typing.Optional[str] = None,
) -> typing.Any:
    ...


@typing.overload
def choice_in_order(
    module_names: typing.List[str],
    order: Order = Order.TO_RIGHT,
    do_import: Literal[False] = ...,
    default: typing.Optional[str] = None,
) -> str:
    ...


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
        if find_spec(module_name) is not None
    ]
    if not installed and default is None:
        raise ModuleNotFoundError(
            "No proper module was installed. "
            "List: {}".format(", ".join(module_names))
        )

    ordered_module_name = installed[order.value] if installed else default_name
    return ordered_module_name if not do_import else import_module(ordered_module_name)
