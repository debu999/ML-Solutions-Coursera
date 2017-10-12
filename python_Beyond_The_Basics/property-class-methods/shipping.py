"""Shipping container class for usage"""

import iso6346
from pprint import pprint as pp
import time


class ShippingContainer:
    next_serial = 1337
    next_serial_cls = 12321

    HEIGHT_FT = 10
    WIDTH_FT = 9.2

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.length_ft = length_ft
        self.serial = ShippingContainer._get_next_serial()
        self.serial_cls = ShippingContainer._get_next_serial_cls()
        # self.bic = ShippingContainer._make_bic_code(owner_code=owner_code,
        #                                             serial=ShippingContainer._get_next_serial_cls())
        ####IF the object is from child class it will execute the _make_bic_code for child method
        ###Thus, facilitate the polymorphic behaviour of the function.
        #### If a static method is inherited then its required in init not to reference from the parent
        ###class to facilitate correct working.
        self.bic = self._make_bic_code(owner_code=owner_code,
                                       serial=ShippingContainer._get_next_serial_cls())

    @classmethod
    def _get_next_serial_cls(cls):
        result = cls.next_serial_cls
        cls.next_serial_cls += 1
        return result

    @classmethod
    def create_shipping_without_obj(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_shipping_with_obj(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    @property
    def volume_ft3(self):
        # return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft
        # Use stop using the property see derived class implementation
        return self._calc_Volume()

    def _calc_Volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


c1 = ShippingContainer("ABC", 20, "PQR")
print(ShippingContainer.next_serial)

c2 = ShippingContainer("DEF", 30, "STU")

print(c1.serial, c2.serial, ShippingContainer.next_serial, c2.next_serial, c1.serial_cls,
      c2.serial_cls, ShippingContainer.next_serial_cls, )

c3 = ShippingContainer.create_shipping_without_obj("PRA", 23)

c4 = ShippingContainer.create_shipping_with_obj("DEB", 22, ["Gold and Silver", "SGD $2000000", "INR Rs100000000000"])

print(c3.serial, c3.serial_cls, ShippingContainer.next_serial_cls, ShippingContainer.next_serial,
      c3.contents, c3.owner_code,
      "\n",
      c4.serial, c4.serial_cls, ShippingContainer.next_serial_cls, ShippingContainer.next_serial,
      c4.contents, c4.owner_code)
print(type(c4.bic))
pp([c4.bic, c3.bic, c2.bic, c1.bic])

print(c4.bic, c3.bic, c2.bic, c1.bic)


class RefrigeratorShippingContainer(ShippingContainer):
    MAX_CELSIUS = 3.5

    FRIDGE_VOLUME_FT3 = 200

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')

    @classmethod
    def _c_to_f(cls, celsius):
        return celsius * 9 / 5 + 32

    @classmethod
    def _f_to_c(cls, farenheit):
        return (farenheit - 32) * 5 / 9

    def __repr__(self):
        return "###".join([str(val) for val in [super(RefrigeratorShippingContainer, self).next_serial,
                                                super(RefrigeratorShippingContainer, self).next_serial_cls,
                                                self.owner_code,
                                                self.bic,
                                                self.contents,
                                                self.serial,
                                                self.serial_cls,
                                                self.next_serial_cls,
                                                self.next_serial,
                                                self._celsius,
                                                self.MAX_CELSIUS]])

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        # if celsius > RefrigeratorShippingContainer.MAX_CELSIUS:
        #     raise ValueError("".join(
        #         ["Refrigeration Temperature cant be more than :", str(RefrigeratorShippingContainer.MAX_CELSIUS)]))
        self.celsius = celsius
        # self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    #
    #
    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)


    def _set_celsius(self, value):
        if value > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("".join(
                ["Refrigeration Temperature cant be more than :", str(RefrigeratorShippingContainer.MAX_CELSIUS)]))
        self._celsius = value
        time.sleep(0.3)
        pp(" ".join(["Temperature set to:", str(value)]))

    @property
    def farenheit(self):
        return RefrigeratorShippingContainer._c_to_f(self.celsius)

    @farenheit.setter
    def farenheit(self, value):
        self.celsius = RefrigeratorShippingContainer._f_to_c(value)

    # @property
    """Remove the @property and overide the function as normal function"""
    # def volume_ft3(self):
    def _calc_Volume(self):
        # return (self.length_ft * ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT - RefrigeratorShippingContainer.FRIDGE_VOLUME_FT3)
        # return super().volume_ft3 - RefrigeratorShippingContainer.FRIDGE_VOLUME_FT3
        return super()._calc_Volume() - RefrigeratorShippingContainer.FRIDGE_VOLUME_FT3
        # @staticmethod
        # def cel_2 frs


# r1 = RefrigeratorShippingContainer.create_shipping_with_obj(None, None, 2.0, owner_code="DEB", items=["Meat", "Prawns", "Metals", "Stocks",
#                                            "Vegetables"])
# pp(r1)
r1 = RefrigeratorShippingContainer.create_shipping_with_obj("DEB", 30, ["Meat", "Prawns", "Metals", "Stocks",
                                                                        "Vegetables"], celsius=3.1)
print(r1)
r1.celsius = 1.5
pp([r1.celsius, r1.farenheit])
r1.farenheit = 32
pp([r1.celsius, r1.farenheit])
pp([r1.volume_ft3])


class HeatedRefrigeratedShippingContainer(RefrigeratorShippingContainer):
    MIN_CELSIUS = -20.0


    def _set_celsius(self, value):
        time.sleep(0.4)
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature is too cold. MIN Temp allowd is "+str(HeatedRefrigeratedShippingContainer.MIN_CELSIUS))
        super()._set_celsius(value)

    # @RefrigeratorShippingContainer.celsius.setter
    # def celsius(self, value):
    #     time.sleep(0.4)
    #     # if not (HeatedRefrigeratedShippingContainer.MIN_CELSIUS
    #     #             <= value
    #     #             <= RefrigeratorShippingContainer.MAX_CELSIUS):
    #     #     msg = "".join(['Temperature out of range. Range is between', str(
    #     #         HeatedRefrigeratedShippingContainer.MIN_CELSIUS), " and ", str(
    #     #         RefrigeratorShippingContainer.MAX_CELSIUS)])
    #     #     pp(msg)
    #     #     raise ValueError(msg)
    #     if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
    #         raise ValueError("Temperature is too cold. MIN Temp allowd is "+str(HeatedRefrigeratedShippingContainer.MIN_CELSIUS))
    #
    #     # Doesnot work as usual since the super().celsius implementation is not available to child class
    #     # super().celsius = value
    #     # Solution:
    #     RefrigeratorShippingContainer.celsius.fset(self, value)
    #

r2 = HeatedRefrigeratedShippingContainer.create_shipping_with_obj("DEB", 40.5, ["Carrot", "Brinjal", "Coconut"],
                                                                  celsius=2)

pp(r2.celsius)
r2.celsius = -15
pp(r2.celsius)

r2.farenheit = -4
pp(r2.celsius)
