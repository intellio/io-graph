# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .external_connectors_add_activities import ExternalConnectorsAddActivitiesRequest
	from .activities import ActivitiesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.external_connectors_external_item import ExternalConnectorsExternalItem


class ByExternalItemIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/connections/{externalConnection%2Did}/items/{externalItem%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

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



	@property
	def activities(self,
	) -> ActivitiesRequest:
		from .activities import ActivitiesRequest
		return ActivitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def external_connectors_add_activities(self,
	) -> ExternalConnectorsAddActivitiesRequest:
		from .external_connectors_add_activities import ExternalConnectorsAddActivitiesRequest
		return ExternalConnectorsAddActivitiesRequest(self.request_adapter, self.path_parameters)

