from rest_framework.views import APIView
from django.http import JsonResponse
import json
from .phishing_url_detection import DETECTION


class URLPredictionApiView(APIView):
	def post(self, request):
		js = str(request.data).replace("'", '"')
		# GET THE URL FROM THE API
		url = (json.loads(js)['url'])
		detection = DETECTION()
		# CALL THE DECTECTION METHOD HERE
		prediction = detection.featureExtractions(url)
		return JsonResponse({"success": True, "detection":prediction}, safe=False)






