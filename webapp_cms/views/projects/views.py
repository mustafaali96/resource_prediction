from webapp import models
from django.views.generic import View
from django.shortcuts import render, redirect


class ProjectView(View):
    def get(self, request, *args, **kwargs):
        projects = models.Project.objects.all()
        # all_badge_data = []
        # for badge in badges:
        #     badge_data = {}
        #     badge_data['id'] = badge.id
        #     badge_data['image'] = badge.image.url
        #     badge_data['lesson_name'] = badge.lesson_id.lesson_name
        #     badge_data['user_count'] = models.UserLessonRecord.objects.filter(lesson_id=badge.lesson_id).count()
            # badge['user_count'] = str(models.UserLessonRecord.objects.filter(lesson_id=badge.lesson_id).count())
            # all_badge_data.append(badge_data)
        return render(request, 'Project/Projects.html', {'projects': projects})
