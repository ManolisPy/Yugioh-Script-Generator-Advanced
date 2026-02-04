#-------------------------------------------------------------------------------
# ygoscr_script_dictionaries
#
#
#-------------------------------------------------------------------------------

def dictionaries(self):
    #Some depend on words from the card effect, others on general variables.

    self.effect_category = {
    'destroy': "CATEGORY_DESTROY",
    'return': "CATEGORY_TOHAND"
    #'shuffle': something,
    #'banish': something
    }

    self.effect_type = {
    'Spell': "EFFECT_TYPE_ACTIVATE",
    'Trap': "EFFECT_TYPE_ACTIVATE",
    'Monster': "EFFECT_TYPE_IGNITION"
    }

    self.effect_code = {
    'Spell': "e1:SetCode(EVENT_FREE_CHAIN)",
    'Trap': "e1:SetCode(EVENT_FREE_CHAIN)",
    'Monster': ""
    #something: "EVENT_TO_GRAVE"
    }

    self.effect_range ={
    'Monster': "e1:SetRange(LOCATION_MZONE)",
    'Spell': "",
    'Trap': ""
    }

    self.effect_location = {
    'monsters': "LOCATION_MZONE",
    'spells_traps': "LOCATION_ONFIELD"
    }

    self.effect_validity = {
    'destroy': "aux.TRUE"
    #something: "Card.IsAbleToHand",
    #something: "Card.IsFaceup"
    }


def dict_replacements():
    """
    Not everyone is familiar with the latest patterns in writing card effects.
    Some parts can be written in more than one ways.
    Therefore, to make use of single strings throughout the program,
    this method replaces such parts.
    """

    pattern_replacements = {
    "your opponent has on the field": "your_opponent_controls",
    "on your opponents side of the field": "your_opponent_controls",

    "on your field": "you_control",
    "on your side of the field": "you_control",

    "on both sides of the field": "on_the_field",
    "on the field": "on_the_field",

    "monster cards": "monsters",

    "spell and trap cards": "spells_traps",
    "spells and traps": "spells_traps",
    "spells/traps": "spells_traps"
    }

    return pattern_replacements.copy()
