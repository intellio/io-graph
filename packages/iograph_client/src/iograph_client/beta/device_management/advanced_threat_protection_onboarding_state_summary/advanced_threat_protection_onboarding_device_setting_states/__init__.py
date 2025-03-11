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
	from .count import CountRequest
	from .by_advanced_threat_protection_onboarding_device_setting_state_id import ByAdvancedThreatProtectionOnboardingDeviceSettingStateIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.advanced_threat_protection_onboarding_device_setting_state import AdvancedThreatProtectionOnboardingDeviceSettingState
from iograph_models.beta.advanced_threat_protection_onboarding_device_setting_state_collection_response import AdvancedThreatProtectionOnboardingDeviceSettingStateCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AdvancedThreatProtectionOnboardingDeviceSettingStatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/advancedThreatProtectionOnboardingStateSummary/advancedThreatProtectionOnboardingDeviceSettingStates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AdvancedThreatProtectionOnboardingDeviceSettingStateCollectionResponse:
		"""
		Get advancedThreatProtectionOnboardingDeviceSettingStates from deviceManagement
		
		"""
		tags = ['deviceManagement.advancedThreatProtectionOnboardingStateSummary']

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
		return await self.request_adapter.send_async(request_info, AdvancedThreatProtectionOnboardingDeviceSettingStateCollectionResponse, error_mapping)

	async def post(
		self,
		body: AdvancedThreatProtectionOnboardingDeviceSettingState,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AdvancedThreatProtectionOnboardingDeviceSettingState:
		"""
		Create new navigation property to advancedThreatProtectionOnboardingDeviceSettingStates for deviceManagement
		
		"""
		tags = ['deviceManagement.advancedThreatProtectionOnboardingStateSummary']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, AdvancedThreatProtectionOnboardingDeviceSettingState, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AdvancedThreatProtectionOnboardingDeviceSettingStatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AdvancedThreatProtectionOnboardingDeviceSettingStatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AdvancedThreatProtectionOnboardingDeviceSettingStatesRequest(self.request_adapter, self.path_parameters)

	def by_advanced_threat_protection_onboarding_device_setting_state_id(self,
		advancedThreatProtectionOnboardingDeviceSettingState_id: str,
	) -> ByAdvancedThreatProtectionOnboardingDeviceSettingStateIdRequest:
		if advancedThreatProtectionOnboardingDeviceSettingState_id is None:
			raise TypeError("advancedThreatProtectionOnboardingDeviceSettingState_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["advancedThreatProtectionOnboardingDeviceSettingState%2Did"] =  advancedThreatProtectionOnboardingDeviceSettingState_id

		from .by_advanced_threat_protection_onboarding_device_setting_state_id import ByAdvancedThreatProtectionOnboardingDeviceSettingStateIdRequest
		return ByAdvancedThreatProtectionOnboardingDeviceSettingStateIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

