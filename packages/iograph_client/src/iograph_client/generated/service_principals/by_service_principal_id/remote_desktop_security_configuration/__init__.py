# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .target_device_groups import TargetDeviceGroupsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class RemoteDesktopSecurityConfigurationRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/remoteDesktopSecurityConfiguration"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RemoteDesktopSecurityConfiguration:
		"""
		Get remoteDesktopSecurityConfiguration
		Read the properties and relationships of a remoteDesktopSecurityConfiguration object on a servicePrincipal. Use this configuration to view the Microsoft Entra ID Remote Desktop Services (RDS) authentication protocol to authenticate a user to Microsoft Entra joined or Microsoft Entra hybrid joined devices. Additionally you can view any targetDeviceGroups that have been configured for SSO.
		Find more info here: https://learn.microsoft.com/graph/api/remotedesktopsecurityconfiguration-get?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.remoteDesktopSecurityConfiguration']

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
		return await self.request_adapter.send_async(request_info, RemoteDesktopSecurityConfiguration, error_mapping)

	async def patch(
		self,
		body: RemoteDesktopSecurityConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RemoteDesktopSecurityConfiguration:
		"""
		Update remoteDesktopSecurityConfiguration
		Update the properties of a remoteDesktopSecurityConfiguration object on the servicePrincipal. Use this configuration to enable or disable the Microsoft Entra ID Remote Desktop Services (RDS) authentication protocol to authenticate a user to Microsoft Entra joined or Microsoft Entra hybrid joined devices.
		Find more info here: https://learn.microsoft.com/graph/api/remotedesktopsecurityconfiguration-update?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.remoteDesktopSecurityConfiguration']

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
		return await self.request_adapter.send_async(request_info, RemoteDesktopSecurityConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete remoteDesktopSecurityConfiguration
		Delete a remoteDesktopSecurityConfiguration object on a servicePrincipal. Removing remoteDesktopSecurityConfiguration object on the servicePrincipal disables the Microsoft Entra ID Remote Desktop Services (RDS) authentication protocol to authenticate a user to Microsoft Entra joined or Microsoft Entra hybrid joined devices, and removes any target device groups that you configured for SSO.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-delete-remotedesktopsecurityconfiguration?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.remoteDesktopSecurityConfiguration']
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
	def target_device_groups(self,
	) -> TargetDeviceGroupsRequest:
		from .target_device_groups import TargetDeviceGroupsRequest
		return TargetDeviceGroupsRequest(self.request_adapter, self.path_parameters)

