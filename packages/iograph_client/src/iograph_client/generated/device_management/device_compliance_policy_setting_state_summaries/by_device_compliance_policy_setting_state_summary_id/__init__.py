# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .device_compliance_setting_states import DeviceComplianceSettingStatesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary


class ByDeviceCompliancePolicySettingStateSummaryIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/deviceCompliancePolicySettingStateSummaries/{deviceCompliancePolicySettingStateSummary%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceCompliancePolicySettingStateSummary:
		"""
		Get deviceCompliancePolicySettingStateSummary
		Read properties and relationships of the deviceCompliancePolicySettingStateSummary object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-devicecompliancepolicysettingstatesummary-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceCompliancePolicySettingStateSummary']

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
		return await self.request_adapter.send_async(request_info, DeviceCompliancePolicySettingStateSummary, error_mapping)

	async def patch(
		self,
		body: DeviceCompliancePolicySettingStateSummary,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceCompliancePolicySettingStateSummary:
		"""
		Update deviceCompliancePolicySettingStateSummary
		Update the properties of a deviceCompliancePolicySettingStateSummary object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-devicecompliancepolicysettingstatesummary-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceCompliancePolicySettingStateSummary']

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
		return await self.request_adapter.send_async(request_info, DeviceCompliancePolicySettingStateSummary, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete deviceCompliancePolicySettingStateSummary
		Deletes a deviceCompliancePolicySettingStateSummary.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-devicecompliancepolicysettingstatesummary-delete?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceCompliancePolicySettingStateSummary']
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
	def device_compliance_setting_states(self,
	) -> DeviceComplianceSettingStatesRequest:
		from .device_compliance_setting_states import DeviceComplianceSettingStatesRequest
		return DeviceComplianceSettingStatesRequest(self.request_adapter, self.path_parameters)

