# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_device_management_configuration_setting_definition_id import ByDeviceManagementConfigurationSettingDefinitionIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_configuration_setting_definition_collection_response import DeviceManagementConfigurationSettingDefinitionCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SettingDefinitionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/compliancePolicies/{deviceManagementCompliancePolicy%2Did}/settings/{deviceManagementConfigurationSetting%2Did}/settingDefinitions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementConfigurationSettingDefinitionCollectionResponse:
		"""
		Get settingDefinitions from deviceManagement
		List of related Setting Definitions. This property is read-only.
		"""
		tags = ['deviceManagement.deviceManagementCompliancePolicy']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementConfigurationSettingDefinitionCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> SettingDefinitionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SettingDefinitionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SettingDefinitionsRequest(self.request_adapter, self.path_parameters)

	def by_device_management_configuration_setting_definition_id(self,
		deviceManagementCompliancePolicy_id: str,
		deviceManagementConfigurationSetting_id: str,
		deviceManagementConfigurationSettingDefinition_id: str,
	) -> ByDeviceManagementConfigurationSettingDefinitionIdRequest:
		if deviceManagementCompliancePolicy_id is None:
			raise TypeError("deviceManagementCompliancePolicy_id cannot be null.")
		if deviceManagementConfigurationSetting_id is None:
			raise TypeError("deviceManagementConfigurationSetting_id cannot be null.")
		if deviceManagementConfigurationSettingDefinition_id is None:
			raise TypeError("deviceManagementConfigurationSettingDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementCompliancePolicy%2Did"] =  deviceManagementCompliancePolicy_id
		path_parameters["deviceManagementConfigurationSetting%2Did"] =  deviceManagementConfigurationSetting_id
		path_parameters["deviceManagementConfigurationSettingDefinition%2Did"] =  deviceManagementConfigurationSettingDefinition_id

		from .by_device_management_configuration_setting_definition_id import ByDeviceManagementConfigurationSettingDefinitionIdRequest
		return ByDeviceManagementConfigurationSettingDefinitionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		deviceManagementCompliancePolicy_id: str,
		deviceManagementConfigurationSetting_id: str,
	) -> CountRequest:
		if deviceManagementCompliancePolicy_id is None:
			raise TypeError("deviceManagementCompliancePolicy_id cannot be null.")
		if deviceManagementConfigurationSetting_id is None:
			raise TypeError("deviceManagementConfigurationSetting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementCompliancePolicy%2Did"] =  deviceManagementCompliancePolicy_id
		path_parameters["deviceManagementConfigurationSetting%2Did"] =  deviceManagementConfigurationSetting_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

