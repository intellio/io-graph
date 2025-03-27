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
	from .run_health_checks import RunHealthChecksRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByCloudPcOnPremisesConnectionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/onPremisesConnections/{cloudPcOnPremisesConnection%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudPcOnPremisesConnection:
		"""
		Get cloudPcOnPremisesConnection
		Read the properties and relationships of the cloudPcOnPremisesConnection object.
		Find more info here: https://learn.microsoft.com/graph/api/cloudpconpremisesconnection-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPcOnPremisesConnection, error_mapping)

	async def patch(
		self,
		body: CloudPcOnPremisesConnection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPcOnPremisesConnection:
		"""
		Update cloudPcOnPremisesConnection
		Update the properties of a cloudPcOnPremisesConnection object.
		Find more info here: https://learn.microsoft.com/graph/api/cloudpconpremisesconnection-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPcOnPremisesConnection, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete cloudPcOnPremisesConnection
		Delete a specific cloudPcOnPremisesConnection object. When you delete an Azure network connection, permissions to the service are removed from the specified Azure resources. You cannot delete an Azure network connection when it's in use, as indicated by the inUse property.
		Find more info here: https://learn.microsoft.com/graph/api/cloudpconpremisesconnection-delete?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.virtualEndpoint']
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



	def with_url(self, raw_url: str) -> ByCloudPcOnPremisesConnectionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCloudPcOnPremisesConnectionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCloudPcOnPremisesConnectionIdRequest(self.request_adapter, self.path_parameters)

	def run_health_checks(self,
		cloudPcOnPremisesConnection_id: str,
	) -> RunHealthChecksRequest:
		if cloudPcOnPremisesConnection_id is None:
			raise TypeError("cloudPcOnPremisesConnection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPcOnPremisesConnection%2Did"] =  cloudPcOnPremisesConnection_id

		from .run_health_checks import RunHealthChecksRequest
		return RunHealthChecksRequest(self.request_adapter, path_parameters)

