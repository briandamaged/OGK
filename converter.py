# Converter dictionary and convert() method for 'Oh Great Knight'
import items

# Convertor dictionary contains commonly used string abbreviations for items
# and the constant (item) the string refers to.
converter = {"": False,
             "wood shield": items.wood_shield,
             "sturdy shield": items.sturdy_shield, 
             "rusty sword": items.rusty_sword,
             "battle axe": items.battle_axe, 
             "shiny sword": items.shiny_sword,
             "band-aid": items.band_aid,
             "gold ring": items.gold_ring,
             "herbenol": items.herb, 
             "first-aid": items.first_aid,
             "first aid": items.first_aid,
             "hand-me-downs": items.handmedowns,
             "hand me downs": items.handmedowns,
             "leather armor": items.leather,
             "sweet getup": items.sweet_armor,
             "sweet get-up": items.sweet_armor,
             "sweet get up": items.sweet_armor,
             "b.t.l.": items.btl,
             "btl": items.btl,
             "bear trap": items.bear_trap}

def convert(term):
    """converts item abbreviation to item variable using convertor dictionary"""
    if term in converter:
        return converter[term]
    else:
        print("That item does not exist.\a")
        return False


if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'")
    input("Press enter to exit")
