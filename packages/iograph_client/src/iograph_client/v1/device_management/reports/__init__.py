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
	from .retrieve_device_app_installation_status_report import RetrieveDeviceAppInstallationStatusReportRequest
	from .get_setting_non_compliance_report import GetSettingNonComplianceReportRequest
	from .get_report_filters import GetReportFiltersRequest
	from .get_policy_non_compliance_summary_report import GetPolicyNonComplianceSummaryReportRequest
	from .get_policy_non_compliance_report import GetPolicyNonComplianceReportRequest
	from .get_policy_non_compliance_metadata import GetPolicyNonComplianceMetadataRequest
	from .get_noncompliant_devices_and_settings_report import GetNoncompliantDevicesAndSettingsReportRequest
	from .get_historical_report import GetHistoricalReportRequest
	from .get_devices_without_compliance_policy_report import GetDevicesWithoutCompliancePolicyReportRequest
	from .get_device_non_compliance_report import GetDeviceNonComplianceReportRequest
	from .get_device_management_intent_settings_report import GetDeviceManagementIntentSettingsReportRequest
	from .get_device_management_intent_per_setting_contributing_profiles import GetDeviceManagementIntentPerSettingContributingProfilesRequest
	from .get_configuration_setting_non_compliance_report import GetConfigurationSettingNonComplianceReportRequest
	from .get_configuration_policy_non_compliance_summary_report import GetConfigurationPolicyNonComplianceSummaryReportRequest
	from .get_configuration_policy_non_compliance_report import GetConfigurationPolicyNonComplianceReportRequest
	from .get_compliance_setting_non_compliance_report import GetComplianceSettingNonComplianceReportRequest
	from .get_compliance_policy_non_compliance_summary_report import GetCompliancePolicyNonComplianceSummaryReportRequest
	from .get_compliance_policy_non_compliance_report import GetCompliancePolicyNonComplianceReportRequest
	from .get_cached_report import GetCachedReportRequest
	from .export_jobs import ExportJobsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.device_management_reports import DeviceManagementReports


class ReportsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/reports", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementReports:
		"""
		Get deviceManagementReports
		Read properties and relationships of the deviceManagementReports object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-reporting-devicemanagementreports-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagementReports']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementReports, error_mapping)

	async def patch(
		self,
		body: DeviceManagementReports,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementReports:
		"""
		Update deviceManagementReports
		Update the properties of a deviceManagementReports object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-reporting-devicemanagementreports-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagementReports']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementReports, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property reports for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementReports']
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



	def with_url(self, raw_url: str) -> ReportsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ReportsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def export_jobs(self,
	) -> ExportJobsRequest:
		from .export_jobs import ExportJobsRequest
		return ExportJobsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_cached_report(self,
	) -> GetCachedReportRequest:
		from .get_cached_report import GetCachedReportRequest
		return GetCachedReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_policy_non_compliance_report(self,
	) -> GetCompliancePolicyNonComplianceReportRequest:
		from .get_compliance_policy_non_compliance_report import GetCompliancePolicyNonComplianceReportRequest
		return GetCompliancePolicyNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_policy_non_compliance_summary_report(self,
	) -> GetCompliancePolicyNonComplianceSummaryReportRequest:
		from .get_compliance_policy_non_compliance_summary_report import GetCompliancePolicyNonComplianceSummaryReportRequest
		return GetCompliancePolicyNonComplianceSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_setting_non_compliance_report(self,
	) -> GetComplianceSettingNonComplianceReportRequest:
		from .get_compliance_setting_non_compliance_report import GetComplianceSettingNonComplianceReportRequest
		return GetComplianceSettingNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_policy_non_compliance_report(self,
	) -> GetConfigurationPolicyNonComplianceReportRequest:
		from .get_configuration_policy_non_compliance_report import GetConfigurationPolicyNonComplianceReportRequest
		return GetConfigurationPolicyNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_policy_non_compliance_summary_report(self,
	) -> GetConfigurationPolicyNonComplianceSummaryReportRequest:
		from .get_configuration_policy_non_compliance_summary_report import GetConfigurationPolicyNonComplianceSummaryReportRequest
		return GetConfigurationPolicyNonComplianceSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_setting_non_compliance_report(self,
	) -> GetConfigurationSettingNonComplianceReportRequest:
		from .get_configuration_setting_non_compliance_report import GetConfigurationSettingNonComplianceReportRequest
		return GetConfigurationSettingNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_management_intent_per_setting_contributing_profiles(self,
	) -> GetDeviceManagementIntentPerSettingContributingProfilesRequest:
		from .get_device_management_intent_per_setting_contributing_profiles import GetDeviceManagementIntentPerSettingContributingProfilesRequest
		return GetDeviceManagementIntentPerSettingContributingProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_management_intent_settings_report(self,
	) -> GetDeviceManagementIntentSettingsReportRequest:
		from .get_device_management_intent_settings_report import GetDeviceManagementIntentSettingsReportRequest
		return GetDeviceManagementIntentSettingsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_non_compliance_report(self,
	) -> GetDeviceNonComplianceReportRequest:
		from .get_device_non_compliance_report import GetDeviceNonComplianceReportRequest
		return GetDeviceNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_devices_without_compliance_policy_report(self,
	) -> GetDevicesWithoutCompliancePolicyReportRequest:
		from .get_devices_without_compliance_policy_report import GetDevicesWithoutCompliancePolicyReportRequest
		return GetDevicesWithoutCompliancePolicyReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_historical_report(self,
	) -> GetHistoricalReportRequest:
		from .get_historical_report import GetHistoricalReportRequest
		return GetHistoricalReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_noncompliant_devices_and_settings_report(self,
	) -> GetNoncompliantDevicesAndSettingsReportRequest:
		from .get_noncompliant_devices_and_settings_report import GetNoncompliantDevicesAndSettingsReportRequest
		return GetNoncompliantDevicesAndSettingsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_policy_non_compliance_metadata(self,
	) -> GetPolicyNonComplianceMetadataRequest:
		from .get_policy_non_compliance_metadata import GetPolicyNonComplianceMetadataRequest
		return GetPolicyNonComplianceMetadataRequest(self.request_adapter, self.path_parameters)

	@property
	def get_policy_non_compliance_report(self,
	) -> GetPolicyNonComplianceReportRequest:
		from .get_policy_non_compliance_report import GetPolicyNonComplianceReportRequest
		return GetPolicyNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_policy_non_compliance_summary_report(self,
	) -> GetPolicyNonComplianceSummaryReportRequest:
		from .get_policy_non_compliance_summary_report import GetPolicyNonComplianceSummaryReportRequest
		return GetPolicyNonComplianceSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_report_filters(self,
	) -> GetReportFiltersRequest:
		from .get_report_filters import GetReportFiltersRequest
		return GetReportFiltersRequest(self.request_adapter, self.path_parameters)

	@property
	def get_setting_non_compliance_report(self,
	) -> GetSettingNonComplianceReportRequest:
		from .get_setting_non_compliance_report import GetSettingNonComplianceReportRequest
		return GetSettingNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_device_app_installation_status_report(self,
	) -> RetrieveDeviceAppInstallationStatusReportRequest:
		from .retrieve_device_app_installation_status_report import RetrieveDeviceAppInstallationStatusReportRequest
		return RetrieveDeviceAppInstallationStatusReportRequest(self.request_adapter, self.path_parameters)

