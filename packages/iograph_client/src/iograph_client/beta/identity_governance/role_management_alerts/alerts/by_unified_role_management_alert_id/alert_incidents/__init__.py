# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_unified_role_management_alert_incident_id import ByUnifiedRoleManagementAlertIncidentIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident
from iograph_models.beta.unified_role_management_alert_incident_collection_response import UnifiedRoleManagementAlertIncidentCollectionResponse


class AlertIncidentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/roleManagementAlerts/alerts/{unifiedRoleManagementAlert%2Did}/alertIncidents", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleManagementAlertIncidentCollectionResponse:
		"""
		Get alertIncidents from identityGovernance
		Represents the incidents of this type of alert that have been triggered in Privileged Identity Management (PIM) for Microsoft Entra roles in the tenant. Supports $expand.
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
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlertIncidentCollectionResponse, error_mapping)

	async def post(
		self,
		body: UnifiedRoleManagementAlertIncident,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleManagementAlertIncident:
		"""
		Create new navigation property to alertIncidents for identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementAlertIncident, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AlertIncidentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AlertIncidentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AlertIncidentsRequest(self.request_adapter, self.path_parameters)

	def by_unified_role_management_alert_incident_id(self,
		unifiedRoleManagementAlert_id: str,
		unifiedRoleManagementAlertIncident_id: str,
	) -> ByUnifiedRoleManagementAlertIncidentIdRequest:
		if unifiedRoleManagementAlert_id is None:
			raise TypeError("unifiedRoleManagementAlert_id cannot be null.")
		if unifiedRoleManagementAlertIncident_id is None:
			raise TypeError("unifiedRoleManagementAlertIncident_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleManagementAlert%2Did"] =  unifiedRoleManagementAlert_id
		path_parameters["unifiedRoleManagementAlertIncident%2Did"] =  unifiedRoleManagementAlertIncident_id

		from .by_unified_role_management_alert_incident_id import ByUnifiedRoleManagementAlertIncidentIdRequest
		return ByUnifiedRoleManagementAlertIncidentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		unifiedRoleManagementAlert_id: str,
	) -> CountRequest:
		if unifiedRoleManagementAlert_id is None:
			raise TypeError("unifiedRoleManagementAlert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleManagementAlert%2Did"] =  unifiedRoleManagementAlert_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

