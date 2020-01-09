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
from django.db.models.functions import Length, Coalesce
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

    def statistics_extension(self, exten, start_date, end_date):

        totalReceivedCalls = Cdr.objects.filter(dst=exten, calldate__range=[start_date, end_date]).count()

        totalTimeReceivedCalls = Cdr.objects.filter(Q(dst=exten, calldate__range=[start_date, end_date])).aggregate(duration__sum =
        Coalesce(Sum('duration'),0))['duration__sum']

        totalEmitedCalls = Cdr.objects.filter(src=exten, calldate__range=[start_date, end_date]).count()

        totalTimeEmitedCalls = Cdr.objects.filter(Q(src=exten, calldate__range=[start_date, end_date])).aggregate(
            duration__sum=
            Coalesce(Sum('duration'), 0)
        )['duration__sum']

        totalCalls = totalReceivedCalls + totalEmitedCalls
        totalTimeCalls = totalTimeReceivedCalls + totalTimeEmitedCalls


        total30sCalls =Cdr.objects.annotate(
            dst_len=Length('dst')
        ).filter(
            cnum= exten,
            dst_len__gt=4,
            calldate__range=[start_date, end_date],
            duration__gte=30,
        ).count()
        # total30sSrcCalls = Cdr.objects.annotate(
        #     src_len=Length('src')
        # ).filter(src_len__gt=4, calldate__range=[start_date, end_date], duration__gt=30).count()
        #
        # total30sDstCalls = Cdr.objects.annotate(
        #     dst_len=Length('src')
        # ).filter(dst_len__gt=4, calldate__range=[start_date, end_date], duration__gt=30).count()

        # total30sCalls = total30sSrcCalls + total30sDstCalls

        # totalDuration30sSrcCalls = Cdr.objects.annotate(
        #     src_len=Length('src')
        # ).filter(dst=exten, src_len__gt=4, calldate__range=[start_date, end_date], duration__gt=30).aggregate(
        #     duration__sum=
        #     Coalesce(Sum('duration'), 0)
        # )['duration__sum']
        #
        # totalDuration30sDstCalls = Cdr.objects.annotate(
        #     dst_len=Length('dst')
        # ).filter(src=exten, dst_len__gt=4, calldate__range=[start_date, end_date], duration__gt=30).aggregate(
        #     duration__sum=
        #     Coalesce(Sum('duration'), 0)
        # )['duration__sum']


        # totalDuration30sCalls = totalDuration30sSrcCalls + totalDuration30sDstCalls

        lostCalls = Cdr.objects.filter(disposition="NO ANSWER", dst=exten,
                                       calldate__range=[start_date, end_date]).count()

        valueDict = {'totalCalls': totalCalls, 'totalTimeCalls': totalTimeCalls,
                     'totalReceivedCalls': totalReceivedCalls, 'totalTimeReceivedCalls': totalTimeReceivedCalls,
                     'totalEmitedCalls': totalEmitedCalls, 'totalTimeEmitedCalls': totalTimeEmitedCalls,
                     'total30sCalls': total30sCalls,
                     "lostCalls": lostCalls}
        return valueDict



    def get(self, request):
        """
               GET statistics information

               Args:
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
        extens = request.query_params.get("extens",None)
        if extens !=None:
            extens = extens.split(",")
        start_date = datetime.datetime.strptime(request.query_params.get("start_date", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), '%Y-%m-%d %H:%M:%S')
        end_date = datetime.datetime.strptime(request.query_params.get("end_date", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), '%Y-%m-%d %H:%M:%S')

        results = {}
        if type(extens) == list:
            for exten in extens:
                values = self.statistics_extension(exten.strip(), start_date, end_date)
                results[exten.strip()] = values
        return Response(results,
                        status=HTTP_200_OK)


class CDRCallFailsViewSet(APIView):
    permission_classes = [IsAuthenticated]
    extens = [
        917815680,
        902230290,
        902888222,
        911591091,
        911591092,
        911680893,
        917370639,
        933900533,
        934520131,
        955319893,
        961155837,
        934522978,
        911169777,
        911592997,
        911592996,
        911591093,
        911169778
    ]
    # Exten: 917815680(917815680)
    # Exten: 917815680(917815680)
    # Exten: 917815680(917815680)
    # Exten: 902230290(902230290)
    # Exten: 902230290(902230290)
    # Exten: 902230290(902230290)
    # Exten: 902888222(902888222)
    # Exten: 902888222(902888222)
    # Exten: 902888222(902888222)
    # Exten: 911591091(911591091)
    # Exten: 911591091(911591091)
    # Exten: 911591091(911591091)
    # Exten: 911591092(911591092)
    # Exten: 911591092(911591092)
    # Exten: 911591092(911591092)
    # Exten: 911680893(911680893)
    # Exten: 911680893(911680893)
    # Exten: 911680893(911680893)
    # Exten: 917370639(917370639)
    # Exten: 917370639(917370639)
    # Exten: 917370639(917370639)
    # Exten: 933900533(933900533)
    # Exten: 933900533(933900533)
    # Exten: 933900533(933900533)
    # Exten: 934520131(934520131)
    # Exten: 934520131(934520131)
    # Exten: 934520131(934520131)
    # Exten: 955319893(955319893)
    # Exten: 955319893(955319893)
    # Exten: 955319893(955319893)
    # Exten: 961155837(961155837)
    # Exten: 961155837(961155837)
    # Exten: 934522978(934522978)
    # Exten: 911169777(911169777)
    # Exten: 911592997(911592997)
    # Exten: 911592996(911592996)
    # Exten: 911591093(911591093)
    # Exten: 911169778(911169778)
    def get(self, request):
        # extens = request.query_params.get("extens", None)
        # if extens != None:
        #     extens = extens.split(",")
        start_date = datetime.datetime.strptime(
            request.query_params.get("start_date", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            '%Y-%m-%d %H:%M:%S')
        end_date = datetime.datetime.strptime(
            request.query_params.get("end_date", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            '%Y-%m-%d %H:%M:%S')
        results = {}
        sumNOANSWER=0
        sumFAILED=0
        for exten in self.extens:
            cantNOANSWER = Cdr.objects.filter(disposition="NO ANSWER", src__icontains=exten,
                           calldate__range=[start_date, end_date]).count()

            cantFAILED = Cdr.objects.filter(disposition="FAILED", src__icontains=exten,
                                        calldate__range=[start_date, end_date]).count()
            results[exten] = {
                "NOANSWER":cantNOANSWER,
                "FAILED": cantFAILED
            }
            sumNOANSWER= sumNOANSWER + cantNOANSWER
            sumFAILED = sumFAILED + cantFAILED
        results['total']= {
            "TOTAL": sumNOANSWER + sumFAILED ,
            "FAILED": sumFAILED,
            "NOANSWER" : sumNOANSWER
        }
        return Response(results,
                        status=HTTP_200_OK)
