# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .external_connectors_add_activities import ExternalConnectorsAddActivitiesRequest
	from .activities import ActivitiesRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.external_connectors_external_item import ExternalConnectorsExternalItem
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByExternalItemIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/external/connections/{externalConnection%2Did}/items/{externalItem%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExternalConnectorsExternalItem:
		"""
		Get externalItem
		Get the properties and relationships of an externalitem object. This API is provided for diagnostic purposes only. It isn't intended to be used for any other purpose. Repeated requests to this API might result in 429 HTTP errors.
		Find more info here: https://learn.microsoft.com/graph/api/externalconnectors-externalitem-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsExternalItem, error_mapping)

	async def put(
		self,
		body: ExternalConnectorsExternalItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ExternalConnectorsExternalItem:
		"""
		Update externalItem
		Update the properties of an externalitem.
		Find more info here: https://learn.microsoft.com/graph/api/externalconnectors-externalitem-update?view=graph-rest-beta
		"""
		tags = ['external.externalConnection']

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
		Delete externalItem
		Delete an externalitem.
		Find more info here: https://learn.microsoft.com/graph/api/externalconnectors-externalitem-delete?view=graph-rest-beta
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

