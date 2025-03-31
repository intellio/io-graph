# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .windows_protection_states import WindowsProtectionStatesRequest
	from .windows_device_malware_states import WindowsDeviceMalwareStatesRequest
	from .tenant_tags import TenantTagsRequest
	from .tenants_detailed_information import TenantsDetailedInformationRequest
	from .tenants_customized_information import TenantsCustomizedInformationRequest
	from .tenants import TenantsRequest
	from .tenant_groups import TenantGroupsRequest
	from .my_roles import MyRolesRequest
	from .management_template_step_versions import ManagementTemplateStepVersionsRequest
	from .management_template_step_tenant_summaries import ManagementTemplateStepTenantSummariesRequest
	from .management_template_steps import ManagementTemplateStepsRequest
	from .management_templates import ManagementTemplatesRequest
	from .management_template_collection_tenant_summaries import ManagementTemplateCollectionTenantSummariesRequest
	from .management_template_collections import ManagementTemplateCollectionsRequest
	from .management_intents import ManagementIntentsRequest
	from .management_action_tenant_deployment_statuses import ManagementActionTenantDeploymentStatusesRequest
	from .management_actions import ManagementActionsRequest
	from .managed_tenant_ticketing_endpoints import ManagedTenantTicketingEndpointsRequest
	from .managed_tenant_email_notifications import ManagedTenantEmailNotificationsRequest
	from .managed_tenant_api_notifications import ManagedTenantApiNotificationsRequest
	from .managed_tenant_alerts import ManagedTenantAlertsRequest
	from .managed_tenant_alert_rules import ManagedTenantAlertRulesRequest
	from .managed_tenant_alert_rule_definitions import ManagedTenantAlertRuleDefinitionsRequest
	from .managed_tenant_alert_logs import ManagedTenantAlertLogsRequest
	from .managed_device_compliance_trends import ManagedDeviceComplianceTrendsRequest
	from .managed_device_compliances import ManagedDeviceCompliancesRequest
	from .device_health_statuses import DeviceHealthStatusesRequest
	from .device_compliance_policy_setting_state_summaries import DeviceCompliancePolicySettingStateSummariesRequest
	from .device_app_performances import DeviceAppPerformancesRequest
	from .credential_user_registrations_summaries import CredentialUserRegistrationsSummariesRequest
	from .conditional_access_policy_coverages import ConditionalAccessPolicyCoveragesRequest
	from .cloud_pcs_overview import CloudPcsOverviewRequest
	from .cloud_pc_devices import CloudPcDevicesRequest
	from .cloud_pc_connections import CloudPcConnectionsRequest
	from .audit_events import AuditEventsRequest
	from .app_performances import AppPerformancesRequest
	from .aggregated_policy_compliances import AggregatedPolicyCompliancesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.managed_tenants_managed_tenant import ManagedTenantsManagedTenant
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ManagedTenantsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedTenantsManagedTenant:
		"""
		Get managedTenants from tenantRelationships
		The operations available to interact with the multi-tenant management platform.
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
		return await self.request_adapter.send_async(request_info, ManagedTenantsManagedTenant, error_mapping)

	async def patch(
		self,
		body: ManagedTenantsManagedTenant,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedTenantsManagedTenant:
		"""
		Update the navigation property managedTenants in tenantRelationships
		
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
		return await self.request_adapter.send_async(request_info, ManagedTenantsManagedTenant, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property managedTenants for tenantRelationships
		
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



	def with_url(self, raw_url: str) -> ManagedTenantsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ManagedTenantsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ManagedTenantsRequest(self.request_adapter, self.path_parameters)

	@property
	def aggregated_policy_compliances(self,
	) -> AggregatedPolicyCompliancesRequest:
		from .aggregated_policy_compliances import AggregatedPolicyCompliancesRequest
		return AggregatedPolicyCompliancesRequest(self.request_adapter, self.path_parameters)

	@property
	def app_performances(self,
	) -> AppPerformancesRequest:
		from .app_performances import AppPerformancesRequest
		return AppPerformancesRequest(self.request_adapter, self.path_parameters)

	@property
	def audit_events(self,
	) -> AuditEventsRequest:
		from .audit_events import AuditEventsRequest
		return AuditEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_pc_connections(self,
	) -> CloudPcConnectionsRequest:
		from .cloud_pc_connections import CloudPcConnectionsRequest
		return CloudPcConnectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_pc_devices(self,
	) -> CloudPcDevicesRequest:
		from .cloud_pc_devices import CloudPcDevicesRequest
		return CloudPcDevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_pcs_overview(self,
	) -> CloudPcsOverviewRequest:
		from .cloud_pcs_overview import CloudPcsOverviewRequest
		return CloudPcsOverviewRequest(self.request_adapter, self.path_parameters)

	@property
	def conditional_access_policy_coverages(self,
	) -> ConditionalAccessPolicyCoveragesRequest:
		from .conditional_access_policy_coverages import ConditionalAccessPolicyCoveragesRequest
		return ConditionalAccessPolicyCoveragesRequest(self.request_adapter, self.path_parameters)

	@property
	def credential_user_registrations_summaries(self,
	) -> CredentialUserRegistrationsSummariesRequest:
		from .credential_user_registrations_summaries import CredentialUserRegistrationsSummariesRequest
		return CredentialUserRegistrationsSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_app_performances(self,
	) -> DeviceAppPerformancesRequest:
		from .device_app_performances import DeviceAppPerformancesRequest
		return DeviceAppPerformancesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_compliance_policy_setting_state_summaries(self,
	) -> DeviceCompliancePolicySettingStateSummariesRequest:
		from .device_compliance_policy_setting_state_summaries import DeviceCompliancePolicySettingStateSummariesRequest
		return DeviceCompliancePolicySettingStateSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_health_statuses(self,
	) -> DeviceHealthStatusesRequest:
		from .device_health_statuses import DeviceHealthStatusesRequest
		return DeviceHealthStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_device_compliances(self,
	) -> ManagedDeviceCompliancesRequest:
		from .managed_device_compliances import ManagedDeviceCompliancesRequest
		return ManagedDeviceCompliancesRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_device_compliance_trends(self,
	) -> ManagedDeviceComplianceTrendsRequest:
		from .managed_device_compliance_trends import ManagedDeviceComplianceTrendsRequest
		return ManagedDeviceComplianceTrendsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_tenant_alert_logs(self,
	) -> ManagedTenantAlertLogsRequest:
		from .managed_tenant_alert_logs import ManagedTenantAlertLogsRequest
		return ManagedTenantAlertLogsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_tenant_alert_rule_definitions(self,
	) -> ManagedTenantAlertRuleDefinitionsRequest:
		from .managed_tenant_alert_rule_definitions import ManagedTenantAlertRuleDefinitionsRequest
		return ManagedTenantAlertRuleDefinitionsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_tenant_alert_rules(self,
	) -> ManagedTenantAlertRulesRequest:
		from .managed_tenant_alert_rules import ManagedTenantAlertRulesRequest
		return ManagedTenantAlertRulesRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_tenant_alerts(self,
	) -> ManagedTenantAlertsRequest:
		from .managed_tenant_alerts import ManagedTenantAlertsRequest
		return ManagedTenantAlertsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_tenant_api_notifications(self,
	) -> ManagedTenantApiNotificationsRequest:
		from .managed_tenant_api_notifications import ManagedTenantApiNotificationsRequest
		return ManagedTenantApiNotificationsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_tenant_email_notifications(self,
	) -> ManagedTenantEmailNotificationsRequest:
		from .managed_tenant_email_notifications import ManagedTenantEmailNotificationsRequest
		return ManagedTenantEmailNotificationsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_tenant_ticketing_endpoints(self,
	) -> ManagedTenantTicketingEndpointsRequest:
		from .managed_tenant_ticketing_endpoints import ManagedTenantTicketingEndpointsRequest
		return ManagedTenantTicketingEndpointsRequest(self.request_adapter, self.path_parameters)

	@property
	def management_actions(self,
	) -> ManagementActionsRequest:
		from .management_actions import ManagementActionsRequest
		return ManagementActionsRequest(self.request_adapter, self.path_parameters)

	@property
	def management_action_tenant_deployment_statuses(self,
	) -> ManagementActionTenantDeploymentStatusesRequest:
		from .management_action_tenant_deployment_statuses import ManagementActionTenantDeploymentStatusesRequest
		return ManagementActionTenantDeploymentStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def management_intents(self,
	) -> ManagementIntentsRequest:
		from .management_intents import ManagementIntentsRequest
		return ManagementIntentsRequest(self.request_adapter, self.path_parameters)

	@property
	def management_template_collections(self,
	) -> ManagementTemplateCollectionsRequest:
		from .management_template_collections import ManagementTemplateCollectionsRequest
		return ManagementTemplateCollectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def management_template_collection_tenant_summaries(self,
	) -> ManagementTemplateCollectionTenantSummariesRequest:
		from .management_template_collection_tenant_summaries import ManagementTemplateCollectionTenantSummariesRequest
		return ManagementTemplateCollectionTenantSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def management_templates(self,
	) -> ManagementTemplatesRequest:
		from .management_templates import ManagementTemplatesRequest
		return ManagementTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def management_template_steps(self,
	) -> ManagementTemplateStepsRequest:
		from .management_template_steps import ManagementTemplateStepsRequest
		return ManagementTemplateStepsRequest(self.request_adapter, self.path_parameters)

	@property
	def management_template_step_tenant_summaries(self,
	) -> ManagementTemplateStepTenantSummariesRequest:
		from .management_template_step_tenant_summaries import ManagementTemplateStepTenantSummariesRequest
		return ManagementTemplateStepTenantSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def management_template_step_versions(self,
	) -> ManagementTemplateStepVersionsRequest:
		from .management_template_step_versions import ManagementTemplateStepVersionsRequest
		return ManagementTemplateStepVersionsRequest(self.request_adapter, self.path_parameters)

	@property
	def my_roles(self,
	) -> MyRolesRequest:
		from .my_roles import MyRolesRequest
		return MyRolesRequest(self.request_adapter, self.path_parameters)

	@property
	def tenant_groups(self,
	) -> TenantGroupsRequest:
		from .tenant_groups import TenantGroupsRequest
		return TenantGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def tenants(self,
	) -> TenantsRequest:
		from .tenants import TenantsRequest
		return TenantsRequest(self.request_adapter, self.path_parameters)

	@property
	def tenants_customized_information(self,
	) -> TenantsCustomizedInformationRequest:
		from .tenants_customized_information import TenantsCustomizedInformationRequest
		return TenantsCustomizedInformationRequest(self.request_adapter, self.path_parameters)

	@property
	def tenants_detailed_information(self,
	) -> TenantsDetailedInformationRequest:
		from .tenants_detailed_information import TenantsDetailedInformationRequest
		return TenantsDetailedInformationRequest(self.request_adapter, self.path_parameters)

	@property
	def tenant_tags(self,
	) -> TenantTagsRequest:
		from .tenant_tags import TenantTagsRequest
		return TenantTagsRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_device_malware_states(self,
	) -> WindowsDeviceMalwareStatesRequest:
		from .windows_device_malware_states import WindowsDeviceMalwareStatesRequest
		return WindowsDeviceMalwareStatesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_protection_states(self,
	) -> WindowsProtectionStatesRequest:
		from .windows_protection_states import WindowsProtectionStatesRequest
		return WindowsProtectionStatesRequest(self.request_adapter, self.path_parameters)

