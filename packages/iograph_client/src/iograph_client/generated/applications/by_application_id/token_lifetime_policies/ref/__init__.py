# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.string_collection_response import StringCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.reference_create import ReferenceCreate


class RefRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/applications/{application%2Did}/tokenLifetimePolicies/$ref"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> StringCollectionResponse:
		"""
		List assigned tokenLifetimePolicies
		List the tokenLifetimePolicy objects that are assigned to an application. Only one object is returned in the collection because only one tokenLifetimePolicy can be assigned to an application.
		Find more info here: https://learn.microsoft.com/graph/api/application-list-tokenlifetimepolicies?view=graph-rest-1.0
		"""
		tags = ['applications.tokenLifetimePolicy']

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
		Assign tokenLifetimePolicy
		Assign a tokenLifetimePolicy to an application. You can have multiple tokenLifetimePolicy policies in a tenant but can assign only one tokenLifetimePolicy per application.
		Find more info here: https://learn.microsoft.com/graph/api/application-post-tokenlifetimepolicies?view=graph-rest-1.0
		"""
		tags = ['applications.tokenLifetimePolicy']

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
		Remove tokenLifetimePolicy
		Remove a tokenLifetimePolicy from an application.
		Find more info here: https://learn.microsoft.com/graph/api/application-delete-tokenlifetimepolicies?view=graph-rest-1.0
		"""
		tags = ['applications.tokenLifetimePolicy']
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

