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
from iograph_models.v1.external_connectors_schema import ExternalConnectorsSchema
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class SchemaRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/external/connections/{externalConnection%2Did}/schema", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExternalConnectorsSchema:
		"""
		Get schema
		Read the properties and relationships of a schema object.
		Find more info here: https://learn.microsoft.com/graph/api/externalconnectors-schema-get?view=graph-rest-1.0
		"""
		tags = ['external.externalConnection']

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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsSchema, error_mapping)

	async def patch(
		self,
		body: ExternalConnectorsSchema,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ExternalConnectorsSchema:
		"""
		Create or update schema
		Create a new or update an existing schema for a Microsoft Search connection.
		Find more info here: https://learn.microsoft.com/graph/api/externalconnectors-externalconnection-patch-schema?view=graph-rest-1.0
		"""
		tags = ['external.externalConnection']

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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsSchema, error_mapping)

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

