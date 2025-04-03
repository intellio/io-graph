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
	from .get_health_metric_time_series import GetHealthMetricTimeSeriesRequest
	from .get_health_metrics import GetHealthMetricsRequest
	from .generate_server_log_collection_request import GenerateServerLogCollectionRequestRequest
	from .create_server_log_collection_request import CreateServerLogCollectionRequestRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.microsoft_tunnel_server import MicrosoftTunnelServer


class ByMicrosoftTunnelServerIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/microsoftTunnelSites/{microsoftTunnelSite%2Did}/microsoftTunnelServers/{microsoftTunnelServer%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MicrosoftTunnelServer:
		"""
		Get microsoftTunnelServers from deviceManagement
		A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
		"""
		tags = ['deviceManagement.microsoftTunnelSite']

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
		return await self.request_adapter.send_async(request_info, MicrosoftTunnelServer, error_mapping)

	async def patch(
		self,
		body: MicrosoftTunnelServer,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MicrosoftTunnelServer:
		"""
		Update the navigation property microsoftTunnelServers in deviceManagement
		
		"""
		tags = ['deviceManagement.microsoftTunnelSite']

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
		return await self.request_adapter.send_async(request_info, MicrosoftTunnelServer, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property microsoftTunnelServers for deviceManagement
		
		"""
		tags = ['deviceManagement.microsoftTunnelSite']
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



	def with_url(self, raw_url: str) -> ByMicrosoftTunnelServerIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMicrosoftTunnelServerIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMicrosoftTunnelServerIdRequest(self.request_adapter, self.path_parameters)

	def create_server_log_collection_request(self,
		microsoftTunnelSite_id: str,
		microsoftTunnelServer_id: str,
	) -> CreateServerLogCollectionRequestRequest:
		if microsoftTunnelSite_id is None:
			raise TypeError("microsoftTunnelSite_id cannot be null.")
		if microsoftTunnelServer_id is None:
			raise TypeError("microsoftTunnelServer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelSite%2Did"] =  microsoftTunnelSite_id
		path_parameters["microsoftTunnelServer%2Did"] =  microsoftTunnelServer_id

		from .create_server_log_collection_request import CreateServerLogCollectionRequestRequest
		return CreateServerLogCollectionRequestRequest(self.request_adapter, path_parameters)

	def generate_server_log_collection_request(self,
		microsoftTunnelSite_id: str,
		microsoftTunnelServer_id: str,
	) -> GenerateServerLogCollectionRequestRequest:
		if microsoftTunnelSite_id is None:
			raise TypeError("microsoftTunnelSite_id cannot be null.")
		if microsoftTunnelServer_id is None:
			raise TypeError("microsoftTunnelServer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelSite%2Did"] =  microsoftTunnelSite_id
		path_parameters["microsoftTunnelServer%2Did"] =  microsoftTunnelServer_id

		from .generate_server_log_collection_request import GenerateServerLogCollectionRequestRequest
		return GenerateServerLogCollectionRequestRequest(self.request_adapter, path_parameters)

	def get_health_metrics(self,
		microsoftTunnelSite_id: str,
		microsoftTunnelServer_id: str,
	) -> GetHealthMetricsRequest:
		if microsoftTunnelSite_id is None:
			raise TypeError("microsoftTunnelSite_id cannot be null.")
		if microsoftTunnelServer_id is None:
			raise TypeError("microsoftTunnelServer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelSite%2Did"] =  microsoftTunnelSite_id
		path_parameters["microsoftTunnelServer%2Did"] =  microsoftTunnelServer_id

		from .get_health_metrics import GetHealthMetricsRequest
		return GetHealthMetricsRequest(self.request_adapter, path_parameters)

	def get_health_metric_time_series(self,
		microsoftTunnelSite_id: str,
		microsoftTunnelServer_id: str,
	) -> GetHealthMetricTimeSeriesRequest:
		if microsoftTunnelSite_id is None:
			raise TypeError("microsoftTunnelSite_id cannot be null.")
		if microsoftTunnelServer_id is None:
			raise TypeError("microsoftTunnelServer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelSite%2Did"] =  microsoftTunnelSite_id
		path_parameters["microsoftTunnelServer%2Did"] =  microsoftTunnelServer_id

		from .get_health_metric_time_series import GetHealthMetricTimeSeriesRequest
		return GetHealthMetricTimeSeriesRequest(self.request_adapter, path_parameters)

