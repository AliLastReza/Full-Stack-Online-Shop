from oscar.apps.shipping import repository

from . import methods


class Repository(repository.Repository):
    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):
        available_methods = (methods.Standard(),)
        if shipping_addr and shipping_addr.country.code == 'GB':
            # Express is only available in the UK
            available_methods = (methods.Standard(), methods.Express())
        return available_methods
