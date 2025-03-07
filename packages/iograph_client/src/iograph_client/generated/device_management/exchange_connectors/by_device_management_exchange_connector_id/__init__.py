# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sync import SyncRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.device_management_exchange_connector import DeviceManagementExchangeConnector
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceManagementExchangeConnectorIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/exchangeConnectors/{deviceManagementExchangeConnector%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementExchangeConnector:
		"""
		Get deviceManagementExchangeConnector
		Read properties and relationships of the deviceManagementExchangeConnector object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-devicemanagementexchangeconnector-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagementExchangeConnector']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementExchangeConnector, error_mapping)

	async def patch(
		self,
		body: DeviceManagementExchangeConnector,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementExchangeConnector:
		"""
		Update deviceManagementExchangeConnector
		Update the properties of a deviceManagementExchangeConnector object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-devicemanagementexchangeconnector-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagementExchangeConnector']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementExchangeConnector, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete deviceManagementExchangeConnector
		Deletes a deviceManagementExchangeConnector.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-devicemanagementexchangeconnector-delete?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagementExchangeConnector']
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



	def with_url(self, raw_url: str) -> ByDeviceManagementExchangeConnectorIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceManagementExchangeConnectorIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceManagementExchangeConnectorIdRequest(self.request_adapter, self.path_parameters)

	def sync(self,
		deviceManagementExchangeConnector_id: str,
	) -> SyncRequest:
		if deviceManagementExchangeConnector_id is None:
			raise TypeError("deviceManagementExchangeConnector_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementExchangeConnector%2Did"] =  deviceManagementExchangeConnector_id

		from .sync import SyncRequest
		return SyncRequest(self.request_adapter, path_parameters)

