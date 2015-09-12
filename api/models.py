from django.db import models

class Citation(models.Model):
    id = models.IntegerField(primary_key=True)
    citation_number = models.IntegerField(default=0, blank=True, null=True)
    citation_date = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    last_name_phone = models.CharField(max_length=255, default='')
    date_of_birth = models.DateTimeField(blank=True, null=True)
    defendant_address = models.CharField(max_length=255, default='')

    defendant_city = models.CharField(max_length=255, default='')
    defendant_state = models.CharField(max_length=255, default='')
    drivers_license_number = models.CharField(max_length=255, default='')
    court_date = models.DateTimeField(blank=True, null=True)

    court_location = models.CharField(max_length=255, default='')
    court_address = models.CharField(max_length=255, default='')

    def __unicode__(self):
        return u'%s' % (self.id)

    class Meta:
        verbose_name = 'Citation'
        verbose_name_plural = 'Citations'
        app_label = "api"

class Violation(models.Model):
    id = models.IntegerField(primary_key=True)
    citation_number = models.IntegerField(default=0, blank=True, null=True)
    violation_number = models.CharField(max_length=255, default='')
    violation_description = models.CharField(max_length=255, default='')
    warrant_status = models.BooleanField(default=False)
    warrant_number = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=255, default='')
    status_date = models.DateTimeField(blank=True, null=True)
    fine_amount = models.CharField(max_length=255, default="")
    court_cost = models.CharField(max_length=255, default="")

    def __unicode__(self):
        return u'%s' % (self.id)

    class Meta:
        verbose_name = 'Violation'
        verbose_name_plural = 'Violations'
        app_label = "api"