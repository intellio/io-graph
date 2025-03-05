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
	from .user_status_overview import UserStatusOverviewRequest
	from .user_statuses import UserStatusesRequest
	from .get_oma_setting_plain_text_value_with_secretreferencevalueid import GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequest
	from .assign import AssignRequest
	from .device_status_overview import DeviceStatusOverviewRequest
	from .device_statuses import DeviceStatusesRequest
	from .device_setting_state_summaries import DeviceSettingStateSummariesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.device_configuration import DeviceConfiguration


class ByDeviceConfigurationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/deviceConfigurations/{deviceConfiguration%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceConfiguration:
		"""
		Get androidWorkProfileCustomConfiguration
		Read properties and relationships of the androidWorkProfileCustomConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-androidworkprofilecustomconfiguration-get?view=graph-rest-1.0
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
		Update windows10SecureAssessmentConfiguration
		Update the properties of a windows10SecureAssessmentConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-windows10secureassessmentconfiguration-update?view=graph-rest-1.0
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
		Delete windowsDefenderAdvancedThreatProtectionConfiguration
		Deletes a windowsDefenderAdvancedThreatProtectionConfiguration.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-windowsdefenderadvancedthreatprotectionconfiguration-delete?view=graph-rest-1.0
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

	def assignments(self,
		deviceConfiguration_id: str,
	) -> AssignmentsRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def device_setting_state_summaries(self,
		deviceConfiguration_id: str,
	) -> DeviceSettingStateSummariesRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id

		from .device_setting_state_summaries import DeviceSettingStateSummariesRequest
		return DeviceSettingStateSummariesRequest(self.request_adapter, path_parameters)

	def device_statuses(self,
		deviceConfiguration_id: str,
	) -> DeviceStatusesRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id

		from .device_statuses import DeviceStatusesRequest
		return DeviceStatusesRequest(self.request_adapter, path_parameters)

	def device_status_overview(self,
		deviceConfiguration_id: str,
	) -> DeviceStatusOverviewRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id

		from .device_status_overview import DeviceStatusOverviewRequest
		return DeviceStatusOverviewRequest(self.request_adapter, path_parameters)

	def assign(self,
		deviceConfiguration_id: str,
	) -> AssignRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

	def get_oma_setting_plain_text_value_with_secretreferencevalueid(self,
		deviceConfiguration_id: str,
		secretReferenceValueId: str,
	) -> GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")
		if secretReferenceValueId is None:
			raise TypeError("secretReferenceValueId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id
		path_parameters["secretReferenceValueId"] =  secretReferenceValueId

		from .get_oma_setting_plain_text_value_with_secretreferencevalueid import GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequest
		return GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequest(self.request_adapter, path_parameters)

	def user_statuses(self,
		deviceConfiguration_id: str,
	) -> UserStatusesRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id

		from .user_statuses import UserStatusesRequest
		return UserStatusesRequest(self.request_adapter, path_parameters)

	def user_status_overview(self,
		deviceConfiguration_id: str,
	) -> UserStatusOverviewRequest:
		if deviceConfiguration_id is None:
			raise TypeError("deviceConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceConfiguration%2Did"] =  deviceConfiguration_id

		from .user_status_overview import UserStatusOverviewRequest
		return UserStatusOverviewRequest(self.request_adapter, path_parameters)

