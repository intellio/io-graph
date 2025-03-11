# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .alert_definition import AlertDefinitionRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByUnifiedRoleManagementAlertConfigurationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/roleManagementAlerts/alertConfigurations/{unifiedRoleManagementAlertConfiguration%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleManagementAlertConfiguration:
		"""
		Get alertConfigurations from identityGovernance
		The various configurations of an alert for Microsoft Entra roles. The configurations are predefined and can't be created or deleted, but some of the configurations can be modified.
		"""
		tags = ['identityGovernance.roleManagementAlert']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlertConfiguration, error_mapping)

	async def patch(
		self,
		body: UnifiedRoleManagementAlertConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleManagementAlertConfiguration:
		"""
		Update the navigation property alertConfigurations in identityGovernance
		
		"""
		tags = ['identityGovernance.roleManagementAlert']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlertConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property alertConfigurations for identityGovernance
		
		"""
		tags = ['identityGovernance.roleManagementAlert']
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



	def with_url(self, raw_url: str) -> ByUnifiedRoleManagementAlertConfigurationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUnifiedRoleManagementAlertConfigurationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUnifiedRoleManagementAlertConfigurationIdRequest(self.request_adapter, self.path_parameters)

	def alert_definition(self,
		unifiedRoleManagementAlertConfiguration_id: str,
	) -> AlertDefinitionRequest:
		if unifiedRoleManagementAlertConfiguration_id is None:
			raise TypeError("unifiedRoleManagementAlertConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleManagementAlertConfiguration%2Did"] =  unifiedRoleManagementAlertConfiguration_id

		from .alert_definition import AlertDefinitionRequest
		return AlertDefinitionRequest(self.request_adapter, path_parameters)

