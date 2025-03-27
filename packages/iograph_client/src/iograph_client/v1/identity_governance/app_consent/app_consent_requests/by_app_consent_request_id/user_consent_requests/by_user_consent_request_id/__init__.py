# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .approval import ApprovalRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.user_consent_request import UserConsentRequest
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserConsentRequestIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/appConsent/appConsentRequests/{appConsentRequest%2Did}/userConsentRequests/{userConsentRequest%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserConsentRequest:
		"""
		Get userConsentRequest
		Read the properties and relationships of a userConsentRequest object.
		Find more info here: https://learn.microsoft.com/graph/api/userconsentrequest-get?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.appConsentApprovalRoute']

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
		return await self.request_adapter.send_async(request_info, UserConsentRequest, error_mapping)

	async def patch(
		self,
		body: UserConsentRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserConsentRequest:
		"""
		Update the navigation property userConsentRequests in identityGovernance
		
		"""
		tags = ['identityGovernance.appConsentApprovalRoute']

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
		return await self.request_adapter.send_async(request_info, UserConsentRequest, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property userConsentRequests for identityGovernance
		
		"""
		tags = ['identityGovernance.appConsentApprovalRoute']
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



	def with_url(self, raw_url: str) -> ByUserConsentRequestIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserConsentRequestIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserConsentRequestIdRequest(self.request_adapter, self.path_parameters)

	def approval(self,
		appConsentRequest_id: str,
		userConsentRequest_id: str,
	) -> ApprovalRequest:
		if appConsentRequest_id is None:
			raise TypeError("appConsentRequest_id cannot be null.")
		if userConsentRequest_id is None:
			raise TypeError("userConsentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["appConsentRequest%2Did"] =  appConsentRequest_id
		path_parameters["userConsentRequest%2Did"] =  userConsentRequest_id

		from .approval import ApprovalRequest
		return ApprovalRequest(self.request_adapter, path_parameters)

