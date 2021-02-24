from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # Gender choices
    MALE = 1
    FEMALE = 2

    GENDER_CHOICES = {
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    }

    bonus = models.IntegerField(null=True, blank=True)
    user_designation = models.ForeignKey('Designation',
                                         on_delete=models.CASCADE, null=True)
    user_platform = models.ManyToManyField('Platform',
                                           blank=False, related_name='user_platform')


class Modules(models.Model):
    module = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.module


class ProjectTemplate(models.Model):

    template = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.template


class ProjectTemplateModules(models.Model):
    template = models.ForeignKey('ProjectTemplate',
                                 on_delete=models.CASCADE)
    module = models.ManyToManyField('Modules',
                                    blank=True, related_name='ProjectTemplateModules_module')
    platform = models.ManyToManyField('Platform',
                                      related_name='ProjectTemplateModules_platform')

    @property
    def displayname(self):
        return f'{self.template} modules'

    def __str__(self):
        return self.displayname


class Designation(models.Model):

    designation = models.CharField(
        max_length=100, unique=True)

    def __str__(self):
        return self.designation


class EmployeeModules(models.Model):
    designation = models.OneToOneField('Designation', on_delete=models.CASCADE)
    module = models.ManyToManyField('Modules',
                                    related_name='EmployeeModules_module')
    platform = models.ManyToManyField('Platform',
                                      related_name='EmployeeModules_platform')

    @property
    def displayname(self):
        return f'{self.designation} Modules'

    def __str__(self):
        return self.displayname


class ModuleTime(models.Model):

    time = models.FloatField(null=True,
                             blank=True)
    designation = models.ForeignKey(
        'Designation', on_delete=models.CASCADE)
    module = models.ForeignKey('Modules',
                               on_delete=models.CASCADE)

    @property
    def displayname(self):
        return f'{self.designation} | {self.module} | {self.time}'

    def __str__(self):
        return self.displayname


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserHourlyRate(models.Model):
    rate = models.IntegerField(default=00,
                               null=False, blank=False)
    region = models.ForeignKey('Region',
                               on_delete=models.CASCADE)
    designation = models.ForeignKey("Designation",
                                    on_delete=models.CASCADE)

    @property
    def displayname(self):
        return f'{self.region} | {self.designation}'

    def __str__(self):
        return self.displayname


class PlatformType(models.Model):
    platform_type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.platform_type


class Platform(models.Model):

    platform = models.CharField(max_length=50, unique=True)
    platform_type = models.ForeignKey('PlatformType', on_delete=models.CASCADE)
    description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.platform


class PlatformModules(models.Model):
    platform = models.ForeignKey('Platform',
                                 on_delete=models.CASCADE)
    module = models.ManyToManyField('Modules',
                                    related_name='PlatformModules_modules')

    @property
    def displayname(self):
        return f'{self.platform} Modules'

    def __str__(self):
        return self.displayname


# class Project(models.Model):
    # # Priority choices values
    # LOW = 1
    # MEDIUM = 2
    # HIGH = 3
    # CRITICAL = 4

    # PRIORITY_CHOICES = {
    #     (LOW, 'Low'),
    #     (MEDIUM, 'Medium'),
    #     (HIGH, 'High'),
    #     (CRITICAL, 'Critical')
    # }

    # name = models.CharField(max_length=100,
    #     null=False, blank=False)
    # cost = models.IntegerField(null=False, blank=False)
    # assigned_employees = models.ManyToManyField('User',
    #     null=True, blank=True, related_name='Project_assigned_employees')
    # start_date = models.DateField()
    # end_date = models.DateField()
    # priority = models.SmallIntegerField(
    #     choices= PRIORITY_CHOICES, default=2)
    # # template = models.ForeignKey('ProjectTemplate',
    #     # on_delete=models.CASCADE)
    # module = models.ManyToManyField('Modules',
    #     null=True, blank=True, related_name='Project_module')
    # platform = models.ManyToManyField('Platform',
    #     blank=False, related_name='Project_platform')
    # region = models.ForeignKey("Region",
    #     on_delete=models.CASCADE, null=True)

    # @property
    # def displayname(self):
    #     return f'{self.name} | {self.start_date}'

    # def __str__(self):
    #     return self.displayname
