# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .reject import RejectRequest
	from .cancel_approval import CancelApprovalRequest
	from .approve import ApproveRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.operation_approval_request import OperationApprovalRequest


class ByOperationApprovalRequestIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/operationApprovalRequests/{operationApprovalRequest%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OperationApprovalRequest:
		"""
		Get operationApprovalRequests from deviceManagement
		The Operation Approval Requests
		"""
		tags = ['deviceManagement.operationApprovalRequest']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, OperationApprovalRequest, error_mapping)

	async def patch(
		self,
		body: OperationApprovalRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OperationApprovalRequest:
		"""
		Update the navigation property operationApprovalRequests in deviceManagement
		
		"""
		tags = ['deviceManagement.operationApprovalRequest']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, OperationApprovalRequest, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property operationApprovalRequests for deviceManagement
		
		"""
		tags = ['deviceManagement.operationApprovalRequest']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByOperationApprovalRequestIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOperationApprovalRequestIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOperationApprovalRequestIdRequest(self.request_adapter, self.path_parameters)

	def approve(self,
		operationApprovalRequest_id: str,
	) -> ApproveRequest:
		if operationApprovalRequest_id is None:
			raise TypeError("operationApprovalRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["operationApprovalRequest%2Did"] =  operationApprovalRequest_id

		from .approve import ApproveRequest
		return ApproveRequest(self.request_adapter, path_parameters)

	def cancel_approval(self,
		operationApprovalRequest_id: str,
	) -> CancelApprovalRequest:
		if operationApprovalRequest_id is None:
			raise TypeError("operationApprovalRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["operationApprovalRequest%2Did"] =  operationApprovalRequest_id

		from .cancel_approval import CancelApprovalRequest
		return CancelApprovalRequest(self.request_adapter, path_parameters)

	def reject(self,
		operationApprovalRequest_id: str,
	) -> RejectRequest:
		if operationApprovalRequest_id is None:
			raise TypeError("operationApprovalRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["operationApprovalRequest%2Did"] =  operationApprovalRequest_id

		from .reject import RejectRequest
		return RejectRequest(self.request_adapter, path_parameters)

