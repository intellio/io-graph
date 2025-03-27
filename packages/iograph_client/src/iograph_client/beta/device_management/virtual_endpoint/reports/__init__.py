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
	from .retrieve_frontline_reports import RetrieveFrontlineReportsRequest
	from .retrieve_cross_region_disaster_recovery_report import RetrieveCrossRegionDisasterRecoveryReportRequest
	from .retrieve_connection_quality_reports import RetrieveConnectionQualityReportsRequest
	from .retrieve_cloud_pc_troubleshoot_reports import RetrieveCloudPcTroubleshootReportsRequest
	from .retrieve_cloud_pc_tenant_metrics_report import RetrieveCloudPcTenantMetricsReportRequest
	from .retrieve_bulk_action_status_report import RetrieveBulkActionStatusReportRequest
	from .get_total_aggregated_remote_connection_reports import GetTotalAggregatedRemoteConnectionReportsRequest
	from .get_remote_connection_historical_reports import GetRemoteConnectionHistoricalReportsRequest
	from .get_real_time_remote_connection_status_with_cloudpcid import GetRealTimeRemoteConnectionStatusWithCloudPcIdRequest
	from .get_real_time_remote_connection_latency_with_cloudpcid import GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequest
	from .get_raw_remote_connection_reports import GetRawRemoteConnectionReportsRequest
	from .get_inaccessible_cloud_pc_reports import GetInaccessibleCloudPcReportsRequest
	from .get_frontline_report import GetFrontlineReportRequest
	from .get_daily_aggregated_remote_connection_reports import GetDailyAggregatedRemoteConnectionReportsRequest
	from .get_connection_quality_reports import GetConnectionQualityReportsRequest
	from .get_cloud_pc_recommendation_reports import GetCloudPcRecommendationReportsRequest
	from .get_cloud_pc_performance_report import GetCloudPcPerformanceReportRequest
	from .get_action_status_reports import GetActionStatusReportsRequest
	from .export_jobs import ExportJobsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.cloud_pc_reports import CloudPcReports


class ReportsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/reports", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudPcReports:
		"""
		Get reports from deviceManagement
		Cloud PC related reports.
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPcReports, error_mapping)

	async def patch(
		self,
		body: CloudPcReports,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPcReports:
		"""
		Update the navigation property reports in deviceManagement
		
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPcReports, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property reports for deviceManagement
		
		"""
		tags = ['deviceManagement.virtualEndpoint']
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
	def get_action_status_reports(self,
	) -> GetActionStatusReportsRequest:
		from .get_action_status_reports import GetActionStatusReportsRequest
		return GetActionStatusReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_cloud_pc_performance_report(self,
	) -> GetCloudPcPerformanceReportRequest:
		from .get_cloud_pc_performance_report import GetCloudPcPerformanceReportRequest
		return GetCloudPcPerformanceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_cloud_pc_recommendation_reports(self,
	) -> GetCloudPcRecommendationReportsRequest:
		from .get_cloud_pc_recommendation_reports import GetCloudPcRecommendationReportsRequest
		return GetCloudPcRecommendationReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_connection_quality_reports(self,
	) -> GetConnectionQualityReportsRequest:
		from .get_connection_quality_reports import GetConnectionQualityReportsRequest
		return GetConnectionQualityReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_daily_aggregated_remote_connection_reports(self,
	) -> GetDailyAggregatedRemoteConnectionReportsRequest:
		from .get_daily_aggregated_remote_connection_reports import GetDailyAggregatedRemoteConnectionReportsRequest
		return GetDailyAggregatedRemoteConnectionReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_frontline_report(self,
	) -> GetFrontlineReportRequest:
		from .get_frontline_report import GetFrontlineReportRequest
		return GetFrontlineReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_inaccessible_cloud_pc_reports(self,
	) -> GetInaccessibleCloudPcReportsRequest:
		from .get_inaccessible_cloud_pc_reports import GetInaccessibleCloudPcReportsRequest
		return GetInaccessibleCloudPcReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_raw_remote_connection_reports(self,
	) -> GetRawRemoteConnectionReportsRequest:
		from .get_raw_remote_connection_reports import GetRawRemoteConnectionReportsRequest
		return GetRawRemoteConnectionReportsRequest(self.request_adapter, self.path_parameters)

	def get_real_time_remote_connection_latency_with_cloudpcid(self,
		cloudPcId: str,
	) -> GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequest:
		if cloudPcId is None:
			raise TypeError("cloudPcId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPcId"] =  cloudPcId

		from .get_real_time_remote_connection_latency_with_cloudpcid import GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequest
		return GetRealTimeRemoteConnectionLatencyWithCloudPcIdRequest(self.request_adapter, path_parameters)

	def get_real_time_remote_connection_status_with_cloudpcid(self,
		cloudPcId: str,
	) -> GetRealTimeRemoteConnectionStatusWithCloudPcIdRequest:
		if cloudPcId is None:
			raise TypeError("cloudPcId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPcId"] =  cloudPcId

		from .get_real_time_remote_connection_status_with_cloudpcid import GetRealTimeRemoteConnectionStatusWithCloudPcIdRequest
		return GetRealTimeRemoteConnectionStatusWithCloudPcIdRequest(self.request_adapter, path_parameters)

	@property
	def get_remote_connection_historical_reports(self,
	) -> GetRemoteConnectionHistoricalReportsRequest:
		from .get_remote_connection_historical_reports import GetRemoteConnectionHistoricalReportsRequest
		return GetRemoteConnectionHistoricalReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_total_aggregated_remote_connection_reports(self,
	) -> GetTotalAggregatedRemoteConnectionReportsRequest:
		from .get_total_aggregated_remote_connection_reports import GetTotalAggregatedRemoteConnectionReportsRequest
		return GetTotalAggregatedRemoteConnectionReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_bulk_action_status_report(self,
	) -> RetrieveBulkActionStatusReportRequest:
		from .retrieve_bulk_action_status_report import RetrieveBulkActionStatusReportRequest
		return RetrieveBulkActionStatusReportRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_cloud_pc_tenant_metrics_report(self,
	) -> RetrieveCloudPcTenantMetricsReportRequest:
		from .retrieve_cloud_pc_tenant_metrics_report import RetrieveCloudPcTenantMetricsReportRequest
		return RetrieveCloudPcTenantMetricsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_cloud_pc_troubleshoot_reports(self,
	) -> RetrieveCloudPcTroubleshootReportsRequest:
		from .retrieve_cloud_pc_troubleshoot_reports import RetrieveCloudPcTroubleshootReportsRequest
		return RetrieveCloudPcTroubleshootReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_connection_quality_reports(self,
	) -> RetrieveConnectionQualityReportsRequest:
		from .retrieve_connection_quality_reports import RetrieveConnectionQualityReportsRequest
		return RetrieveConnectionQualityReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_cross_region_disaster_recovery_report(self,
	) -> RetrieveCrossRegionDisasterRecoveryReportRequest:
		from .retrieve_cross_region_disaster_recovery_report import RetrieveCrossRegionDisasterRecoveryReportRequest
		return RetrieveCrossRegionDisasterRecoveryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_frontline_reports(self,
	) -> RetrieveFrontlineReportsRequest:
		from .retrieve_frontline_reports import RetrieveFrontlineReportsRequest
		return RetrieveFrontlineReportsRequest(self.request_adapter, self.path_parameters)

