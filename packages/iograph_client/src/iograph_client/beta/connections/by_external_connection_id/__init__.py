# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .schema import SchemaRequest
	from .quota import QuotaRequest
	from .operations import OperationsRequest
	from .items import ItemsRequest
	from .groups import GroupsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.external_connectors_external_connection import ExternalConnectorsExternalConnection


class ByExternalConnectionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/connections/{externalConnection%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExternalConnectorsExternalConnection:
		"""
		Get entity from connections by key
		
		"""
		tags = ['connections.externalConnection']

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
		Update entity in connections
		
		"""
		tags = ['connections.externalConnection']

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
		Delete entity from connections
		
		"""
		tags = ['connections.externalConnection']
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

	def groups(self,
		externalConnection_id: str,
	) -> GroupsRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id

		from .groups import GroupsRequest
		return GroupsRequest(self.request_adapter, path_parameters)

	def items(self,
		externalConnection_id: str,
	) -> ItemsRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id

		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, path_parameters)

	def operations(self,
		externalConnection_id: str,
	) -> OperationsRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def quota(self,
		externalConnection_id: str,
	) -> QuotaRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id

		from .quota import QuotaRequest
		return QuotaRequest(self.request_adapter, path_parameters)

	def schema(self,
		externalConnection_id: str,
	) -> SchemaRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id

		from .schema import SchemaRequest
		return SchemaRequest(self.request_adapter, path_parameters)

