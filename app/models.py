from django.db import models


class Person(models.Model):
    class Meta:
        verbose_name_plural = "People"

    nick = models.CharField(max_length=56)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    about = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    class Meta:
        verbose_name_plural = "Projects"

    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    name = models.CharField(max_length=56)
    url = models.CharField(max_length=256, blank=True)
    desc = models.TextField(null=True, blank=True)

    languages = models.ManyToManyField('Language', blank=True)
    frameworks = models.ManyToManyField('Framework', blank=True)
    technologies = models.ManyToManyField('Technology', blank=True)
    protocols = models.ManyToManyField('Protocol', blank=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    class Meta:
        verbose_name_plural = "Languages"
        ordering = ["name"]

    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    projects = models.ManyToManyField(
        Project, through="Project_languages", blank=True)
    name = models.CharField(max_length=56, unique=True)

    def __str__(self):
        return self.name


class Framework(models.Model):
    class Meta:
        verbose_name_plural = "Frameworks"

    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    projects = models.ManyToManyField(
        Project, through="Project_frameworks", blank=True)
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name


class Technology(models.Model):
    class Meta:
        verbose_name_plural = "Technologies"

    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    projects = models.ManyToManyField(
        Project, through="Project_technologies", blank=True)
    name = models.CharField(max_length=56, unique=True)

    def __str__(self):
        return self.name


class Protocol(models.Model):
    class Meta:
        verbose_name_plural = "Protocols"

    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    projects = models.ManyToManyField(
        Project, through="Project_protocols", blank=True)
    name = models.CharField(max_length=56, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name
