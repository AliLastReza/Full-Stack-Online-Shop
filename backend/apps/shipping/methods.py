from decimal import Decimal as D

from oscar.apps.shipping import methods


class Standard(methods.FixedPrice):
    code = "standard"
    name = "Standard shipping"
    charge_excl_tax = D("5.00")


class Express(methods.FixedPrice):
    code = "express"
    name = "Express shipping"
    charge_excl_tax = D("10.00")
