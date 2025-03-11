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
	from .get_health_metric_time_series import GetHealthMetricTimeSeriesRequest
	from .get_health_metrics import GetHealthMetricsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.certificate_connector_details import CertificateConnectorDetails
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByCertificateConnectorDetailsIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/certificateConnectorDetails/{certificateConnectorDetails%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CertificateConnectorDetails:
		"""
		Get certificateConnectorDetails from deviceManagement
		Collection of certificate connector details, each associated with a corresponding Intune Certificate Connector.
		"""
		tags = ['deviceManagement.certificateConnectorDetails']

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
		return await self.request_adapter.send_async(request_info, CertificateConnectorDetails, error_mapping)

	async def patch(
		self,
		body: CertificateConnectorDetails,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CertificateConnectorDetails:
		"""
		Update the navigation property certificateConnectorDetails in deviceManagement
		
		"""
		tags = ['deviceManagement.certificateConnectorDetails']

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
		return await self.request_adapter.send_async(request_info, CertificateConnectorDetails, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property certificateConnectorDetails for deviceManagement
		
		"""
		tags = ['deviceManagement.certificateConnectorDetails']
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



	def with_url(self, raw_url: str) -> ByCertificateConnectorDetailsIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCertificateConnectorDetailsIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCertificateConnectorDetailsIdRequest(self.request_adapter, self.path_parameters)

	def get_health_metrics(self,
		certificateConnectorDetails_id: str,
	) -> GetHealthMetricsRequest:
		if certificateConnectorDetails_id is None:
			raise TypeError("certificateConnectorDetails_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["certificateConnectorDetails%2Did"] =  certificateConnectorDetails_id

		from .get_health_metrics import GetHealthMetricsRequest
		return GetHealthMetricsRequest(self.request_adapter, path_parameters)

	def get_health_metric_time_series(self,
		certificateConnectorDetails_id: str,
	) -> GetHealthMetricTimeSeriesRequest:
		if certificateConnectorDetails_id is None:
			raise TypeError("certificateConnectorDetails_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["certificateConnectorDetails%2Did"] =  certificateConnectorDetails_id

		from .get_health_metric_time_series import GetHealthMetricTimeSeriesRequest
		return GetHealthMetricTimeSeriesRequest(self.request_adapter, path_parameters)

