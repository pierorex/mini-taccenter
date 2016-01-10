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

    def post(self, request, *args, **kwargs):
        # Check basic conditions and return HTTP statuses accordingly
        agent_status = request.data.get('status', None)
        agent_ext = request.data.get('agent_ext', None)
        agent_name = request.data.get('agent', None)
        
        if not (agent_ext and agent_status and agent_name and
                status in ['paused', 'available', 'in-call', 'ringing',
                           'categorizing', 'pause_request']):
            return Response(data={'error': 'Missing something.'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data={}, status=status.HTTP_200_OK)


class AgentView(APIView):
    
    def get(self, query_dict):
        # Return some mocked random information
        return Response(data={'username': query_dict.GET['username'], 
                              'tmp_ext': random.randint(1,1000)},
                        status=status.HTTP_200_OK)
