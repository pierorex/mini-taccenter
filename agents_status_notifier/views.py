from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, status
from rest_framework.response import Response
import random


class AgentStatusView(APIView):
    
    def get(self, request):
        statuses = ['paused', 'available', 'in-call', 'ringing',
                    'categorizing', 'pause_request']
        status_dict = {}            
                    
        for i in range(15):
            status_dict.update({
                'Agent'+str(i): {'status': random.choice(statuses),
                                 'time_in_status': random.randint(1,1000)}
            })
        
        return Response(data=status_dict, status=status.HTTP_200_OK)
