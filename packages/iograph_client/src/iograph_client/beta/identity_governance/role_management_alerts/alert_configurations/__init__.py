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
	from .count import CountRequest
	from .by_unified_role_management_alert_configuration_id import ByUnifiedRoleManagementAlertConfigurationIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.unified_role_management_alert_configuration_collection_response import UnifiedRoleManagementAlertConfigurationCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration


class AlertConfigurationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/roleManagementAlerts/alertConfigurations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleManagementAlertConfigurationCollectionResponse:
		"""
		List alertConfigurations
		Get a list of the alert configurations. The alert configurations are a collection of following types that are derived from the unifiedRoleManagementAlertConfiguration object:
		Find more info here: https://learn.microsoft.com/graph/api/rolemanagementalert-list-alertconfigurations?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlertConfigurationCollectionResponse, error_mapping)

	async def post(
		self,
		body: UnifiedRoleManagementAlertConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleManagementAlertConfiguration:
		"""
		Create new navigation property to alertConfigurations for identityGovernance
		
		"""
		tags = ['identityGovernance.roleManagementAlert']

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
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlertConfiguration, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AlertConfigurationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AlertConfigurationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AlertConfigurationsRequest(self.request_adapter, self.path_parameters)

	def by_unified_role_management_alert_configuration_id(self,
		unifiedRoleManagementAlertConfiguration_id: str,
	) -> ByUnifiedRoleManagementAlertConfigurationIdRequest:
		if unifiedRoleManagementAlertConfiguration_id is None:
			raise TypeError("unifiedRoleManagementAlertConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleManagementAlertConfiguration%2Did"] =  unifiedRoleManagementAlertConfiguration_id

		from .by_unified_role_management_alert_configuration_id import ByUnifiedRoleManagementAlertConfigurationIdRequest
		return ByUnifiedRoleManagementAlertConfigurationIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

