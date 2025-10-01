__all__ = [
    "IFlippingPageCallback"
]
from abc import ABC


class IFlippingPageCallback(ABC):
    page: int