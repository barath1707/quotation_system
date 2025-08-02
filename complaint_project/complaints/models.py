from django.db import models

class CustomerDetails(models.Model):
    customer_name = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'customer_details'

class CustomerQuotation(models.Model):
    customer = models.ForeignKey('CustomerDetails', models.DO_NOTHING)
    quotation_name = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'customer_quotation'

class QuotationTableInstance(models.Model):
    quotation = models.ForeignKey('CustomerQuotation', models.DO_NOTHING)
    table_name = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'quotation_table_instance'

class TableHeaderType(models.Model):
    field_type = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'table_header_type'

    def __str__(self):
        return '%s' % self.field_type

class QuotationTableHeader(models.Model):
    table = models.ForeignKey('QuotationTableInstance', models.DO_NOTHING)
    field_type = models.ForeignKey('TableHeaderType', models.DO_NOTHING, db_column='field_type_id')
    field_name = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'quotation_table_header'

class QuotationTableValue(models.Model):
    table = models.ForeignKey('QuotationTableInstance', models.DO_NOTHING)
    row_id = models.IntegerField()
    field = models.ForeignKey('QuotationTableHeader', models.DO_NOTHING)
    field_value = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'quotation_table_value'

class CustomerQuotationDetails(models.Model):
    customer = models.ForeignKey('CustomerDetails', models.DO_NOTHING)
    quotation = models.ForeignKey('CustomerQuotation', models.DO_NOTHING)
    quotation_date = models.DateField(blank=True, null=True)
    quotation_address = models.TextField(blank=True, null=True)
    quotation_subject = models.TextField(blank=True, null=True)
    quotation_description = models.CharField(max_length=255, blank=True, null=True)
    quotation_referrence = models.TextField(max_length=255, blank=True, null=True)
    quotation_note = models.TextField(blank=True, null=True)
    quotation_bank_details = models.TextField(blank=True, null=True)
    quotation_signature = models.TextField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_quotation_details'