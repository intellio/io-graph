# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .has_active_deployments import HasActiveDeploymentsRequest
	from .disconnect import DisconnectRequest
	from .connect import ConnectRequest
	from .approve_fota_apps import ApproveFotaAppsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.zebra_fota_connector import ZebraFotaConnector


class ZebraFotaConnectorRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/zebraFotaConnector", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ZebraFotaConnector:
		"""
		Get zebraFotaConnector from deviceManagement
		The singleton ZebraFotaConnector associated with account.
		"""
		tags = ['deviceManagement.zebraFotaConnector']

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
		return await self.request_adapter.send_async(request_info, ZebraFotaConnector, error_mapping)

	async def patch(
		self,
		body: ZebraFotaConnector,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ZebraFotaConnector:
		"""
		Update the navigation property zebraFotaConnector in deviceManagement
		
		"""
		tags = ['deviceManagement.zebraFotaConnector']

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
		return await self.request_adapter.send_async(request_info, ZebraFotaConnector, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property zebraFotaConnector for deviceManagement
		
		"""
		tags = ['deviceManagement.zebraFotaConnector']
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



	def with_url(self, raw_url: str) -> ZebraFotaConnectorRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ZebraFotaConnectorRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ZebraFotaConnectorRequest(self.request_adapter, self.path_parameters)

	@property
	def approve_fota_apps(self,
	) -> ApproveFotaAppsRequest:
		from .approve_fota_apps import ApproveFotaAppsRequest
		return ApproveFotaAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def connect(self,
	) -> ConnectRequest:
		from .connect import ConnectRequest
		return ConnectRequest(self.request_adapter, self.path_parameters)

	@property
	def disconnect(self,
	) -> DisconnectRequest:
		from .disconnect import DisconnectRequest
		return DisconnectRequest(self.request_adapter, self.path_parameters)

	@property
	def has_active_deployments(self,
	) -> HasActiveDeploymentsRequest:
		from .has_active_deployments import HasActiveDeploymentsRequest
		return HasActiveDeploymentsRequest(self.request_adapter, self.path_parameters)

