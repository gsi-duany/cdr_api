from rest_framework.test import  APITestCase
from rest_framework.test import APIRequestFactory
from ..views import CDRInfoExtenViewSet
from ..models import Cdr
class CDRTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CDRInfoExtenViewSet.as_view()
        self.uri = 'api/statistics/infoExten/'
        self.cdr1 = Cdr(
            calldate = "2017-07-29 05:43:51",
            clid = '"Jack Bradford" <101>',
            src = 101,
            dst = 9,
            dcontext = "app-echo-test-echo",
            channel= 'PJSIP/101-00000000',
            dstchannel="",
            lastapp='Echo',
            lastdata='',
            duration =73,
            billsec= 73,
            disposition = 'ANSWERED',
            amaflags = 3,
            accountcode = " ",
            uniqueid = 1501299831.0,
            userfield = "",
            did = "",
            recordingfile= "",
            cnum = 101,
            cnam = "Jack Bradford",
            outbound_cnum = "",
            outbound_cnam = "",
            dst_cnam = "",
            linkedid = 1501299831.0,
            peeraccount ="",
            sequence = 0,
        )

        self.cdr1.save()



    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEquals(request.status_code, 200,
                          'Expected Response Code 200, received {0} instead.'
                          .format(response.status_code)
                          )
        self.assertEquals(response.callsTotal, 1,
                          'Expected Response Call Total 1, received {0} instead.'
                          .format(response.callsTotal)
                          )