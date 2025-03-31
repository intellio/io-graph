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
	from .operations import OperationsRequest
	from .update_software import UpdateSoftwareRequest
	from .run_diagnostics import RunDiagnosticsRequest
	from .restart import RestartRequest
	from .health import HealthRequest
	from .configuration import ConfigurationRequest
	from .activity import ActivityRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.teamwork_device import TeamworkDevice
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByTeamworkDeviceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamwork/devices/{teamworkDevice%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TeamworkDevice:
		"""
		Get teamworkDevice
		Get the properties of a Microsoft Teams-enabled device. For example, you can use this method to get the device type, hardware detail, activity state, and health status information for a device that's enabled for Teams.
		Find more info here: https://learn.microsoft.com/graph/api/teamworkdevice-get?view=graph-rest-beta
		"""
		tags = ['teamwork.teamworkDevice']

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
		return await self.request_adapter.send_async(request_info, TeamworkDevice, error_mapping)

	async def patch(
		self,
		body: TeamworkDevice,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TeamworkDevice:
		"""
		Update the navigation property devices in teamwork
		
		"""
		tags = ['teamwork.teamworkDevice']

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
		return await self.request_adapter.send_async(request_info, TeamworkDevice, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property devices for teamwork
		
		"""
		tags = ['teamwork.teamworkDevice']
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



	def with_url(self, raw_url: str) -> ByTeamworkDeviceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTeamworkDeviceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTeamworkDeviceIdRequest(self.request_adapter, self.path_parameters)

	def activity(self,
		teamworkDevice_id: str,
	) -> ActivityRequest:
		if teamworkDevice_id is None:
			raise TypeError("teamworkDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamworkDevice%2Did"] =  teamworkDevice_id

		from .activity import ActivityRequest
		return ActivityRequest(self.request_adapter, path_parameters)

	def configuration(self,
		teamworkDevice_id: str,
	) -> ConfigurationRequest:
		if teamworkDevice_id is None:
			raise TypeError("teamworkDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamworkDevice%2Did"] =  teamworkDevice_id

		from .configuration import ConfigurationRequest
		return ConfigurationRequest(self.request_adapter, path_parameters)

	def health(self,
		teamworkDevice_id: str,
	) -> HealthRequest:
		if teamworkDevice_id is None:
			raise TypeError("teamworkDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamworkDevice%2Did"] =  teamworkDevice_id

		from .health import HealthRequest
		return HealthRequest(self.request_adapter, path_parameters)

	def restart(self,
		teamworkDevice_id: str,
	) -> RestartRequest:
		if teamworkDevice_id is None:
			raise TypeError("teamworkDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamworkDevice%2Did"] =  teamworkDevice_id

		from .restart import RestartRequest
		return RestartRequest(self.request_adapter, path_parameters)

	def run_diagnostics(self,
		teamworkDevice_id: str,
	) -> RunDiagnosticsRequest:
		if teamworkDevice_id is None:
			raise TypeError("teamworkDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamworkDevice%2Did"] =  teamworkDevice_id

		from .run_diagnostics import RunDiagnosticsRequest
		return RunDiagnosticsRequest(self.request_adapter, path_parameters)

	def update_software(self,
		teamworkDevice_id: str,
	) -> UpdateSoftwareRequest:
		if teamworkDevice_id is None:
			raise TypeError("teamworkDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamworkDevice%2Did"] =  teamworkDevice_id

		from .update_software import UpdateSoftwareRequest
		return UpdateSoftwareRequest(self.request_adapter, path_parameters)

	def operations(self,
		teamworkDevice_id: str,
	) -> OperationsRequest:
		if teamworkDevice_id is None:
			raise TypeError("teamworkDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamworkDevice%2Did"] =  teamworkDevice_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

