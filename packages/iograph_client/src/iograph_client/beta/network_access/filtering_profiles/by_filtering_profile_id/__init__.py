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
	from .policies import PoliciesRequest
	from .conditional_access_policies import ConditionalAccessPoliciesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.networkaccess_filtering_profile import NetworkaccessFilteringProfile


class ByFilteringProfileIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/filteringProfiles/{filteringProfile%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessFilteringProfile:
		"""
		Get filteringProfiles from networkAccess
		A filtering profile associates network access policies with Microsoft Entra ID Conditional Access policies, so that access policies can be applied to users and groups.
		"""
		tags = ['networkAccess.filteringProfile']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessFilteringProfile, error_mapping)

	async def patch(
		self,
		body: NetworkaccessFilteringProfile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessFilteringProfile:
		"""
		Update filteringProfile
		Update the properties of a filteringProfile object.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-filteringprofile-update?view=graph-rest-beta
		"""
		tags = ['networkAccess.filteringProfile']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessFilteringProfile, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property filteringProfiles for networkAccess
		
		"""
		tags = ['networkAccess.filteringProfile']
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



	def with_url(self, raw_url: str) -> ByFilteringProfileIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByFilteringProfileIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByFilteringProfileIdRequest(self.request_adapter, self.path_parameters)

	def conditional_access_policies(self,
		filteringProfile_id: str,
	) -> ConditionalAccessPoliciesRequest:
		if filteringProfile_id is None:
			raise TypeError("filteringProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["filteringProfile%2Did"] =  filteringProfile_id

		from .conditional_access_policies import ConditionalAccessPoliciesRequest
		return ConditionalAccessPoliciesRequest(self.request_adapter, path_parameters)

	def policies(self,
		filteringProfile_id: str,
	) -> PoliciesRequest:
		if filteringProfile_id is None:
			raise TypeError("filteringProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["filteringProfile%2Did"] =  filteringProfile_id

		from .policies import PoliciesRequest
		return PoliciesRequest(self.request_adapter, path_parameters)

