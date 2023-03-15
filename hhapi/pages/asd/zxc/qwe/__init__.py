from http import HTTPStatus

from hhapi.consts import BACKEND_UNAVAILABLE, ORDER_BY
from hhapi.errors import HTTPError, BadArgumentError
from hhapi.page_handler.json import HhapiJsonPageHandler
from hhapi.service.security.preprocessors.auth_type import employer_only
from hhapi.page_handler.helpers import parse_json_object_body
from hhapi.service.validation_openapi import validate_by_schema


class Page(HhapiJsonPageHandler):

    action_by_method = {
        'get': 'get_qwe',
        'put': 'update_qwe',
        'delete': 'delete_qwe',
    }
    
    @authorized_only
    def get_page(self):
        # for arguments
        #argument = paging.get_arguments(self.request.arguments)

        # for request
        # result = yield self.get_url(
        #     self.config.<host>,
        #     '<url>',
        #     data=request_data,
        #     headers={
        #         'Accept': 'application/json'
        #     }
        # )

        self.send_json({ 'example': 'response' })

    def get_page_fail_fast(self, request_result):
        if request_result.response.code == HTTPStatus.BAD_REQUEST:
            result_status = HTTPStatus.BAD_REQUEST
        elif request_result.response.code in (HTTPStatus.FORBIDDEN, HTTPStatus.NOT_FOUND):
            result_status = HTTPStatus.NOT_FOUND

        raise HTTPError(
            result_status, backend_response=request_result.response
        )
    
    @authorized_only
    def put_page(self):
        self.send_json({'key': 'value'})

    def put_page_fail_fast(self, request_result):
        raise HTTPError(HTTPStatus.BAD_REQUEST, user_errors=BadArgumentError(
            'example put error'
        ))
    
    @authorized_only
    def delete_page(self):
        arg = self.get_argument('some_arg', default='default')

        # yield self.delete_url(
        #     self.config.<host>,
        #     '<url>',
        #     name='name',
        #     data={
        #         'someData': 'value',
        #     },
        # )

        self.set_status(HTTPStatus.NO_CONTENT)

    def delete_page_fail_fast(self, request_result):
        raise HTTPError(BACKEND_UNAVAILABLE, backend_response=request_result.response)
