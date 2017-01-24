# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Agency(models.Model):
    agency_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    statecode = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agency'


class Alarmlevel(models.Model):
    alarmlevel_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_911 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alarmlevel'

class Censustract(models.Model):
    gid = models.AutoField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce = models.CharField(max_length=1, blank=True, null=True)
    geoid = models.CharField(max_length=12, blank=True, null=True)
    namelsad = models.CharField(max_length=13, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'censustract'

class Fireblock(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid_1 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    objectid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fma = models.CharField(max_length=2, blank=True, null=True)
    resp_zone = models.CharField(max_length=6, blank=True, null=True)
    jurisdict = models.CharField(max_length=2, blank=True, null=True)
    dist_grp = models.CharField(max_length=2, blank=True, null=True)
    notes = models.CharField(max_length=60, blank=True, null=True)
    of_fma = models.CharField(max_length=26, blank=True, null=True)
    mv_label = models.CharField(max_length=15, blank=True, null=True)
    shape_star = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_stle = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fireblock'


class Firestation(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    station = models.CharField(max_length=6, blank=True, null=True)
    address = models.CharField(max_length=38, blank=True, null=True)
    city = models.CharField(max_length=28, blank=True, null=True)
    district = models.CharField(max_length=40, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'firestation'


class Fma(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fma = models.CharField(max_length=26, blank=True, null=True)
    mv_label = models.CharField(max_length=15, blank=True, null=True)
    shape_star = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_stle = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fma'


class Incident(models.Model):
    incident_id = models.IntegerField(primary_key=True)
    responderunit_id = models.IntegerField(blank=True, null=True)
    runnumber = models.CharField(max_length=20, blank=True, null=True)
    alarmlevel_id = models.IntegerField(blank=True, null=True)
    mutualaid_id = models.IntegerField(blank=True, null=True)
    fmarespcomp = models.CharField(max_length=6, blank=True, null=True)
    fireblock = models.CharField(max_length=6, blank=True, null=True)
    neighborassoc = models.CharField(max_length=18, blank=True, null=True)
    censustract = models.CharField(max_length=6, blank=True, null=True)
    quad = models.CharField(max_length=2, blank=True, null=True)
    streetname = models.CharField(max_length=30, blank=True, null=True)
    streettype = models.CharField(max_length=4, blank=True, null=True)
    quad2 = models.CharField(max_length=2, blank=True, null=True)
    streetname2 = models.CharField(max_length=30, blank=True, null=True)
    streettype2 = models.CharField(max_length=4, blank=True, null=True)
    county = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=9, blank=True, null=True)
    incdate = models.DateField(blank=True, null=True)
    typenaturecode_id = models.IntegerField(blank=True, null=True)
    incsitfoundprm_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident'


class IncidentsIncidents(models.Model):
    incident_id = models.IntegerField(primary_key=True)
    runnumber = models.CharField(max_length=20)
    fmarespcomp = models.CharField(max_length=6)
    fireblock = models.CharField(max_length=6)
    neighborassoc = models.CharField(max_length=18)
    censustract = models.CharField(max_length=6)
    quad = models.CharField(max_length=2)
    streetname = models.CharField(max_length=30)
    streettype = models.CharField(max_length=4)
    quad2 = models.CharField(max_length=2)
    streetname2 = models.CharField(max_length=30)
    streettype2 = models.CharField(max_length=4)
    county = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'incidents_incidents'


class Incsitfound(models.Model):
    incsitfound_id = models.IntegerField(primary_key=True)
    incsitfoundsub_id = models.IntegerField()
    description = models.CharField(max_length=50, blank=True, null=True)
    statecode = models.CharField(max_length=3, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)
    inactive = models.IntegerField(blank=True, null=True)
    nfirs = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incsitfound'


class Incsitfoundclass(models.Model):
    incsitfoundclass_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incsitfoundclass'


class Incsitfoundsub(models.Model):
    incsitfoundsub_id = models.IntegerField(primary_key=True)
    incsitfoundclass_id = models.IntegerField()
    description = models.CharField(max_length=50, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incsitfoundsub'


class Inctimes(models.Model):
    inctimes_id = models.IntegerField(primary_key=True)
    timedesc_id = models.IntegerField()
    incident_id = models.IntegerField()
    responder_id = models.IntegerField(blank=True, null=True)
    realtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inctimes'


class Mutualaid(models.Model):
    mutualaid_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    inactive = models.IntegerField(blank=True, null=True)
    nfirs = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mutualaid'


class Responder(models.Model):
    incident_id = models.IntegerField()
    responder_id = models.IntegerField()
    responderunit_id = models.IntegerField(blank=True, null=True)
    codetosc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responder'
        unique_together = (('incident_id', 'responder_id'),)


class Responderunit(models.Model):
    responderunit_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_911 = models.CharField(max_length=6, blank=True, null=True)
    station_id = models.IntegerField(blank=True, null=True)
    translateto = models.CharField(max_length=50, blank=True, null=True)
    agency_id = models.IntegerField(blank=True, null=True)
    process = models.IntegerField(blank=True, null=True)
    versaterm = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responderunit'


class Situationfound(models.Model):
    situationfound_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    review = models.IntegerField(blank=True, null=True)
    inactive = models.IntegerField(blank=True, null=True)
    nemsis = models.CharField(max_length=10, blank=True, null=True)
    e09_15 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'situationfound'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Station(models.Model):
    station_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'


class Timedesc(models.Model):
    timedesc_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_911 = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timedesc'


class Typenaturecode(models.Model):
    typenaturecode_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    id_911 = models.CharField(max_length=8, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    nemsis = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typenaturecode'
