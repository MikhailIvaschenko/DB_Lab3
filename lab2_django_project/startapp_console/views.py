from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.forms import formset_factory

import re
import Scripts.lab2_django_project.startapp_console.database as Database
import Scripts.lab2_django_project.startapp_console.forms as FormClasses
data = None
previousArgs = []

mainConnector = Database.Connector()

#methods' declarations
def resetData():
    global data
    global mainConnector
    data = mainConnector.getFormsetData()

def getRevertedStatus(currentStatus):
    if(currentStatus == "OFF"):
        return "ON"
    else:
        return "OFF"

def showMainTable(request):
    global data
    resetData()

    formSetBuilder = formset_factory(FormClasses.MainFormTable, extra=(len(data) - 3) / 3) #automatically collects the table : template=MainFormTable; count = extra=(len(data) - 3) / 3)
    filledFormSet = formSetBuilder(data)
    currentUpdateStatus = "Turn update trigger " + getRevertedStatus(Database.Models.TriggerManager.objects.get().updateTriggerStatus.__str__())
    currentInsertStatus = "Turn insert trigger " + getRevertedStatus(Database.Models.TriggerManager.objects.get().insertTriggerStatus.__str__())
    currentDeleteStatus = "Turn delete trigger " + getRevertedStatus(Database.Models.TriggerManager.objects.get().deleteTriggerStatus.__str__())
    formResponse = {'Formset':filledFormSet,
                    'updateText': currentUpdateStatus,
                    'insertText': currentInsertStatus,
                    'deleteText': currentDeleteStatus,}
    return render(request, 'Table.html', formResponse) #return page template filled with formResponse

def showSearchTable(request):
    acDSform = FormClasses.ACTDateSearch() #filter data between two values => l.w. task
    acCSform = FormClasses.ACTCurrencySearch() #get the records with the set currency
    acPFform = FormClasses.BRDTPriceFilter() #filter by price values
    brdOSform = FormClasses.BRDTOrgSearch() #get the records with the set organization
    caCSform = FormClasses.CATCodeSearch() #get the records with the set code
    caSSform = FormClasses.CATSchemeSearch() #get the records with the set scheme
    nomMUSform = FormClasses.NOMTMUSearch() #get the records with the set measure units
    nomFTSPhraseForm = FormClasses.NOMTFTPhraseSearch() #full text serach by a phrase => l.w. task
    nomFTSWordForm = FormClasses.NOMTFTWordSearch() #full text serach by a word => l.w. task

    return render(request, 'Search.html', {'form0': acDSform, 'form1': acCSform, 'form2': acPFform, 'form3': brdOSform,
                                           'form4': caCSform, 'form5': caSSform, 'form6': nomMUSform, 'form7': nomFTSPhraseForm,
                                           'form8': nomFTSWordForm})

def acDateSearch(request):
    rows = Database.Models.Accounts.objects.filter(acDate__range = (request.POST["acDateLeft"], request.POST["acDateRight"]))
    rowsDictionary = mainConnector.getQueryDictionary_Accounts(rows)

    formSetBuilder = formset_factory(FormClasses.AccountsForm, extra=(len(rowsDictionary) - 3) / 3)
    filledFormSet = formSetBuilder(rowsDictionary)

    response = {}
    response['Formset'] = filledFormSet
    return render(request, 'SimpleTable.html', response)

def acCurrencySearch(request):
    rows = Database.Models.Accounts.objects.filter(acCurrency__exact = request.POST["acCurrency"])
    rowsDictionary = mainConnector.getQueryDictionary_Accounts(rows)

    formSetBuilder = formset_factory(FormClasses.AccountsForm, extra=(len(rowsDictionary) - 3) / 3)
    filledFormSet = formSetBuilder(rowsDictionary)

    response = {}
    response['Formset'] = filledFormSet
    return render(request, 'SimpleTable.html', response)

def brdPriceFilter(request):
    rows = Database.Models.BRD.objects.filter(brdPrice__range = (request.POST["brdPriceLeft"], request.POST["brdPriceRight"]))
    rowsDictionary = mainConnector.getQueryDictionary_BRD(rows)

    print(rowsDictionary.__str__())

    formSetBuilder = formset_factory(FormClasses.BRDForm, extra=(len(rowsDictionary) - 3) / 3)
    filledFormSet = formSetBuilder(rowsDictionary)

    response = {}
    response['Formset'] = filledFormSet
    return render(request, 'SimpleTable.html', response)

def brdOrgSearch(request):
    rows = Database.Models.BRD.objects.filter(brdOrganization_name__exact = request.POST["brdOrganization_name"])
    rowsDictionary = mainConnector.getQueryDictionary_BRD(rows)

    formSetBuilder = formset_factory(FormClasses.BRDForm, extra=(len(rowsDictionary) - 3) / 3)
    filledFormSet = formSetBuilder(rowsDictionary)

    response = {}
    response['Formset'] = filledFormSet
    return render(request, 'SimpleTable.html', response)

