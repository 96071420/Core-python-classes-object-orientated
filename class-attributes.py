from _typeshed import Self


class ShippingContainer:

 next_serial =13337
 

 def __init__(self, owner_code, contents):
     self.owner_code = owner_code
     self.contents = contents
     self.serial = Self.next_serial
     ShippingContainer.next_serial += 1

     


