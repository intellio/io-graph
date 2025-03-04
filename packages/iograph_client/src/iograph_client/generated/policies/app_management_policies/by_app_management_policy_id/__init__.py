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
	from .applies_to import AppliesToRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.app_management_policy import AppManagementPolicy
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByAppManagementPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies/appManagementPolicies/{appManagementPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AppManagementPolicy:
		"""
		Get appManagementPolicy
		Read the properties of an appManagementPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/appmanagementpolicy-get?view=graph-rest-1.0
		"""
		tags = ['policies.appManagementPolicy']

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
		return await self.request_adapter.send_async(request_info, AppManagementPolicy, error_mapping)

	async def patch(
		self,
		body: AppManagementPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AppManagementPolicy:
		"""
		Update appManagementPolicy
		Update an appManagementPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/appmanagementpolicy-update?view=graph-rest-1.0
		"""
		tags = ['policies.appManagementPolicy']

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
		return await self.request_adapter.send_async(request_info, AppManagementPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete appManagementPolicy
		Delete an appManagementPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/appmanagementpolicy-delete?view=graph-rest-1.0
		"""
		tags = ['policies.appManagementPolicy']
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



	def with_url(self, raw_url: str) -> ByAppManagementPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAppManagementPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAppManagementPolicyIdRequest(self.request_adapter, self.path_parameters)

	def applies_to(self,
		appManagementPolicy_id: str,
	) -> AppliesToRequest:
		if appManagementPolicy_id is None:
			raise TypeError("appManagementPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["appManagementPolicy%2Did"] =  appManagementPolicy_id

		from .applies_to import AppliesToRequest
		return AppliesToRequest(self.request_adapter, path_parameters)

