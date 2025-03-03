# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .schema import SchemaRequest
	from .operations import OperationsRequest
	from .items import ItemsRequest
	from .groups import GroupsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.external_connectors_external_connection import ExternalConnectorsExternalConnection
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByExternalConnectionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/external/connections/{externalConnection%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExternalConnectorsExternalConnection:
		"""
		Get externalConnection
		Read the properties and relationships of an externalConnection object.
		Find more info here: https://learn.microsoft.com/graph/api/externalconnectors-externalconnection-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsExternalConnection, error_mapping)

	async def patch(
		self,
		body: ExternalConnectorsExternalConnection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ExternalConnectorsExternalConnection:
		"""
		Update externalConnection
		Update the properties of an externalConnection object.
		Find more info here: https://learn.microsoft.com/graph/api/externalconnectors-externalconnection-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsExternalConnection, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete externalConnection
		Deletes an externalConnection object.
		Find more info here: https://learn.microsoft.com/graph/api/externalconnectors-externalconnection-delete?view=graph-rest-1.0
		"""
		tags = ['external.externalConnection']
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



	def with_url(self, raw_url: str) -> ByExternalConnectionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByExternalConnectionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByExternalConnectionIdRequest(self.request_adapter, self.path_parameters)

	@property
	def groups(self,
	) -> GroupsRequest:
		from .groups import GroupsRequest
		return GroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def items(self,
	) -> ItemsRequest:
		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def schema(self,
	) -> SchemaRequest:
		from .schema import SchemaRequest
		return SchemaRequest(self.request_adapter, self.path_parameters)

