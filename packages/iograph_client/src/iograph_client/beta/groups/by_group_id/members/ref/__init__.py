# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.reference_create import ReferenceCreate
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.string_collection_response import StringCollectionResponse


class RefRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/members/$ref", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> StringCollectionResponse:
		"""
		List group members
		Get a list of the group's direct members. A group can have users, contacts, devices, service principals, and other groups as members. This operation isn't transitive.
		Find more info here: https://learn.microsoft.com/graph/api/group-list-members?view=graph-rest-beta
		"""
		tags = ['groups.directoryObject']
		header_parameters = [{'name': 'ConsistencyLevel', 'in': 'header', 'description': 'Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries', 'schema': {'type': 'string'}, 'examples': {'example-1': {'description': "$search and $count queries require the client to set the ConsistencyLevel HTTP header to 'eventual'.", 'value': 'eventual'}}}]

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
		return await self.request_adapter.send_async(request_info, StringCollectionResponse, error_mapping)

	async def post(
		self,
		body: ReferenceCreate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Add members
		Add a member to a security or Microsoft 365 group. When using the API to add multiple members in one request, you can add up to only 20 members.  The following table shows the types of members that can be added to either security groups or Microsoft 365 groups.
		Find more info here: https://learn.microsoft.com/graph/api/group-post-members?view=graph-rest-beta
		"""
		tags = ['groups.directoryObject']

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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[DeleteQueryParams]] = None,
	) -> None:
		"""
		Remove member
		Remove a member from a group via the members navigation property. You can't remove a member from groups with dynamic memberships.
		Find more info here: https://learn.microsoft.com/graph/api/group-delete-members?view=graph-rest-beta
		"""
		tags = ['groups.directoryObject']
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
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")


	class DeleteQueryParams(BaseModel):
		id: str = Field(default=None,serialization_alias="%40id")

	def with_url(self, raw_url: str) -> RefRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RefRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RefRequest(self.request_adapter, self.path_parameters)

