# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .parse_expression import ParseExpressionRequest
	from .directories import DirectoriesRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.synchronization_schema import SynchronizationSchema
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class SchemaRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/synchronization/jobs/{synchronizationJob%2Did}/schema", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SynchronizationSchema:
		"""
		Get synchronizationSchema
		Retrieve the schema for a given synchronization job or template.
		Find more info here: https://learn.microsoft.com/graph/api/synchronization-synchronizationschema-get?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.synchronization']

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
		return await self.request_adapter.send_async(request_info, SynchronizationSchema, error_mapping)

	async def patch(
		self,
		body: SynchronizationSchema,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SynchronizationSchema:
		"""
		Update synchronizationSchema
		Update the synchronization schema for a given job or template. This method fully replaces the current schema with the one provided in the request. To update the schema of a template, make the call on the application object. You must be the owner of the application.
		Find more info here: https://learn.microsoft.com/graph/api/synchronization-synchronizationschema-update?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.synchronization']

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
		return await self.request_adapter.send_async(request_info, SynchronizationSchema, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property schema for servicePrincipals
		
		"""
		tags = ['servicePrincipals.synchronization']
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



	def with_url(self, raw_url: str) -> SchemaRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SchemaRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SchemaRequest(self.request_adapter, self.path_parameters)

	@property
	def directories(self,
	) -> DirectoriesRequest:
		from .directories import DirectoriesRequest
		return DirectoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def parse_expression(self,
	) -> ParseExpressionRequest:
		from .parse_expression import ParseExpressionRequest
		return ParseExpressionRequest(self.request_adapter, self.path_parameters)

