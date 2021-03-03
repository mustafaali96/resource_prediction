from rest_framework.generics import ListAPIView
from rest_framework.response import Response

class PostProjectAPIListView(ListAPIView):
    def post(self, request, format=None):
        project_name = request.POST.get('project_name')
        project_cost = request.POST.get("project_cost")
        predicted_designations = request.POST.getlist("designations", [])
        duration = request.POST.get("duration")
        template = request.POST.get("template")
        modules = request.POST.getlist("modules", [])
        platforms = request.POST.getlist("platforms", [])
        region = request.POST.get('region')

        return Response(
            {
                'result': "Your Project has been recorded"
            }
        )