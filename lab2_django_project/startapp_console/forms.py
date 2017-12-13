from django import forms
import Scripts.lab2_django_project.startapp_console.models as Models

class MainFormTable(forms.Form):
    opCA_name = forms.CharField(required=True, label='Counteragent', label_suffix='',
                              widget=forms.TextInput(attrs={'readonly': True}))
    opNom_name = forms.CharField(required=True, label='Nomenclature', label_suffix='',
                             widget=forms.TextInput(attrs={'readonly': True}))
    opBRD_id = forms.CharField(required=True, label='BRD number', label_suffix='',
                             widget=forms.TextInput(attrs={'readonly': True}))
    opAC_id = forms.CharField( required=True, label='Account', label_suffix='',
                           widget=forms.TextInput(attrs={'readonly': True}))

class ACTDateSearch(forms.Form):
    acDateLeft = forms.fields.DateField(required=True, label='Start date')
    acDateRight = forms.fields.DateField(required=True, label='Finish date')


acoounts_ChoiceSet = []
acCurrency_QuerySet = Models.Accounts.objects.raw("Select acID, acCurrency from accounts group by acCurrency")
acID_QuerySet = Models.Accounts.objects.raw("Select acID from accounts group by acID")

for record in acCurrency_QuerySet:
    acoounts_ChoiceSet.append((record.acCurrency, record.acCurrency))
class ACTCurrencySearch(forms.Form):
    acCurrency = forms.ChoiceField(choices=acoounts_ChoiceSet, required=True, label='Currency')

class BRDTPriceFilter(forms.Form):
    brdPriceLeft = forms.fields.FloatField(required=True, label='Bottom price border', min_value=0, max_value=10000)
    brdPriceRight = forms.fields.FloatField(required=True, label='Top price border', min_value=0, max_value=10000)


brd_ChoiceSet = []
brdOrganization_name_QuerySet = Models.BRD.objects.raw("Select brdID, brdOrganization_name from brd group by brdOrganization_name")
brdID_QuerySet = Models.BRD.objects.raw("Select brdID from brd group by brdID")
for record in brdOrganization_name_QuerySet:
    brd_ChoiceSet.append((record.brdOrganization_name, record.brdOrganization_name))
class BRDTOrgSearch(forms.Form):
    brdOrganization_name = forms.ChoiceField(choices=brd_ChoiceSet, required=True, label='Organization')

class CATCodeSearch(forms.Form):
    caUKTZED_code = forms.CharField(required=True, label='Counteragent\'s UKTZED_code')


counteragents_ChoiceSet = []
caScheme_QuerySet = Models.Counteragents.objects.raw("Select caName, caScheme from counteragents group by caScheme")
caName_QuerySet = Models.Counteragents.objects.raw("Select caName from counteragents group by caName")
for record in caScheme_QuerySet:
    counteragents_ChoiceSet.append((record.caScheme, record.caScheme))
class CATSchemeSearch(forms.Form):
    caScheme = forms.ChoiceField(choices=counteragents_ChoiceSet, required=True, label='Scheme')


nomenclatures_ChoiceSet = []
nomMU_QuerySet = Models.Nomenclatures.objects.raw("Select nomName, nomMU from nomenclatures group by nomMU")
nomName_QuerySet = Models.Nomenclatures.objects.raw("Select nomName from nomenclatures group by nomName")
for record in nomMU_QuerySet:
    nomenclatures_ChoiceSet.append((record.nomMU, record.nomMU))
class NOMTMUSearch(forms.Form):
    nomMU = forms.ChoiceField(choices=nomenclatures_ChoiceSet, required=True, label='Measure units')

class NOMTFTPhraseSearch(forms.Form):
    nomFTPhraseSearchResult = forms.CharField(required=True, label='Contains the following phrase', max_length=40)

class NOMTFTWordSearch(forms.Form):
    nomFTWordSearchResult = forms.CharField(required=True, label='Doesn\'t containt the following word', max_length=14)

class AccountsForm(forms.Form):
    acID = forms.CharField(required=True, label='acID ',
                              widget=forms.TextInput(attrs={'readonly': True}))
    acDate = forms.DateField(required=True, label='acDate ',
                           widget=forms.TextInput(attrs={'readonly': True}))
    acOperation_type = forms.CharField(required=True, label='acOperation_type ',
                              widget=forms.TextInput(attrs={'readonly': True}))
    acPrice = forms.FloatField(required=True, label='acPrice ',
                              widget=forms.TextInput(attrs={'readonly': True}))
    acCurrency = forms.CharField(required=True, label='acCurrency ',
                              widget=forms.TextInput(attrs={'readonly': True}))
    acGoods_type = forms.CharField(required=True, label='acGoods_type ',
                              widget=forms.TextInput(attrs={'readonly': True}))

