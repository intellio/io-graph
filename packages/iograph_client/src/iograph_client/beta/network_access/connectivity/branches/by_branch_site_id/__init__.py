# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .forwarding_profiles import ForwardingProfilesRequest
	from .device_links import DeviceLinksRequest
	from .connectivity_configuration import ConnectivityConfigurationRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.networkaccess_branch_site import NetworkaccessBranchSite
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByBranchSiteIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/branches/{branchSite%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessBranchSite:
		"""
		Get branchSite (deprecated)
		Retrieve information about a specific branch.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-branchsite-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, NetworkaccessBranchSite, error_mapping)

	async def patch(
		self,
		body: NetworkaccessBranchSite,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessBranchSite:
		"""
		Update branchSite (deprecated)
		Update the configuration or properties of a specific branch.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-branchsite-update?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, NetworkaccessBranchSite, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete branchSite (deprecated)
		Delete a specific branch.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-branchsite-delete?view=graph-rest-beta
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



	def with_url(self, raw_url: str) -> ByBranchSiteIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByBranchSiteIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByBranchSiteIdRequest(self.request_adapter, self.path_parameters)

	def connectivity_configuration(self,
		branchSite_id: str,
	) -> ConnectivityConfigurationRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id

		from .connectivity_configuration import ConnectivityConfigurationRequest
		return ConnectivityConfigurationRequest(self.request_adapter, path_parameters)

	def device_links(self,
		branchSite_id: str,
	) -> DeviceLinksRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id

		from .device_links import DeviceLinksRequest
		return DeviceLinksRequest(self.request_adapter, path_parameters)

	def forwarding_profiles(self,
		branchSite_id: str,
	) -> ForwardingProfilesRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id

		from .forwarding_profiles import ForwardingProfilesRequest
		return ForwardingProfilesRequest(self.request_adapter, path_parameters)

