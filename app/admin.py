from django.contrib import admin

from app.models import Framework, Language, Person, Project, Technology


class PersonInline(admin.StackedInline):
    model = Person
    extra = 0


class LanguageProjectsInline(admin.TabularInline):
    """ A relationship inline for project languages. """
    model = Language.projects.through
    extra = 0


class FrameworkProjectsInline(admin.TabularInline):
    """ A relationship inline for project frameworks. """
    model = Framework.projects.through
    extra = 0


class TechnologyProjectsInline(admin.TabularInline):
    """ A relationship inline for project technologies. """
    model = Technology.projects.through
    extra = 0


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [ProjectInline]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    inlines = [LanguageProjectsInline]
    exclude = ('projects',)


@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    inlines = [FrameworkProjectsInline]
    exclude = ('projects',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    inlines = [TechnologyProjectsInline]
    exclude = ('projects',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        LanguageProjectsInline,
        FrameworkProjectsInline,
        TechnologyProjectsInline
    ]
