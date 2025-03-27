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
	from .deployment_summary import DeploymentSummaryRequest
	from .assignments import AssignmentsRequest
	from .apps import AppsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.android_managed_app_protection import AndroidManagedAppProtection
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByAndroidManagedAppProtectionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/androidManagedAppProtections/{androidManagedAppProtection%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AndroidManagedAppProtection:
		"""
		Get androidManagedAppProtection
		Read properties and relationships of the androidManagedAppProtection object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-androidmanagedappprotection-get?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.androidManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, AndroidManagedAppProtection, error_mapping)

	async def patch(
		self,
		body: AndroidManagedAppProtection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AndroidManagedAppProtection:
		"""
		Update androidManagedAppProtection
		Update the properties of a androidManagedAppProtection object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-androidmanagedappprotection-update?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.androidManagedAppProtection']

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
		return await self.request_adapter.send_async(request_info, AndroidManagedAppProtection, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete androidManagedAppProtection
		Deletes a androidManagedAppProtection.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-androidmanagedappprotection-delete?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.androidManagedAppProtection']
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



	def with_url(self, raw_url: str) -> ByAndroidManagedAppProtectionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAndroidManagedAppProtectionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAndroidManagedAppProtectionIdRequest(self.request_adapter, self.path_parameters)

	def apps(self,
		androidManagedAppProtection_id: str,
	) -> AppsRequest:
		if androidManagedAppProtection_id is None:
			raise TypeError("androidManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["androidManagedAppProtection%2Did"] =  androidManagedAppProtection_id

		from .apps import AppsRequest
		return AppsRequest(self.request_adapter, path_parameters)

	def assignments(self,
		androidManagedAppProtection_id: str,
	) -> AssignmentsRequest:
		if androidManagedAppProtection_id is None:
			raise TypeError("androidManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["androidManagedAppProtection%2Did"] =  androidManagedAppProtection_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def deployment_summary(self,
		androidManagedAppProtection_id: str,
	) -> DeploymentSummaryRequest:
		if androidManagedAppProtection_id is None:
			raise TypeError("androidManagedAppProtection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["androidManagedAppProtection%2Did"] =  androidManagedAppProtection_id

		from .deployment_summary import DeploymentSummaryRequest
		return DeploymentSummaryRequest(self.request_adapter, path_parameters)

