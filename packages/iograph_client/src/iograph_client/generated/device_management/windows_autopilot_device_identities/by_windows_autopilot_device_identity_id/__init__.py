# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .update_device_properties import UpdateDevicePropertiesRequest
	from .unassign_user_from_device import UnassignUserFromDeviceRequest
	from .assign_user_to_device import AssignUserToDeviceRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity


class ByWindowsAutopilotDeviceIdentityIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/windowsAutopilotDeviceIdentities/{windowsAutopilotDeviceIdentity%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsAutopilotDeviceIdentity:
		"""
		Get windowsAutopilotDeviceIdentity
		Read properties and relationships of the windowsAutopilotDeviceIdentity object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-enrollment-windowsautopilotdeviceidentity-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.windowsAutopilotDeviceIdentity']

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
		return await self.request_adapter.send_async(request_info, WindowsAutopilotDeviceIdentity, error_mapping)

	async def patch(
		self,
		body: WindowsAutopilotDeviceIdentity,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsAutopilotDeviceIdentity:
		"""
		Update the navigation property windowsAutopilotDeviceIdentities in deviceManagement
		
		"""
		tags = ['deviceManagement.windowsAutopilotDeviceIdentity']

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
		return await self.request_adapter.send_async(request_info, WindowsAutopilotDeviceIdentity, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete windowsAutopilotDeviceIdentity
		Deletes a windowsAutopilotDeviceIdentity.
		Find more info here: https://learn.microsoft.com/graph/api/intune-enrollment-windowsautopilotdeviceidentity-delete?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.windowsAutopilotDeviceIdentity']
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
	def assign_user_to_device(self,
	) -> AssignUserToDeviceRequest:
		from .assign_user_to_device import AssignUserToDeviceRequest
		return AssignUserToDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def unassign_user_from_device(self,
	) -> UnassignUserFromDeviceRequest:
		from .unassign_user_from_device import UnassignUserFromDeviceRequest
		return UnassignUserFromDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def update_device_properties(self,
	) -> UpdateDevicePropertiesRequest:
		from .update_device_properties import UpdateDevicePropertiesRequest
		return UpdateDevicePropertiesRequest(self.request_adapter, self.path_parameters)

