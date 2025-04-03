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
	from .assign import AssignRequest
	from .device_statuses import DeviceStatusesRequest
	from .deploy_summary import DeploySummaryRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByWindowsDefenderApplicationControlSupplementalPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/wdacSupplementalPolicies/{windowsDefenderApplicationControlSupplementalPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsDefenderApplicationControlSupplementalPolicy:
		"""
		Get wdacSupplementalPolicies from deviceAppManagement
		The collection of Windows Defender Application Control Supplemental Policies.
		"""
		tags = ['deviceAppManagement.windowsDefenderApplicationControlSupplementalPolicy']

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
		return await self.request_adapter.send_async(request_info, WindowsDefenderApplicationControlSupplementalPolicy, error_mapping)

	async def patch(
		self,
		body: WindowsDefenderApplicationControlSupplementalPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsDefenderApplicationControlSupplementalPolicy:
		"""
		Update the navigation property wdacSupplementalPolicies in deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.windowsDefenderApplicationControlSupplementalPolicy']

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
		return await self.request_adapter.send_async(request_info, WindowsDefenderApplicationControlSupplementalPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property wdacSupplementalPolicies for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.windowsDefenderApplicationControlSupplementalPolicy']
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



	def with_url(self, raw_url: str) -> ByWindowsDefenderApplicationControlSupplementalPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWindowsDefenderApplicationControlSupplementalPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWindowsDefenderApplicationControlSupplementalPolicyIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		windowsDefenderApplicationControlSupplementalPolicy_id: str,
	) -> AssignmentsRequest:
		if windowsDefenderApplicationControlSupplementalPolicy_id is None:
			raise TypeError("windowsDefenderApplicationControlSupplementalPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsDefenderApplicationControlSupplementalPolicy%2Did"] =  windowsDefenderApplicationControlSupplementalPolicy_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def deploy_summary(self,
		windowsDefenderApplicationControlSupplementalPolicy_id: str,
	) -> DeploySummaryRequest:
		if windowsDefenderApplicationControlSupplementalPolicy_id is None:
			raise TypeError("windowsDefenderApplicationControlSupplementalPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsDefenderApplicationControlSupplementalPolicy%2Did"] =  windowsDefenderApplicationControlSupplementalPolicy_id

		from .deploy_summary import DeploySummaryRequest
		return DeploySummaryRequest(self.request_adapter, path_parameters)

	def device_statuses(self,
		windowsDefenderApplicationControlSupplementalPolicy_id: str,
	) -> DeviceStatusesRequest:
		if windowsDefenderApplicationControlSupplementalPolicy_id is None:
			raise TypeError("windowsDefenderApplicationControlSupplementalPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsDefenderApplicationControlSupplementalPolicy%2Did"] =  windowsDefenderApplicationControlSupplementalPolicy_id

		from .device_statuses import DeviceStatusesRequest
		return DeviceStatusesRequest(self.request_adapter, path_parameters)

	def assign(self,
		windowsDefenderApplicationControlSupplementalPolicy_id: str,
	) -> AssignRequest:
		if windowsDefenderApplicationControlSupplementalPolicy_id is None:
			raise TypeError("windowsDefenderApplicationControlSupplementalPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsDefenderApplicationControlSupplementalPolicy%2Did"] =  windowsDefenderApplicationControlSupplementalPolicy_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

