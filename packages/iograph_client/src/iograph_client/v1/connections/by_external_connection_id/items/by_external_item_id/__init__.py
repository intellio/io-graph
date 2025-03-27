# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .external_connectors_add_activities import ExternalConnectorsAddActivitiesRequest
	from .activities import ActivitiesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.external_connectors_external_item import ExternalConnectorsExternalItem


class ByExternalItemIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/connections/{externalConnection%2Did}/items/{externalItem%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExternalConnectorsExternalItem:
		"""
		Get items from connections
		
		"""
		tags = ['connections.externalItem']

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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsExternalItem, error_mapping)

	async def put(
		self,
		body: ExternalConnectorsExternalItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ExternalConnectorsExternalItem:
		"""
		Update the navigation property items in connections
		
		"""
		tags = ['connections.externalItem']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PUT,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, ExternalConnectorsExternalItem, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property items for connections
		
		"""
		tags = ['connections.externalItem']
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



	def with_url(self, raw_url: str) -> ByExternalItemIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByExternalItemIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByExternalItemIdRequest(self.request_adapter, self.path_parameters)

	def activities(self,
		externalConnection_id: str,
		externalItem_id: str,
	) -> ActivitiesRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")
		if externalItem_id is None:
			raise TypeError("externalItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id
		path_parameters["externalItem%2Did"] =  externalItem_id

		from .activities import ActivitiesRequest
		return ActivitiesRequest(self.request_adapter, path_parameters)

	def external_connectors_add_activities(self,
		externalConnection_id: str,
		externalItem_id: str,
	) -> ExternalConnectorsAddActivitiesRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")
		if externalItem_id is None:
			raise TypeError("externalItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id
		path_parameters["externalItem%2Did"] =  externalItem_id

		from .external_connectors_add_activities import ExternalConnectorsAddActivitiesRequest
		return ExternalConnectorsAddActivitiesRequest(self.request_adapter, path_parameters)