def caCodeSearch(request):
    rows = Database.Models.Counteragents.objects.filter(caUKTZED_code__exact = request.POST["caUKTZED_code"])
    rowsDictionary = mainConnector.getQueryDictionary_Counteragents(rows)

    formSetBuilder = formset_factory(FormClasses.CounteragentsForm, extra=(len(rowsDictionary) - 3) / 3)
    filledFormSet = formSetBuilder(rowsDictionary)

    response = {}
    response['Formset'] = filledFormSet
    return render(request, 'SimpleTable.html', response)

def caSchemeSearch(request):
    rows = Database.Models.Counteragents.objects.filter(caScheme__exact = request.POST["caScheme"])
    rowsDictionary = mainConnector.getQueryDictionary_Counteragents(rows)

    formSetBuilder = formset_factory(FormClasses.CounteragentsForm, extra=(len(rowsDictionary) - 3) / 3)
    filledFormSet = formSetBuilder(rowsDictionary)

    response = {}
    response['Formset'] = filledFormSet
    return render(request, 'SimpleTable.html', response)

def nomMUSearch(request):
    rows = Database.Models.Nomenclatures.objects.filter(nomMU__exact = request.POST["nomMU"])
    rowsDictionary = mainConnector.getQueryDictionary_Nomenclatures(rows)

    formSetBuilder = formset_factory(FormClasses.NomenclaturesForm, extra=(len(rowsDictionary) - 3) / 3)
    filledFormSet = formSetBuilder(rowsDictionary)

    response = {}
    response['Formset'] = filledFormSet
    return render(request, 'SimpleTable.html', response)

def nomFTWordSearch(request):
    rows = Database.Models.Nomenclatures.objects.raw(
        "SELECT * FROM nomenclatures WHERE NOT MATCH (Description) AGAINST (\'+ \"" + request.POST[
            "nomFTWordSearchResult"] + "\"' IN BOOLEAN MODE)")



    rowsDictionary = mainConnector.getQueryDictionary_Nomenclatures(rows)

    formSetBuilder = formset_factory(FormClasses.NomenclaturesForm, extra=(len(rowsDictionary) - 3) / 3)
    filledFormSet = formSetBuilder(rowsDictionary)

    response = {}
    response['Formset'] = filledFormSet
    return render(request, 'SimpleTable.html', response)
    #return HttpResponse(Query.__str__())

def nomFTPhraseSearch(request):
    rows = Database.Models.Nomenclatures.objects.raw(
        "SELECT * FROM nomenclatures WHERE MATCH (Description) AGAINST (\'\"" + request.POST[
            "nomFTPhraseSearchResult"] + "\"' IN BOOLEAN MODE)")
    rowsDictionary = mainConnector.getQueryDictionary_Nomenclatures(rows)

    formSetBuilder = formset_factory(FormClasses.NomenclaturesForm, extra=(len(rowsDictionary) - 3) / 3)
    filledFormSet = formSetBuilder(rowsDictionary)

    response = {}
    response['Formset'] = filledFormSet
    return render(request, 'SimpleTable.html', response)

def comeBackToSTwithResult(request):
    return redirect('http://127.0.0.1:8000/MainFormTable/SearchMainTable/')

def collectDataForEditting(request, Key):
    global previousArgs
    if "form-" + Key + "-opCA_name" in request.POST:
        opCA_name = request.POST["form-" + Key + "-opCA_name"]
    if "form-" + Key + "-opNom_name" in request.POST:
        opNom_name = request.POST["form-" + Key + "-opNom_name"]
    if "form-" + Key + "-opBRD_id" in request.POST:
        opBRD_id = request.POST["form-" + Key + "-opBRD_id"]
    if "form-" + Key + "-opAC_id" in request.POST:
        opAC_id = request.POST["form-" + Key + "-opAC_id"]
    previousArgs = [ opCA_name ,opNom_name, opBRD_id, opAC_id]
    SearchMainTable = FormClasses.getFormTableTemplates({'opCA_name': opCA_name, 'opNom_name': opNom_name, 'opBRD_id': opBRD_id, 'opAC_id': opAC_id})
    return render(request, 'CommitEditting.html', {'form': SearchMainTable})
def collectDataForAdding(request):
    SearchMainTable = FormClasses.getFormTableTemplates({'opCA_name': '', 'opNom_name': '', 'opBRD_id': '', 'opAC_id': ''})
    return render(request, 'CommitAdding.html', {'form': SearchMainTable})
