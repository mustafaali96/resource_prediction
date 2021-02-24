from rest_framework.generics import ListAPIView
from webapp.views.prediction.predict import predict
from rest_framework.response import Response
from webapp.views.prediction.training import train


class GetPredictionAPIListView(ListAPIView):
    def post(self, request, format=None):
        platforms = request.POST.getlist("platforms", [])
        modules = request.POST.getlist("modules", [])
        requirements = {}
        for platform in platforms:
            requirements[platform] = modules
        designation_group = predict(requirements)
        train()
        print("Done Training")

        return Response(
            {
                'result': designation_group
            }
        )