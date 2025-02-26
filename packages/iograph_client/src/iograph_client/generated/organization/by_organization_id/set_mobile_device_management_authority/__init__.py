# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.set_mobile_device_management_authority_post_response import Set_mobile_device_management_authorityPostResponse


class SetMobileDeviceManagementAuthorityRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/organization/{organization%2Did}/setMobileDeviceManagementAuthority"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Set_mobile_device_management_authorityPostResponse:
		"""
		Invoke action setMobileDeviceManagementAuthority
		Set mobile device management authority
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-organization-setmobiledevicemanagementauthority?view=graph-rest-1.0
		"""
		tags = ['organization.organization.Actions']

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
		return await self.request_adapter.send_async(request_info, Set_mobile_device_management_authorityPostResponse, error_mapping)