def collectDataForDeleting(request, Key):
    global data
    global mainConnector
    updateDataBuffer = ["", "", "", ""]
    if "form-" + Key + "-opCA_name" in request.POST:
        opCA_name = request.POST["form-" + Key + "-opCA_name"]
    if "form-" + Key + "-opNom_name" in request.POST:
        opNom_name = request.POST["form-" + Key + "-opNom_name"]
    if "form-" + Key + "-opBRD_id" in request.POST:
        opBRD_id = request.POST["form-" + Key + "-opBRD_id"]
    if "form-" + Key + "-opAC_id" in request.POST:
        opAC_id = request.POST["form-" + Key + "-opAC_id"]

    updateDataBuffer = [opCA_name ,  opNom_name ,  opBRD_id ,  opAC_id ]

    Database.Models.Operations.objects.filter(opCA_name__exact=updateDataBuffer[0], opNom_name__exact=updateDataBuffer[1],
                                              opBRD_id__exact=updateDataBuffer[2], opAC_id__exact=updateDataBuffer[3]).delete()

    resetData()
    return redirect('http://127.0.0.1:8000/MainFormTable/')

def commitEditting(request):
    global data
    global previousArgs
    global mainConnector
    updateDataBuffer = ["", "", "", ""]
    for field in request.POST:
        if re.match("opCA_name",field):
            updateDataBuffer[0] = request.POST[field]
        if re.match("opNom_name", field):
            updateDataBuffer[1] =  request.POST[field]
        if re.match("opBRD_id", field):
            updateDataBuffer[2] =  request.POST[field]
        if re.match("opAC_id", field):
            updateDataBuffer[3] =  request.POST[field]

    Database.Models.Operations.objects.filter(opCA_name__exact=previousArgs[0], opNom_name__exact=previousArgs[1], opBRD_id__exact=previousArgs[2],
                                      opAC_id__exact=previousArgs[3]).update(opCA_name=updateDataBuffer[0],
                                      opNom_name=updateDataBuffer[1], opBRD_id=updateDataBuffer[2], opAC_id=updateDataBuffer[3])

    resetData()
    previousArgs = []
    return redirect('http://127.0.0.1:8000/MainFormTable/')
    #return HttpResponse(q.__str__())
def commitAdding(request):
    global data
    global mainConnector
    updateDataBuffer = ["", "", "", ""]
    for field in request.POST:
        if re.match("opCA_name",field):
            updateDataBuffer[0] = Database.Models.Counteragents.objects.get(caName = request.POST[field])
        if re.match("opNom_name", field):
            updateDataBuffer[1] = Database.Models.Nomenclatures.objects.get(nomName = request.POST[field])
        if re.match("opBRD_id", field):
            updateDataBuffer[2] = Database.Models.BRD.objects.get(brdID = request.POST[field])
        if re.match("opAC_id", field):
            updateDataBuffer[3] = Database.Models.Accounts.objects.get(acID = request.POST[field])

    Database.Models.Operations.objects.create(opCA_name=updateDataBuffer[0], opNom_name=updateDataBuffer[1],
                                          opBRD_id=updateDataBuffer[2], opAC_id=updateDataBuffer[3])
    resetData()
    return redirect('http://127.0.0.1:8000/MainFormTable/')

def detectButton(request):
    for s in request.POST:
        if s.startswith("edit"):
            return collectDataForEditting(request, s[4:])
        if s.startswith("delete"):
            return collectDataForDeleting(request, s[6:])
        if s.startswith("add"):
            return collectDataForAdding(request)
        if s.startswith("search"):
            return redirect('http://127.0.0.1:8000/MainFormTable/SearchMainTable/')
        if s.startswith("resetUpdate"):
            obj = Database.Models.TriggerManager.objects.get().updateTriggerStatus
            if obj == "ON":
                Database.Models.TriggerManager.objects.update(updateTriggerStatus="OFF")
            else:
                Database.Models.TriggerManager.objects.update(updateTriggerStatus="ON")

            return redirectToMT(request)
        if s.startswith("resetInsert"):
            obj = Database.Models.TriggerManager.objects.get().insertTriggerStatus
            if obj == "ON":
                Database.Models.TriggerManager.objects.update(insertTriggerStatus="OFF")
            else:
                Database.Models.TriggerManager.objects.update(insertTriggerStatus="ON")

            return redirectToMT(request)
        if s.startswith("resetDelete"):
            obj = Database.Models.TriggerManager.objects.get().deleteTriggerStatus
            if obj == "ON":
                Database.Models.TriggerManager.objects.update(deleteTriggerStatus="OFF")
            else:
                Database.Models.TriggerManager.objects.update(deleteTriggerStatus="ON")

            return redirectToMT(request)

def redirectToMT(request):
    return redirect('http://127.0.0.1:8000/MainFormTable/')