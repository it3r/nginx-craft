import json
from http import HTTPStatus

from tornado_mock.httpclient import get_response_stub

from hhapi_tests import ApiTestCase, Route
from hhapi_tests.consts import OPENAPI_SPEC
from hhapi_tests.stubs import session_stub


class QwePageTestCase(ApiTestCase):

    def setUp(self):
        super(QwePageTestCase, self).setUp()

    def get_app(self):
        app = super().get_app()
        app.openapi_spec = OPENAPI_SPEC
        return app

    def test_post_call_body_validation(self):
        session_stub.set_employer_session(self)
        self.set_permissions(('ignore_employer_payable_actions',))

        data = {
            'some': 'bad_data'
        }

        post_response = self.fetch_json('/asd/<zxc>/<qwe>', method="POST", body=json.dumps(data))

        error = post_response["errors"][0]
        self.assertEqual(error['value'], 'тут велью')
        self.assertEqual(error['reason'], 'тут причина')
        self.assertEqual(error['pointer'], 'тут поинтер')
        self.assertEqual(error['type'], 'bad_json_data')
        self.assertEqual(error['description'], 'тут описание')
