from baseItem import BaseItem

class Equipment(BaseItem):
    def __init__(self):
        super.__init__(self)
        self.equip_locations = list() # what body parts can equip it.
        # equippable items can be Armor, Container, or Weapon

