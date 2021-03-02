from rest_framework.generics import ListAPIView
from webapp.views.prediction.predict import predict
from rest_framework.response import Response
from webapp.views.prediction.costing import ProjectCost

class PostPredictionAPIListView(ListAPIView):
    def post(self, request, format=None):
        platforms = request.POST.getlist("platforms", [])
        modules = request.POST.getlist("modules", [])
        region = request.POST.getlist('region', [])
        requirements = {}
        for platform in platforms:
            requirements[platform] = modules
        designation_group = predict(requirements)

        designation_group_time_cost = {}
        for model in designation_group.keys():
            designation_group_time_cost[model] = ProjectCost(designation_group[model], region[0])

        return Response(
            {
                'result': designation_group_time_cost
            }
        )