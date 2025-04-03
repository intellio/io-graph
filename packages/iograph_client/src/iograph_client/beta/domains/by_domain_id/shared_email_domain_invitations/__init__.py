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
	from .count import CountRequest
	from .by_shared_email_domain_invitation_id import BySharedEmailDomainInvitationIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.shared_email_domain_invitation import SharedEmailDomainInvitation
from iograph_models.beta.shared_email_domain_invitation_collection_response import SharedEmailDomainInvitationCollectionResponse


class SharedEmailDomainInvitationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/domains/{domain%2Did}/sharedEmailDomainInvitations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SharedEmailDomainInvitationCollectionResponse:
		"""
		Get sharedEmailDomainInvitations from domains
		
		"""
		tags = ['domains.sharedEmailDomainInvitation']

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
		return await self.request_adapter.send_async(request_info, SharedEmailDomainInvitationCollectionResponse, error_mapping)

	async def post(
		self,
		body: SharedEmailDomainInvitation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SharedEmailDomainInvitation:
		"""
		Create new navigation property to sharedEmailDomainInvitations for domains
		
		"""
		tags = ['domains.sharedEmailDomainInvitation']

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
		return await self.request_adapter.send_async(request_info, SharedEmailDomainInvitation, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SharedEmailDomainInvitationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SharedEmailDomainInvitationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SharedEmailDomainInvitationsRequest(self.request_adapter, self.path_parameters)

	def by_shared_email_domain_invitation_id(self,
		domain_id: str,
		sharedEmailDomainInvitation_id: str,
	) -> BySharedEmailDomainInvitationIdRequest:
		if domain_id is None:
			raise TypeError("domain_id cannot be null.")
		if sharedEmailDomainInvitation_id is None:
			raise TypeError("sharedEmailDomainInvitation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["domain%2Did"] =  domain_id
		path_parameters["sharedEmailDomainInvitation%2Did"] =  sharedEmailDomainInvitation_id

		from .by_shared_email_domain_invitation_id import BySharedEmailDomainInvitationIdRequest
		return BySharedEmailDomainInvitationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		domain_id: str,
	) -> CountRequest:
		if domain_id is None:
			raise TypeError("domain_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["domain%2Did"] =  domain_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

