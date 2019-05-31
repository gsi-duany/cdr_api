# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cdr(models.Model):
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    userfield = models.CharField(max_length=255)
    did = models.CharField(max_length=50)
    recordingfile = models.CharField(max_length=255)
    cnum = models.CharField(max_length=80)
    cnam = models.CharField(max_length=80)
    outbound_cnum = models.CharField(max_length=80)
    outbound_cnam = models.CharField(max_length=80)
    dst_cnam = models.CharField(max_length=80)
    linkedid = models.CharField(max_length=32)
    peeraccount = models.CharField(max_length=80)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cdr'


class CdrBackup(models.Model):
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    userfield = models.CharField(max_length=255)
    did = models.CharField(max_length=50)
    recordingfile = models.CharField(max_length=255)
    cnum = models.CharField(max_length=80)
    cnam = models.CharField(max_length=80)
    outbound_cnum = models.CharField(max_length=80)
    outbound_cnam = models.CharField(max_length=80)
    dst_cnam = models.CharField(max_length=80)
    linkedid = models.CharField(max_length=32)
    peeraccount = models.CharField(max_length=80)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cdr_backup'


class CdrLegacy(models.Model):
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    userfield = models.CharField(max_length=255)
    did = models.CharField(max_length=50)
    recordingfile = models.CharField(max_length=255)
    cnum = models.CharField(max_length=80)
    cnam = models.CharField(max_length=80)
    outbound_cnum = models.CharField(max_length=80)
    outbound_cnam = models.CharField(max_length=80)
    dst_cnam = models.CharField(max_length=80)
    linkedid = models.CharField(max_length=32)
    peeraccount = models.CharField(max_length=80)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cdr_legacy'


class CdrOriginal(models.Model):
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    userfield = models.CharField(max_length=255)
    did = models.CharField(max_length=50)
    recordingfile = models.CharField(max_length=255)
    cnum = models.CharField(max_length=80)
    cnam = models.CharField(max_length=80)
    outbound_cnum = models.CharField(max_length=80)
    outbound_cnam = models.CharField(max_length=80)
    dst_cnam = models.CharField(max_length=80)
    linkedid = models.CharField(max_length=32)
    peeraccount = models.CharField(max_length=80)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cdr_original'


class Cel(models.Model):
    eventtype = models.CharField(max_length=30)
    eventtime = models.DateTimeField()
    cid_name = models.CharField(max_length=80)
    cid_num = models.CharField(max_length=80)
    cid_ani = models.CharField(max_length=80)
    cid_rdnis = models.CharField(max_length=80)
    cid_dnid = models.CharField(max_length=80)
    exten = models.CharField(max_length=80)
    context = models.CharField(max_length=80)
    channame = models.CharField(max_length=80)
    appname = models.CharField(max_length=80)
    appdata = models.CharField(max_length=255)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    linkedid = models.CharField(max_length=32)
    peer = models.CharField(max_length=80)
    userdeftype = models.CharField(max_length=255)
    extra = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'cel'


class Queuelog(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField()
    callid = models.CharField(max_length=40)
    queuename = models.CharField(max_length=20)
    serverid = models.CharField(max_length=20)
    agent = models.CharField(max_length=40)
    event = models.CharField(max_length=20)
    data1 = models.CharField(max_length=40)
    data2 = models.CharField(max_length=40)
    data3 = models.CharField(max_length=40)
    data4 = models.CharField(max_length=40)
    data5 = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'queuelog'


class Replication(models.Model):
    año = models.CharField(max_length=255, blank=True, null=True)
    mes = models.CharField(max_length=255, blank=True, null=True)
    dia = models.CharField(max_length=255, blank=True, null=True)
    hora = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'replication'
