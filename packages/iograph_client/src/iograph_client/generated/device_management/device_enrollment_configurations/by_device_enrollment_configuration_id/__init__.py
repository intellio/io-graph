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
	from .set_priority import SetPriorityRequest
	from .assign import AssignRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.device_enrollment_configuration import DeviceEnrollmentConfiguration
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceEnrollmentConfigurationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceEnrollmentConfigurations/{deviceEnrollmentConfiguration%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceEnrollmentConfiguration:
		"""
		Get deviceEnrollmentPlatformRestrictionsConfiguration
		Read properties and relationships of the deviceEnrollmentPlatformRestrictionsConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-deviceenrollmentplatformrestrictionsconfiguration-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceEnrollmentConfiguration']

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
		return await self.request_adapter.send_async(request_info, DeviceEnrollmentConfiguration, error_mapping)

	async def patch(
		self,
		body: DeviceEnrollmentConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceEnrollmentConfiguration:
		"""
		Update deviceEnrollmentWindowsHelloForBusinessConfiguration
		Update the properties of a deviceEnrollmentWindowsHelloForBusinessConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-deviceenrollmentwindowshelloforbusinessconfiguration-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceEnrollmentConfiguration']

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
		return await self.request_adapter.send_async(request_info, DeviceEnrollmentConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete deviceEnrollmentLimitConfiguration
		Deletes a deviceEnrollmentLimitConfiguration.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-deviceenrollmentlimitconfiguration-delete?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceEnrollmentConfiguration']
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



	def with_url(self, raw_url: str) -> ByDeviceEnrollmentConfigurationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceEnrollmentConfigurationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceEnrollmentConfigurationIdRequest(self.request_adapter, self.path_parameters)

	@property
	def assignments(self,
	) -> AssignmentsRequest:
		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def assign(self,
	) -> AssignRequest:
		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, self.path_parameters)

	@property
	def set_priority(self,
	) -> SetPriorityRequest:
		from .set_priority import SetPriorityRequest
		return SetPriorityRequest(self.request_adapter, self.path_parameters)

