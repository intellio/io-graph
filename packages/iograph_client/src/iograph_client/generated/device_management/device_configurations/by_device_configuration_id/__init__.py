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
	from .user_status_overview import UserStatusOverviewRequest
	from .user_statuses import UserStatusesRequest
	from .assign import AssignRequest
	from .device_status_overview import DeviceStatusOverviewRequest
	from .device_statuses import DeviceStatusesRequest
	from .device_setting_state_summaries import DeviceSettingStateSummariesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.device_configuration import DeviceConfiguration
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceConfigurationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceConfigurations/{deviceConfiguration%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceConfiguration:
		"""
		Get windowsPhone81GeneralConfiguration
		Read properties and relationships of the windowsPhone81GeneralConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-windowsphone81generalconfiguration-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceConfiguration']

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
		return await self.request_adapter.send_async(request_info, DeviceConfiguration, error_mapping)

	async def patch(
		self,
		body: DeviceConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceConfiguration:
		"""
		Update windows10EnterpriseModernAppManagementConfiguration
		Update the properties of a windows10EnterpriseModernAppManagementConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-windows10enterprisemodernappmanagementconfiguration-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceConfiguration']

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
		return await self.request_adapter.send_async(request_info, DeviceConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete iosCustomConfiguration
		Deletes a iosCustomConfiguration.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-ioscustomconfiguration-delete?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceConfiguration']
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



	def with_url(self, raw_url: str) -> ByDeviceConfigurationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceConfigurationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceConfigurationIdRequest(self.request_adapter, self.path_parameters)

	@property
	def assignments(self,
	) -> AssignmentsRequest:
		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_setting_state_summaries(self,
	) -> DeviceSettingStateSummariesRequest:
		from .device_setting_state_summaries import DeviceSettingStateSummariesRequest
		return DeviceSettingStateSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_statuses(self,
	) -> DeviceStatusesRequest:
		from .device_statuses import DeviceStatusesRequest
		return DeviceStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_status_overview(self,
	) -> DeviceStatusOverviewRequest:
		from .device_status_overview import DeviceStatusOverviewRequest
		return DeviceStatusOverviewRequest(self.request_adapter, self.path_parameters)

	@property
	def assign(self,
	) -> AssignRequest:
		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, self.path_parameters)

	@property
	def user_statuses(self,
	) -> UserStatusesRequest:
		from .user_statuses import UserStatusesRequest
		return UserStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_status_overview(self,
	) -> UserStatusOverviewRequest:
		from .user_status_overview import UserStatusOverviewRequest
		return UserStatusOverviewRequest(self.request_adapter, self.path_parameters)

