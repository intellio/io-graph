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
	from .user_statuses import UserStatusesRequest
	from .assign import AssignRequest
	from .group_assignments import GroupAssignmentsRequest
	from .device_statuses import DeviceStatusesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByIosLobAppProvisioningConfigurationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/iosLobAppProvisioningConfigurations/{iosLobAppProvisioningConfiguration%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IosLobAppProvisioningConfiguration:
		"""
		Get iosLobAppProvisioningConfigurations from deviceAppManagement
		The IOS Lob App Provisioning Configurations.
		"""
		tags = ['deviceAppManagement.iosLobAppProvisioningConfiguration']

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
		return await self.request_adapter.send_async(request_info, IosLobAppProvisioningConfiguration, error_mapping)

	async def patch(
		self,
		body: IosLobAppProvisioningConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IosLobAppProvisioningConfiguration:
		"""
		Update the navigation property iosLobAppProvisioningConfigurations in deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.iosLobAppProvisioningConfiguration']

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
		return await self.request_adapter.send_async(request_info, IosLobAppProvisioningConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property iosLobAppProvisioningConfigurations for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.iosLobAppProvisioningConfiguration']
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



	def with_url(self, raw_url: str) -> ByIosLobAppProvisioningConfigurationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByIosLobAppProvisioningConfigurationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByIosLobAppProvisioningConfigurationIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		iosLobAppProvisioningConfiguration_id: str,
	) -> AssignmentsRequest:
		if iosLobAppProvisioningConfiguration_id is None:
			raise TypeError("iosLobAppProvisioningConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["iosLobAppProvisioningConfiguration%2Did"] =  iosLobAppProvisioningConfiguration_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def device_statuses(self,
		iosLobAppProvisioningConfiguration_id: str,
	) -> DeviceStatusesRequest:
		if iosLobAppProvisioningConfiguration_id is None:
			raise TypeError("iosLobAppProvisioningConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["iosLobAppProvisioningConfiguration%2Did"] =  iosLobAppProvisioningConfiguration_id

		from .device_statuses import DeviceStatusesRequest
		return DeviceStatusesRequest(self.request_adapter, path_parameters)

	def group_assignments(self,
		iosLobAppProvisioningConfiguration_id: str,
	) -> GroupAssignmentsRequest:
		if iosLobAppProvisioningConfiguration_id is None:
			raise TypeError("iosLobAppProvisioningConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["iosLobAppProvisioningConfiguration%2Did"] =  iosLobAppProvisioningConfiguration_id

		from .group_assignments import GroupAssignmentsRequest
		return GroupAssignmentsRequest(self.request_adapter, path_parameters)

	def assign(self,
		iosLobAppProvisioningConfiguration_id: str,
	) -> AssignRequest:
		if iosLobAppProvisioningConfiguration_id is None:
			raise TypeError("iosLobAppProvisioningConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["iosLobAppProvisioningConfiguration%2Did"] =  iosLobAppProvisioningConfiguration_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

	def user_statuses(self,
		iosLobAppProvisioningConfiguration_id: str,
	) -> UserStatusesRequest:
		if iosLobAppProvisioningConfiguration_id is None:
			raise TypeError("iosLobAppProvisioningConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["iosLobAppProvisioningConfiguration%2Did"] =  iosLobAppProvisioningConfiguration_id

		from .user_statuses import UserStatusesRequest
		return UserStatusesRequest(self.request_adapter, path_parameters)

