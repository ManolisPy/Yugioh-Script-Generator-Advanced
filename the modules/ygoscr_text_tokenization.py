#-------------------------------------------------------------------------------
# ygoscr_text_tokenization

# NLTK is used to tokenize the input, making it easier to work on.
# <effect_main>, <effect_cost_target> and <effect_cost_target> may be moved
# to a different module in the future.
#-------------------------------------------------------------------------------

from nltk.tokenize import RegexpTokenizer
import re
import string

import ygoscr_script_dictionaries



pattern_repl = ygoscr_script_dictionaries.dict_replacements()


def pattern_function(match):

    return pattern_repl[match.group(0)]


def text_token_list(self, text_target):
    """
    The method makes the input easier to work on by doing the following,
    in the order below:
    1. Changing all letters to lowercase.
    2. Replacing key parts with simplified versions if necessary,
       with the help of a dictionary.
    3. Tokenizing the sentence with a regex rule, based on a group of
       punctuation marks.
    4. Grouping the tokenized sentence according to those marks.
    5. Working on each group separately.
    """

    text_clean = re.sub(r"\'", "", text_target.lower())

    testing = re.compile("|".join(re.escape(k) for k in pattern_repl))
    cleaned_test_text = testing.sub(pattern_function, text_clean)

    test_regex = RegexpTokenizer('(?<=[;:.,])', gaps = True)
    regexlist = test_regex.tokenize(cleaned_test_text)

    tokenizer_clean = RegexpTokenizer(r'\w+')
    templist = []
    for i in regexlist:
        temp_i = tokenizer_clean.tokenize(i)
        templist.append(temp_i)
        #templist.append(i.split())

    # In one of their basic forms, the cards' effects consist of up to
    # four parts, in the following order:
    # Activation condition -> cost to use -> application target -> action.
    # There's always an action, the rest are optional.
    # Each part is handled separately.
    effect_parts = len(templist)
    effect_main(self, templist[effect_parts-1])
    if effect_parts in [2,3]:
        effect_cost_target(self, templist[effect_parts-2])
        if effect_parts == 3:
            effect_condition(self, templist[effect_parts-3])


def effect_main(self, mtext):

    self.effect_cat = ""
    self.effect_val = ""
    self.effect_loc = ""
    self.effect_typ = ""
    self.effect_cod = ""
    self.effect_rge = ""
    self.effect_filter = "function s.filter(c)\n    return "

    # Filters aren't always required. filter_ctrl checks whether one is needed,
    # adding it to the script.
    filter_ctrl = False
    # self.filter_param is one of the last variables in some methods in the scripts.
    # It indicates the presence or absence of a filter and is typically labeled
    # as "nil", "c" or "e:GetHandler()".
    self.filter_param = ""

    card_type = self.corecardtype.currentText()
    self.effect_err_msg = ("The script cannot be created due to the"
                            " following error(s):\n")

    try:
        self.effect_cat = self.effect_category[mtext[0]]
        self.effect_val = self.effect_validity[mtext[0]]
        for location_type in ['monsters', 'spells_traps']:
            if location_type in mtext:
                self.effect_loc = self.effect_location[location_type]
                if location_type == 'spells_traps':
                    self.effect_filter += "c:IsSpellTrap()\nend"
                    self.effect_val = "s.filter"
                    filter_ctrl = True
                    self.filter_param = "e:GetHandler()"
                else:
                    self.filter_param = "nil"
        if not self.effect_loc:
            self.effect_err_msg += ("\n- Invalid syntax or key word(s)"
                                    " missing from the card's effect.")
            self.effect_error = True
    except:
        self.effect_err_msg += ("\n- Invalid syntax or key word(s)"
                                " missing from the card's effect.")
        self.effect_error = True
    try:
        self.effect_typ = self.effect_type[card_type]
        self.effect_cod = self.effect_code[card_type]
        self.effect_rge = self.effect_range[card_type]
    except:
        self.effect_err_msg += "\n- No type of card selected (Monster/Spell/Trap)."
        self.effect_error = True
    if filter_ctrl == False:
        self.effect_filter = ""

def effect_cost_target(self, cttext):
    pass


def effect_condition(self, ctext):
    pass
