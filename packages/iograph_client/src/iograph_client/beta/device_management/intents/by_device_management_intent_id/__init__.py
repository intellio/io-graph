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
	from .user_state_summary import UserStateSummaryRequest
	from .user_states import UserStatesRequest
	from .settings import SettingsRequest
	from .update_settings import UpdateSettingsRequest
	from .migrate_to_template import MigrateToTemplateRequest
	from .get_customized_settings import GetCustomizedSettingsRequest
	from .create_copy import CreateCopyRequest
	from .compare_with_templateid import CompareWithTemplateIdRequest
	from .assign import AssignRequest
	from .device_state_summary import DeviceStateSummaryRequest
	from .device_states import DeviceStatesRequest
	from .device_setting_state_summaries import DeviceSettingStateSummariesRequest
	from .categories import CategoriesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_intent import DeviceManagementIntent
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceManagementIntentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/intents/{deviceManagementIntent%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementIntent:
		"""
		Get intents from deviceManagement
		The device management intents
		"""
		tags = ['deviceManagement.deviceManagementIntent']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementIntent, error_mapping)

	async def patch(
		self,
		body: DeviceManagementIntent,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementIntent:
		"""
		Update the navigation property intents in deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementIntent']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementIntent, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property intents for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementIntent']
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



	def with_url(self, raw_url: str) -> ByDeviceManagementIntentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceManagementIntentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceManagementIntentIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		deviceManagementIntent_id: str,
	) -> AssignmentsRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def categories(self,
		deviceManagementIntent_id: str,
	) -> CategoriesRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .categories import CategoriesRequest
		return CategoriesRequest(self.request_adapter, path_parameters)

	def device_setting_state_summaries(self,
		deviceManagementIntent_id: str,
	) -> DeviceSettingStateSummariesRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .device_setting_state_summaries import DeviceSettingStateSummariesRequest
		return DeviceSettingStateSummariesRequest(self.request_adapter, path_parameters)

	def device_states(self,
		deviceManagementIntent_id: str,
	) -> DeviceStatesRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .device_states import DeviceStatesRequest
		return DeviceStatesRequest(self.request_adapter, path_parameters)

	def device_state_summary(self,
		deviceManagementIntent_id: str,
	) -> DeviceStateSummaryRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .device_state_summary import DeviceStateSummaryRequest
		return DeviceStateSummaryRequest(self.request_adapter, path_parameters)

	def assign(self,
		deviceManagementIntent_id: str,
	) -> AssignRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

	def compare_with_templateid(self,
		deviceManagementIntent_id: str,
		templateId: str,
	) -> CompareWithTemplateIdRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")
		if templateId is None:
			raise TypeError("templateId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id
		path_parameters["templateId"] =  templateId

		from .compare_with_templateid import CompareWithTemplateIdRequest
		return CompareWithTemplateIdRequest(self.request_adapter, path_parameters)

	def create_copy(self,
		deviceManagementIntent_id: str,
	) -> CreateCopyRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .create_copy import CreateCopyRequest
		return CreateCopyRequest(self.request_adapter, path_parameters)

	def get_customized_settings(self,
		deviceManagementIntent_id: str,
	) -> GetCustomizedSettingsRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .get_customized_settings import GetCustomizedSettingsRequest
		return GetCustomizedSettingsRequest(self.request_adapter, path_parameters)

	def migrate_to_template(self,
		deviceManagementIntent_id: str,
	) -> MigrateToTemplateRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .migrate_to_template import MigrateToTemplateRequest
		return MigrateToTemplateRequest(self.request_adapter, path_parameters)

	def update_settings(self,
		deviceManagementIntent_id: str,
	) -> UpdateSettingsRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .update_settings import UpdateSettingsRequest
		return UpdateSettingsRequest(self.request_adapter, path_parameters)

	def settings(self,
		deviceManagementIntent_id: str,
	) -> SettingsRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, path_parameters)

	def user_states(self,
		deviceManagementIntent_id: str,
	) -> UserStatesRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .user_states import UserStatesRequest
		return UserStatesRequest(self.request_adapter, path_parameters)

	def user_state_summary(self,
		deviceManagementIntent_id: str,
	) -> UserStateSummaryRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .user_state_summary import UserStateSummaryRequest
		return UserStateSummaryRequest(self.request_adapter, path_parameters)