class BRDForm(forms.Form):
    brdID = forms.CharField(required=True, label='brdID ',
                           widget=forms.TextInput(attrs={'readonly': True}))
    brdPrice = forms.FloatField(required=True, label='brdPrice ',
                               widget=forms.TextInput(attrs={'readonly': True}))
    brdCurrency = forms.CharField(required=True, label='brdCurrency ',
                               widget=forms.TextInput(attrs={'readonly': True}))
    brdOperation_types = forms.CharField(required=True, label='brdOperation_types ',
                                       widget=forms.TextInput(attrs={'readonly': True}))
    brdOrganization_name = forms.CharField(required=True, label='brdOrganization_name ',
                                 widget=forms.TextInput(attrs={'readonly': True}))

class CounteragentsForm(forms.Form):
    caName = forms.CharField(required=True, label='caID ',
                            widget=forms.TextInput(attrs={'readonly': True}))
    caUKTZED_code = forms.CharField(required=True, label='caUKTZED_code ',
                            widget=forms.TextInput(attrs={'readonly': True}))
    caScheme = forms.CharField(required=True, label='caScheme ',
                            widget=forms.TextInput(attrs={'readonly': True}))
    caITC = forms.CharField(required=True, label='caITC ',
                            widget=forms.TextInput(attrs={'readonly': True}))

class NomenclaturesForm(forms.Form):
    nomName = forms.CharField(required=True, label='nomName ',
                              widget=forms.TextInput(attrs={'readonly': True}))
    nomVendore_code = forms.DateField(required=True, label='nomVendore_code ',
                           widget=forms.TextInput(attrs={'readonly': True}))
    nomVAT_rate = forms.CharField(required=True, label='nomVAT_rate ',
                              widget=forms.TextInput(attrs={'readonly': True}))
    nomUKTZED_code = forms.CharField(required=True, label='nomUKTZED_code ',
                                widget=forms.TextInput(attrs={'readonly': True}))
    nomStock_type = forms.CharField(required=True, label='nomStock_type ',
                              widget=forms.TextInput(attrs={'readonly': True}))
    description = forms.CharField(required=True, label='Description ',
                                  widget=forms.Textarea(attrs={'readonly': True, 'rows': 3, 'cols': 20}))


acoounts_ChoiceSet = []
brd_ChoiceSet = []
nomenclatures_ChoiceSet = []
counteragents_ChoiceSet = []
for record in acID_QuerySet:
    acoounts_ChoiceSet.append((record.acID, record.acID))
for record in brdID_QuerySet:
    brd_ChoiceSet.append((record.brdID, record.brdID))
for record in nomName_QuerySet:
    nomenclatures_ChoiceSet.append((record.nomName, record.nomName))
for record in caName_QuerySet:
    counteragents_ChoiceSet.append((record.caName, record.caName))
class getFormTableTemplates(forms.Form):
    opCA_name = forms.ChoiceField(choices=counteragents_ChoiceSet, required=True, label='CA_name')
    opNom_name = forms.ChoiceField(choices=nomenclatures_ChoiceSet, required=True, label='Nom_name')
    opBRD_id = forms.ChoiceField(choices=brd_ChoiceSet, required=True, label='BRD_id')
    opAC_id = forms.ChoiceField(choices=acoounts_ChoiceSet, required=True, label='Account_id')

class AccountsTable():
    acDate = "acDate"
    acCurrency = "acCurrency"
    acTable = "accounts"
    acColumns = ["acID", "acDate", "acOperation_type", "acPrice", "acCurrency", "acGoods_type"]

class BRDTable():
    brdPrice = "brdPrice"
    brdOrgname = "brdOrganization_name"
    brdTable = "brd"
    brdColumns = ["brdID", "brdPrice", "brdCurrency", "brdOperation_types", "brdOrganization_name"]

class CounteragentsTable():
    caCode = "caUKTZED_code"
    caScheme = "caScheme"
    caTable = "counteragents"
    caColumns = ["caName", "caUKTZED_code", "caScheme", "caITC"]

class NomenclaturesTable():
    nomMU = "nomMU"
    nomTable = "nomenclatures"
    nomColumns = ["nomName", "nomVendore_code", "nomMU", "nomVAT_rate", "nomUKTZED_code", "nomStock_type", "description"]
