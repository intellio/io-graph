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
	from .managed_tenants_add_user_input_log import ManagedTenantsAddUserInputLogRequest
	from .email_notifications import EmailNotificationsRequest
	from .api_notifications import ApiNotificationsRequest
	from .alert_rule import AlertRuleRequest
	from .alert_logs import AlertLogsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.managed_tenants_managed_tenant_alert import ManagedTenantsManagedTenantAlert


class ByManagedTenantAlertIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants/managedTenantAlerts/{managedTenantAlert%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedTenantsManagedTenantAlert:
		"""
		Get managedTenantAlerts from tenantRelationships
		
		"""
		tags = ['tenantRelationships.managedTenant']

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
		return await self.request_adapter.send_async(request_info, ManagedTenantsManagedTenantAlert, error_mapping)

	async def patch(
		self,
		body: ManagedTenantsManagedTenantAlert,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedTenantsManagedTenantAlert:
		"""
		Update the navigation property managedTenantAlerts in tenantRelationships
		
		"""
		tags = ['tenantRelationships.managedTenant']

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
		return await self.request_adapter.send_async(request_info, ManagedTenantsManagedTenantAlert, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property managedTenantAlerts for tenantRelationships
		
		"""
		tags = ['tenantRelationships.managedTenant']
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



	def with_url(self, raw_url: str) -> ByManagedTenantAlertIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByManagedTenantAlertIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByManagedTenantAlertIdRequest(self.request_adapter, self.path_parameters)

	def alert_logs(self,
		managedTenantAlert_id: str,
	) -> AlertLogsRequest:
		if managedTenantAlert_id is None:
			raise TypeError("managedTenantAlert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedTenantAlert%2Did"] =  managedTenantAlert_id

		from .alert_logs import AlertLogsRequest
		return AlertLogsRequest(self.request_adapter, path_parameters)

	def alert_rule(self,
		managedTenantAlert_id: str,
	) -> AlertRuleRequest:
		if managedTenantAlert_id is None:
			raise TypeError("managedTenantAlert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedTenantAlert%2Did"] =  managedTenantAlert_id

		from .alert_rule import AlertRuleRequest
		return AlertRuleRequest(self.request_adapter, path_parameters)

	def api_notifications(self,
		managedTenantAlert_id: str,
	) -> ApiNotificationsRequest:
		if managedTenantAlert_id is None:
			raise TypeError("managedTenantAlert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedTenantAlert%2Did"] =  managedTenantAlert_id

		from .api_notifications import ApiNotificationsRequest
		return ApiNotificationsRequest(self.request_adapter, path_parameters)

	def email_notifications(self,
		managedTenantAlert_id: str,
	) -> EmailNotificationsRequest:
		if managedTenantAlert_id is None:
			raise TypeError("managedTenantAlert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedTenantAlert%2Did"] =  managedTenantAlert_id

		from .email_notifications import EmailNotificationsRequest
		return EmailNotificationsRequest(self.request_adapter, path_parameters)

	def managed_tenants_add_user_input_log(self,
		managedTenantAlert_id: str,
	) -> ManagedTenantsAddUserInputLogRequest:
		if managedTenantAlert_id is None:
			raise TypeError("managedTenantAlert_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedTenantAlert%2Did"] =  managedTenantAlert_id

		from .managed_tenants_add_user_input_log import ManagedTenantsAddUserInputLogRequest
		return ManagedTenantsAddUserInputLogRequest(self.request_adapter, path_parameters)

