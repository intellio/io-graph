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
	from .target_apps import TargetAppsRequest
	from .assign import AssignRequest
	from .deployment_summary import DeploymentSummaryRequest
	from .assignments import AssignmentsRequest
	from .apps import AppsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_managed_app_protection import WindowsManagedAppProtection
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByWindowsManagedAppProtectionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/windowsManagedAppProtections/{windowsManagedAppProtection%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsManagedAppProtection:
		"""
		Get windowsManagedAppProtections from deviceAppManagement
		Windows managed app policies.
		"""
		tags = ['deviceAppManagement.windowsManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, WindowsManagedAppProtection, error_mapping)

	async def patch(
		self,
		body: WindowsManagedAppProtection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsManagedAppProtection:
		"""
		Update the navigation property windowsManagedAppProtections in deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.windowsManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, WindowsManagedAppProtection, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property windowsManagedAppProtections for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.windowsManagedAppProtection']
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



	def with_url(self, raw_url: str) -> ByWindowsManagedAppProtectionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWindowsManagedAppProtectionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWindowsManagedAppProtectionIdRequest(self.request_adapter, self.path_parameters)

	def apps(self,
		windowsManagedAppProtection_id: str,
	) -> AppsRequest:
		if windowsManagedAppProtection_id is None:
			raise TypeError("windowsManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsManagedAppProtection%2Did"] =  windowsManagedAppProtection_id

		from .apps import AppsRequest
		return AppsRequest(self.request_adapter, path_parameters)

	def assignments(self,
		windowsManagedAppProtection_id: str,
	) -> AssignmentsRequest:
		if windowsManagedAppProtection_id is None:
			raise TypeError("windowsManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsManagedAppProtection%2Did"] =  windowsManagedAppProtection_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def deployment_summary(self,
		windowsManagedAppProtection_id: str,
	) -> DeploymentSummaryRequest:
		if windowsManagedAppProtection_id is None:
			raise TypeError("windowsManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsManagedAppProtection%2Did"] =  windowsManagedAppProtection_id

		from .deployment_summary import DeploymentSummaryRequest
		return DeploymentSummaryRequest(self.request_adapter, path_parameters)

	def assign(self,
		windowsManagedAppProtection_id: str,
	) -> AssignRequest:
		if windowsManagedAppProtection_id is None:
			raise TypeError("windowsManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsManagedAppProtection%2Did"] =  windowsManagedAppProtection_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

	def target_apps(self,
		windowsManagedAppProtection_id: str,
	) -> TargetAppsRequest:
		if windowsManagedAppProtection_id is None:
			raise TypeError("windowsManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsManagedAppProtection%2Did"] =  windowsManagedAppProtection_id

		from .target_apps import TargetAppsRequest
		return TargetAppsRequest(self.request_adapter, path_parameters)

