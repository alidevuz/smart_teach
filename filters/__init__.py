from loader import dp
from . import shaxsiy
from .shaxsiy import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)