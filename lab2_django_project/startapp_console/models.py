from django.db import models

class Accounts(models.Model):
    acID = models.CharField(primary_key=True, max_length=30)
    acDate = models.DateField()
    acOperation_type = models.CharField(max_length=30)
    acPrice = models.FloatField()
    acCurrency = models.CharField(max_length=30)
    acGoods_type = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.acID, self.acDate.__str__(), self.acOperation_type, self.acPrice.__str__(), self.acCurrency, self.acGoods_type)

    class Meta:
        app_label='startapp_console'
        db_table = 'accounts'
        managed = False

class BRD(models.Model):
    brdID = models.CharField(primary_key=True, max_length=30)
    brdPrice = models.FloatField()
    brdCurrency = models.CharField(max_length=30)
    brdOperation_types = models.CharField(max_length=30)
    brdOrganization_name = models.CharField(max_length=40)

    def __str__(self):
        return "%s %s %s %s %s" % (self.brdID, self.brdPrice.__str__(), self.brdCurrency, self.brdOperation_types, self.brdOrganization_name)

    class Meta:
        app_label='startapp_console'
        db_table = 'brd'
        managed = False

class Counteragents(models.Model):
    caName = models.CharField(primary_key=True, max_length=30)
    caUKTZED_code = models.CharField(max_length=30)
    caScheme = models.CharField(max_length=30)
    caITC = models.FloatField()

    def __str__(self):
        return "%s %s %s %s" % (self.caName, self.caUKTZED_code, self.caScheme, self.caITC.__str__())

    class Meta:
        app_label='startapp_console'
        db_table = 'counteragents'
        managed = False

class Nomenclatures(models.Model):
    nomName = models.CharField(primary_key=True, max_length=30)
    nomVendore_code = models.CharField(max_length=30)
    nomMU = models.CharField(max_length=30)
    nomVAT_rate = models.FloatField()
    nomUKTZED_code = models.CharField(max_length=30)
    nomStock_type = models.CharField(max_length=30)
    Description = models.CharField(max_length=60)

    def __str__(self):
        return " %s %s %s %s %s %s %s" % (self.nomName, self.nomVendore_code, self.nomMU, self.nomVAT_rate, self.nomUKTZED_code, self.nomStock_type, self.Description)

    class Meta:
        app_label='startapp_console'
        db_table = 'nomenclatures'
        managed = False

class Operations(models.Model):
    opID = models.IntegerField(primary_key=True)
    opCA_name = models.ForeignKey(Counteragents, on_delete=models.CASCADE, db_column='opCA_name')
    opNom_name = models.ForeignKey(Nomenclatures, on_delete=models.CASCADE, db_column='opNom_name')
    opBRD_id = models.ForeignKey(BRD, on_delete=models.CASCADE, db_column='opBRD_id')
    opAC_id = models.ForeignKey(Accounts, on_delete=models.CASCADE, db_column='opAC_id')

    def __str__(self):
        return "%s %s %s %s %s" % (self.opID.__str__(), self.opCA_name, self.opNom_name, self.opBRD_id, self.opAC_id)

    class Meta:
        app_label='startapp_console'
        db_table = 'operations'
        managed = False


class TriggerManager(models.Model):
    updateTriggerStatus = models.CharField(primary_key=True, max_length=30)
    insertTriggerStatus = models.CharField(max_length=30)
    deleteTriggerStatus = models.CharField(max_length=30)
    addCounter = models.IntegerField()
    updateCounter = models.IntegerField()
    deleteCounter = models.IntegerField()

    class Meta:
        app_label = 'startapp_console'
        db_table = 'triggerlog'
        managed = False