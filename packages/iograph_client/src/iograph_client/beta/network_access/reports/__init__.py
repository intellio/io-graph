# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .networkaccess_web_category_report_with_startdatetime_enddatetime import NetworkaccessWebCategoryReportWithStartDateTimeEndDateTimeRequest
	from .networkaccess_transaction_summaries_with_startdatetime_enddatetime import NetworkaccessTransactionSummariesWithStartDateTimeEndDateTimeRequest
	from .networkaccess_get_device_usage_summary_with_startdatetime_enddatetime_activitypivotdatetime import NetworkaccessGetDeviceUsageSummaryWithStartDateTimeEndDateTimeActivityPivotDateTimeRequest
	from .networkaccess_get_destination_summaries_with_startdatetime_enddatetime_aggregatedby import NetworkaccessGetDestinationSummariesWithStartDateTimeEndDateTimeAggregatedByRequest
	from .networkaccess_get_cross_tenant_summary_with_startdatetime_enddatetime_discoverypivotdatetime import NetworkaccessGetCrossTenantSummaryWithStartDateTimeEndDateTimeDiscoveryPivotDateTimeRequest
	from .networkaccess_entities_summaries_with_startdatetime_enddatetime import NetworkaccessEntitiesSummariesWithStartDateTimeEndDateTimeRequest
	from .networkaccess_device_report_with_startdatetime_enddatetime import NetworkaccessDeviceReportWithStartDateTimeEndDateTimeRequest
	from .networkaccess_destination_report_with_startdatetime_enddatetime import NetworkaccessDestinationReportWithStartDateTimeEndDateTimeRequest
	from .networkaccess_cross_tenant_access_report_with_startdatetime_enddatetime import NetworkaccessCrossTenantAccessReportWithStartDateTimeEndDateTimeRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.networkaccess_reports import NetworkaccessReports
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ReportsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/reports", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessReports:
		"""
		Get reports from networkAccess
		Represents the status of the Global Secure Access services for the tenant.
		"""
		tags = ['networkAccess.reports']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessReports, error_mapping)

	async def patch(
		self,
		body: NetworkaccessReports,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessReports:
		"""
		Update the navigation property reports in networkAccess
		
		"""
		tags = ['networkAccess.reports']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessReports, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property reports for networkAccess
		
		"""
		tags = ['networkAccess.reports']
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

	def networkaccess_cross_tenant_access_report_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> NetworkaccessCrossTenantAccessReportWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .networkaccess_cross_tenant_access_report_with_startdatetime_enddatetime import NetworkaccessCrossTenantAccessReportWithStartDateTimeEndDateTimeRequest
		return NetworkaccessCrossTenantAccessReportWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def networkaccess_destination_report_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> NetworkaccessDestinationReportWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .networkaccess_destination_report_with_startdatetime_enddatetime import NetworkaccessDestinationReportWithStartDateTimeEndDateTimeRequest
		return NetworkaccessDestinationReportWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def networkaccess_device_report_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> NetworkaccessDeviceReportWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .networkaccess_device_report_with_startdatetime_enddatetime import NetworkaccessDeviceReportWithStartDateTimeEndDateTimeRequest
		return NetworkaccessDeviceReportWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def networkaccess_entities_summaries_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> NetworkaccessEntitiesSummariesWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .networkaccess_entities_summaries_with_startdatetime_enddatetime import NetworkaccessEntitiesSummariesWithStartDateTimeEndDateTimeRequest
		return NetworkaccessEntitiesSummariesWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def networkaccess_get_cross_tenant_summary_with_startdatetime_enddatetime_discoverypivotdatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
		discoveryPivotDateTime: datetime,
	) -> NetworkaccessGetCrossTenantSummaryWithStartDateTimeEndDateTimeDiscoveryPivotDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")
		if discoveryPivotDateTime is None:
			raise TypeError("discoveryPivotDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime
		path_parameters["discoveryPivotDateTime"] =  discoveryPivotDateTime

		from .networkaccess_get_cross_tenant_summary_with_startdatetime_enddatetime_discoverypivotdatetime import NetworkaccessGetCrossTenantSummaryWithStartDateTimeEndDateTimeDiscoveryPivotDateTimeRequest
		return NetworkaccessGetCrossTenantSummaryWithStartDateTimeEndDateTimeDiscoveryPivotDateTimeRequest(self.request_adapter, path_parameters)

	def networkaccess_get_destination_summaries_with_startdatetime_enddatetime_aggregatedby(self,
		startDateTime: datetime,
		endDateTime: datetime,
		aggregatedBy: str,
	) -> NetworkaccessGetDestinationSummariesWithStartDateTimeEndDateTimeAggregatedByRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")
		if aggregatedBy is None:
			raise TypeError("aggregatedBy cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime
		path_parameters["aggregatedBy"] =  aggregatedBy

		from .networkaccess_get_destination_summaries_with_startdatetime_enddatetime_aggregatedby import NetworkaccessGetDestinationSummariesWithStartDateTimeEndDateTimeAggregatedByRequest
		return NetworkaccessGetDestinationSummariesWithStartDateTimeEndDateTimeAggregatedByRequest(self.request_adapter, path_parameters)

	def networkaccess_get_device_usage_summary_with_startdatetime_enddatetime_activitypivotdatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
		activityPivotDateTime: datetime,
	) -> NetworkaccessGetDeviceUsageSummaryWithStartDateTimeEndDateTimeActivityPivotDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")
		if activityPivotDateTime is None:
			raise TypeError("activityPivotDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime
		path_parameters["activityPivotDateTime"] =  activityPivotDateTime

		from .networkaccess_get_device_usage_summary_with_startdatetime_enddatetime_activitypivotdatetime import NetworkaccessGetDeviceUsageSummaryWithStartDateTimeEndDateTimeActivityPivotDateTimeRequest
		return NetworkaccessGetDeviceUsageSummaryWithStartDateTimeEndDateTimeActivityPivotDateTimeRequest(self.request_adapter, path_parameters)

	def networkaccess_transaction_summaries_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> NetworkaccessTransactionSummariesWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .networkaccess_transaction_summaries_with_startdatetime_enddatetime import NetworkaccessTransactionSummariesWithStartDateTimeEndDateTimeRequest
		return NetworkaccessTransactionSummariesWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def networkaccess_web_category_report_with_startdatetime_enddatetime(self,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> NetworkaccessWebCategoryReportWithStartDateTimeEndDateTimeRequest:
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .networkaccess_web_category_report_with_startdatetime_enddatetime import NetworkaccessWebCategoryReportWithStartDateTimeEndDateTimeRequest
		return NetworkaccessWebCategoryReportWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

