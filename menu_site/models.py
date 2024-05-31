from django.db import models
from django.template.defaultfilters import slugify


class Test(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class QuestionStatus(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='status')
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return "Correct" if self.is_correct else "Incorrect"
