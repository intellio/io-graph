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
		self.url_template: str = "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/claimsMappingPolicies/$ref"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> StringCollectionResponse:
		"""
		List assigned claimsMappingPolicy
		List the claimsMappingPolicy objects that are assigned to a servicePrincipal.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-list-claimsmappingpolicies?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.claimsMappingPolicy']

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
		Assign claimsMappingPolicy
		Assign a claimsMappingPolicy to a servicePrincipal.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-post-claimsmappingpolicies?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.claimsMappingPolicy']

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
		Remove claimsMappingPolicy
		Remove a claimsMappingPolicy from a servicePrincipal.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-delete-claimsmappingpolicies?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.claimsMappingPolicy']
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

