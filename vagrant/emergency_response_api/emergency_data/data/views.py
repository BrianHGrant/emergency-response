from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from data.models import Incident, Agency, Alarmlevel, Censustract, Fireblock
from data.serializers import IncidentSerializer, AgencySerializer, AlarmlevelSerializer, CensustractSerializer, FireblockSerializer

@api_view(['GET'])
def incident_list(request, format=None):

    if request.method == 'GET':
        incidents = Incident.objects.all()
        serializedIncidents = IncidentSerializer(incidents, many=True)
        return Response(serializedIncidents.data)

@api_view(['GET'])
def agency_list(request, format=None):

    if request.method == 'GET':
        agencies = Agency.objects.all()
        serializedAgencies = AgencySerializer(agencies, many=True)
        return Response(serializedAgencies.data)

@api_view(['GET'])
def alarmlevel_list(request, format=None):

    if request.method == 'GET':
        alarmlevels = Alarmlevel.objects.all()
        serializedAlarmlevel = AlarmlevelSerializer(alarmlevels, many=True)
        return Response(serializedAlarmlevel.data)

@api_view(['GET'])
def censustract_list(request, format=None):

    if request.method == 'GET':
        censustracts = Censustract.objects.all()
        serializedCensustracts = CensustractSerializer(censustracts, many=True)
        return Response(serializedCensustracts.data)

@api_view(['GET'])
def fireblock_list(request, format=None):

    if request.method == 'GET':
        fireblocks = Fireblock.objects.all()
        serializedFireblocks = FireblockSerializer(fireblocks, many=True)
        return Response(serializedFireblocks.data)
