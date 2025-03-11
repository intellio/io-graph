# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_policy_link_id import ByPolicyLinkIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.networkaccess_policy_link import NetworkaccessPolicyLink
from iograph_models.beta.networkaccess_policy_link_collection_response import NetworkaccessPolicyLinkCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class PoliciesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/branches/{branchSite%2Did}/forwardingProfiles/{forwardingProfile%2Did}/policies", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessPolicyLinkCollectionResponse:
		"""
		Get policies from networkAccess
		The traffic forwarding policies associated with this profile.
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
		return await self.request_adapter.send_async(request_info, NetworkaccessPolicyLinkCollectionResponse, error_mapping)

	async def post(
		self,
		body: NetworkaccessPolicyLink,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessPolicyLink:
		"""
		Create new navigation property to policies for networkAccess
		
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
		return await self.request_adapter.send_async(request_info, NetworkaccessPolicyLink, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PoliciesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PoliciesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PoliciesRequest(self.request_adapter, self.path_parameters)

	def by_policy_link_id(self,
		branchSite_id: str,
		forwardingProfile_id: str,
		policyLink_id: str,
	) -> ByPolicyLinkIdRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")
		if forwardingProfile_id is None:
			raise TypeError("forwardingProfile_id cannot be null.")
		if policyLink_id is None:
			raise TypeError("policyLink_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id
		path_parameters["forwardingProfile%2Did"] =  forwardingProfile_id
		path_parameters["policyLink%2Did"] =  policyLink_id

		from .by_policy_link_id import ByPolicyLinkIdRequest
		return ByPolicyLinkIdRequest(self.request_adapter, path_parameters)

	def count(self,
		branchSite_id: str,
		forwardingProfile_id: str,
	) -> CountRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")
		if forwardingProfile_id is None:
			raise TypeError("forwardingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id
		path_parameters["forwardingProfile%2Did"] =  forwardingProfile_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

