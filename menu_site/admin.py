from django.contrib import admin
from .models import Test, Question, QuestionStatus

# Определение Inline админ-класса для статуса вопросов
class QuestionStatusInline(admin.StackedInline):
    model = QuestionStatus
    can_delete = False
    verbose_name_plural = 'status'

# Определение Inline админ-класса для вопросов
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0  # Не создавать пустых полей для новых записей по умолчанию

# Админ-класс для модели Test
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')  # Отображаемые поля в списке
    inlines = [QuestionInline]  # Включение Inline редактирования вопросов

# Админ-класс для модели Question
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test')  # Отображаемые поля в списке
    inlines = [QuestionStatusInline]  # Включение Inline редактирования статуса

admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)