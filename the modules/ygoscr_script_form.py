#-------------------------------------------------------------------------------
# ygoscr_script_form

# Placeholders are used to determine the finalized structure.
#-------------------------------------------------------------------------------

def script_formula(self):

    self.card_form = (
f'''--name_of_card
local s,id=GetID()
function s.initial_effect(c)
    --Activate
    local e1=Effect.CreateEffect(c)
    e1:SetCategory({self.effect_cat})
    e1:SetType({self.effect_typ})
    {self.effect_rge}
    {self.effect_cod}
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end
{self.effect_filter}
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.IsExistingMatchingCard({self.effect_val},tp,{self.effect_loc},{self.effect_loc},1,{self.filter_param}) end
    local sg=Duel.GetMatchingGroup({self.effect_val},tp,{self.effect_loc},{self.effect_loc},{self.filter_param})
    Duel.SetOperationInfo(0,{self.effect_cat},sg,#sg,0,0)
end
function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local sg=Duel.GetMatchingGroup({self.effect_val},tp,{self.effect_loc},{self.effect_loc},{self.filter_param})
    Duel.Destroy(sg,REASON_EFFECT)
end'''
)
