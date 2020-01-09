from django.db import models

# Create your models here.
from django.db import models
import time

DISPOSITION = (
    ('FAILED', 'FAILED'),
    ('ANSWERED', 'ANSWERED'),
    ('NO ANSWER', 'NO ANSWER'),
    ('BUSY', 'BUSY'),
)


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
    uniqueid = models.CharField(max_length=32, primary_key=True)
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
        app_label = 'cdr'
        ordering = ('calldate',)

    def __unicode__(self):
        return 'callid: %s "%s" (%i)' % (self.uniqueid, self.disposition, self.duration)

    @property
    def tiempo_facturado(self):
        return time.strftime('%H:%M:%S', time.gmtime(self.billsec))


class Rate(models.Model):
    date_of_rate = models.DateField()
    value = models.DecimalField(max_digits=5, decimal_places=4, default=0)

    class Meta:
        app_label = 'rate'
        managed = False
    def __unicode__(self):
        return '%s' % (self.date_of_rate)

