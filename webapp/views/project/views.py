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

        project = {"Project Name": project_name, "Project Cost": project_cost,
                    "Template":template, "Project Platforms":platforms, 
                    "Region":region, "Project Time":duration, 
                    "Designations":predicted_designations, "Project Modules":modules}

        return Response(
            {
                'result': "Your Project has been recorded",
                'Project Details': project
            }
        )