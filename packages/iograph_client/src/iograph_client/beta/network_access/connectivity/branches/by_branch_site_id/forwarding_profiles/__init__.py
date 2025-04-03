# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_forwarding_profile_id import ByForwardingProfileIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.networkaccess_forwarding_profile import NetworkaccessForwardingProfile
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.networkaccess_forwarding_profile_collection_response import NetworkaccessForwardingProfileCollectionResponse


class ForwardingProfilesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/branches/{branchSite%2Did}/forwardingProfiles", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessForwardingProfileCollectionResponse:
		"""
		List forwardingProfiles (deprecated)
		Retrieve a list of traffic forwarding profiles associated with a branch.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-branchsite-list-forwardingprofiles?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, NetworkaccessForwardingProfileCollectionResponse, error_mapping)

	async def post(
		self,
		body: NetworkaccessForwardingProfile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessForwardingProfile:
		"""
		Create new navigation property to forwardingProfiles for networkAccess
		
		"""
		tags = ['networkAccess.connectivity']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, NetworkaccessForwardingProfile, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ForwardingProfilesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ForwardingProfilesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ForwardingProfilesRequest(self.request_adapter, self.path_parameters)

	def by_forwarding_profile_id(self,
		branchSite_id: str,
		forwardingProfile_id: str,
	) -> ByForwardingProfileIdRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")
		if forwardingProfile_id is None:
			raise TypeError("forwardingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id
		path_parameters["forwardingProfile%2Did"] =  forwardingProfile_id

		from .by_forwarding_profile_id import ByForwardingProfileIdRequest
		return ByForwardingProfileIdRequest(self.request_adapter, path_parameters)

	def count(self,
		branchSite_id: str,
	) -> CountRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

