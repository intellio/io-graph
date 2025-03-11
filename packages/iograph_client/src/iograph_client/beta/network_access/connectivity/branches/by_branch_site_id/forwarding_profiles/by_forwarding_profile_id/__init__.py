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
	from .service_principal import ServicePrincipalRequest
	from .policies import PoliciesRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.networkaccess_forwarding_profile import NetworkaccessForwardingProfile


class ByForwardingProfileIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/branches/{branchSite%2Did}/forwardingProfiles/{forwardingProfile%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessForwardingProfile:
		"""
		Get forwardingProfiles from networkAccess
		Each forwarding profile associated with a branch site is specified. Supports $expand.
		"""
		tags = ['networkAccess.connectivity']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessForwardingProfile, error_mapping)

	async def patch(
		self,
		body: NetworkaccessForwardingProfile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessForwardingProfile:
		"""
		Update the navigation property forwardingProfiles in networkAccess
		
		"""
		tags = ['networkAccess.connectivity']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessForwardingProfile, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property forwardingProfiles for networkAccess
		
		"""
		tags = ['networkAccess.connectivity']
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



	def with_url(self, raw_url: str) -> ByForwardingProfileIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByForwardingProfileIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByForwardingProfileIdRequest(self.request_adapter, self.path_parameters)

	def policies(self,
		branchSite_id: str,
		forwardingProfile_id: str,
	) -> PoliciesRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")
		if forwardingProfile_id is None:
			raise TypeError("forwardingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id
		path_parameters["forwardingProfile%2Did"] =  forwardingProfile_id

		from .policies import PoliciesRequest
		return PoliciesRequest(self.request_adapter, path_parameters)

	def service_principal(self,
		branchSite_id: str,
		forwardingProfile_id: str,
	) -> ServicePrincipalRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")
		if forwardingProfile_id is None:
			raise TypeError("forwardingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id
		path_parameters["forwardingProfile%2Did"] =  forwardingProfile_id

		from .service_principal import ServicePrincipalRequest
		return ServicePrincipalRequest(self.request_adapter, path_parameters)

