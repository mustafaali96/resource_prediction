from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from webapp.views.training.training import train


class PostTrainingAPIListView(ListAPIView):
    def post(self, request, format=None):
        train()

        return Response(
            {
                'result': "Model Training Successful"
            }
        )