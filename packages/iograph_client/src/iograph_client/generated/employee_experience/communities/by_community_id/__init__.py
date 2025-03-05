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
	from .owners_with_userprincipalname import OwnersWithUserPrincipalNameRequest
	from .owners import OwnersRequest
	from .group import GroupRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.community import Community


class ByCommunityIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/employeeExperience/communities/{community%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Community:
		"""
		Get community
		Read the properties and relationships of a community object.
		Find more info here: https://learn.microsoft.com/graph/api/community-get?view=graph-rest-1.0
		"""
		tags = ['employeeExperience.community']

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
		return await self.request_adapter.send_async(request_info, Community, error_mapping)

	async def patch(
		self,
		body: Community,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Community:
		"""
		Update community
		Update the properties of an existing Viva Engage community.
		Find more info here: https://learn.microsoft.com/graph/api/community-update?view=graph-rest-1.0
		"""
		tags = ['employeeExperience.community']

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
		return await self.request_adapter.send_async(request_info, Community, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete community
		Delete a Viva Engage community along with all associated Microsoft 365 content, including the connected Microsoft 365 group, OneNote notebook, and Planner plans. For more information, see What happens if I delete a Viva Engage community connected to Microsoft 365 groups.
		Find more info here: https://learn.microsoft.com/graph/api/community-delete?view=graph-rest-1.0
		"""
		tags = ['employeeExperience.community']
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



	def with_url(self, raw_url: str) -> ByCommunityIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCommunityIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCommunityIdRequest(self.request_adapter, self.path_parameters)

	def group(self,
		community_id: str,
	) -> GroupRequest:
		if community_id is None:
			raise TypeError("community_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["community%2Did"] =  community_id

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

	def owners(self,
		community_id: str,
	) -> OwnersRequest:
		if community_id is None:
			raise TypeError("community_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["community%2Did"] =  community_id

		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, path_parameters)

	def owners_with_userprincipalname(self,
		community_id: str,
		userPrincipalName: str,
	) -> OwnersWithUserPrincipalNameRequest:
		if community_id is None:
			raise TypeError("community_id cannot be null.")
		if userPrincipalName is None:
			raise TypeError("userPrincipalName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["community%2Did"] =  community_id
		path_parameters["userPrincipalName"] =  userPrincipalName

		from .owners_with_userprincipalname import OwnersWithUserPrincipalNameRequest
		return OwnersWithUserPrincipalNameRequest(self.request_adapter, path_parameters)

