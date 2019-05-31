from django.shortcuts import render
from rest_framework import viewsets, mixins

from .serializers import CdrSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from django_filters import DateFilter, DateRangeFilter
from django.db.models import Sum, Count, Avg, Q
from django.db.models.functions import Length
from .models import Cdr
from datetime import datetime
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from .filters import CdrFilters

import datetime
# Create your views here.

class CdrViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('clid', 'src', 'dst', 'disposition')
    permission_classes = [IsAuthenticated]
    ordering_fields = ('calldate')

    def get_queryset(self):
        return self.queryset


class CDRInfoExtenViewSet(APIView):

    permission_classes= [IsAuthenticated]

    def get(self, request):
        """
               GET statistics information

               Parameters:
                  - name: exten
                    description: Exten Number that you what obtain information
                    required: true
                    type: string
                  - name: start_date
                    description: Initial date
                    required: true
                    type: datetime
                  - name: end_date
                    description: Final date
                    required: true
                    type: datetime
                return {'totalCalls': totalCalls, 'totalTimeCalls': totalTimeCalls,
                     'totalReceivedCalls': totalReceivedCalls,'totalTimeReceivedCalls': totalTimeReceivedCalls,
                     'totalEmitedCalls': totalEmitedCalls,'timeTotalEmitedCalls': totalTimeEmitedCalls,
                     'total30sCalls': total30sCalls,'totalDuration30sCalls': totalDuration30sCalls, "lostCalls": lostCalls}
            """
        exten = request.query_params.get("exten")
        start_date = datetime.datetime.strptime(request.query_params.get("start_date"), '%Y-%m-%d %H:%M:%S')
        end_date = datetime.datetime.strptime(request.query_params.get("end_date"), '%Y-%m-%d %H:%M:%S')

        totalReceivedCalls = Cdr.objects.filter(dst=exten, calldate__range=[start_date, end_date]).count()

        totalTimeReceivedCalls = Cdr.objects.filter(Q(dst=exten, calldate__range=[start_date, end_date])).aggregate(
            Sum('duration'))['duration__sum']

        totalEmitedCalls = Cdr.objects.filter(src=exten, calldate__range=[start_date, end_date]).count()
        totalTimeEmitedCalls = Cdr.objects.filter(Q(src=exten, calldate__range=[start_date, end_date])).aggregate(
            Sum('duration'))['duration__sum']

        totalCalls = totalReceivedCalls + totalEmitedCalls
        totalTimeCalls = totalTimeReceivedCalls + totalTimeEmitedCalls

        total30sSrcCalls = Cdr.objects.annotate(
            src_len=Length('src') 
        ).filter(src_len__gt=4, calldate__range=[start_date, end_date], duration__gt=30).count()

        total30sDstCalls = Cdr.objects.annotate(
            dst_len=Length('src')
        ).filter(dst_len__gt=4, calldate__range=[start_date, end_date], duration__gt=30).count()

        total30sCalls = total30sSrcCalls + total30sDstCalls

        totalDuration30sSrcCalls = Cdr.objects.annotate(
            src_len=Length('src')
        ).filter(dst = exten, src_len__gt=4, calldate__range=[start_date, end_date], duration__gt=30).aggregate(Sum('duration'))['duration__sum']

        totalDuration30sDstCalls = Cdr.objects.annotate(
            dst_len=Length('dst')
        ).filter(src = exten,dst_len__gt=4, calldate__range=[start_date, end_date], duration__gt=30).aggregate(Sum('duration'))['duration__sum']

        totalDuration30sCalls = totalDuration30sSrcCalls + totalDuration30sDstCalls

        lostCalls =  Cdr.objects.filter(disposition="NO ANSWER", dst = exten, calldate__range=[start_date, end_date]).count()

        valueDict = {'totalCalls': totalCalls, 'totalTimeCalls': totalTimeCalls,
                     'totalReceivedCalls': totalReceivedCalls,'totalTimeReceivedCalls': totalTimeReceivedCalls,
                     'totalEmitedCalls': totalEmitedCalls,'totalTimeEmitedCalls': totalTimeEmitedCalls,
                     'total30sCalls': total30sCalls,'totalDuration30sCalls': totalDuration30sCalls, "lostCalls": lostCalls}

        return Response(valueDict,
                        status=HTTP_200_OK)
     