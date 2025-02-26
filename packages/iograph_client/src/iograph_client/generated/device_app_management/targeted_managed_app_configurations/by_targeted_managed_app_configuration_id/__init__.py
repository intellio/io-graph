# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.targeted_managed_app_configuration import TargetedManagedAppConfiguration


class ByTargetedManagedAppConfigurationIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceAppManagement/targetedManagedAppConfigurations/{targetedManagedAppConfiguration%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TargetedManagedAppConfiguration:
		"""
		Get targetedManagedAppConfiguration
		Read properties and relationships of the targetedManagedAppConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-targetedmanagedappconfiguration-get?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.targetedManagedAppConfiguration']

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
		return await self.request_adapter.send_async(request_info, TargetedManagedAppConfiguration, error_mapping)

	async def patch(
		self,
		body: TargetedManagedAppConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TargetedManagedAppConfiguration:
		"""
		Update targetedManagedAppConfiguration
		Update the properties of a targetedManagedAppConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-targetedmanagedappconfiguration-update?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.targetedManagedAppConfiguration']

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
		return await self.request_adapter.send_async(request_info, TargetedManagedAppConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete targetedManagedAppConfiguration
		Deletes a targetedManagedAppConfiguration.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-targetedmanagedappconfiguration-delete?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.targetedManagedAppConfiguration']
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
	def apps(self,
	) -> AppsRequest:
		from .apps import AppsRequest
		return AppsRequest(self.request_adapter, self.path_parameters)

	@property
	def assignments(self,
	) -> AssignmentsRequest:
		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def deployment_summary(self,
	) -> DeploymentSummaryRequest:
		from .deployment_summary import DeploymentSummaryRequest
		return DeploymentSummaryRequest(self.request_adapter, self.path_parameters)

	@property
	def assign(self,
	) -> AssignRequest:
		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, self.path_parameters)

	@property
	def target_apps(self,
	) -> TargetAppsRequest:
		from .target_apps import TargetAppsRequest
		return TargetAppsRequest(self.request_adapter, self.path_parameters)

