# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.get_configuration_policy_non_compliance_summary_report_post_request import Get_configuration_policy_non_compliance_summary_reportPostRequest
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class GetConfigurationPolicyNonComplianceSummaryReportRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/reports/getConfigurationPolicyNonComplianceSummaryReport", path_parameters)

	async def post(
		self,
		body: Get_configuration_policy_non_compliance_summary_reportPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> bytes:
		"""
		Invoke action getConfigurationPolicyNonComplianceSummaryReport
		Not yet documented
		Find more info here: https://learn.microsoft.com/graph/api/intune-reporting-devicemanagementreports-getconfigurationpolicynoncompliancesummaryreport?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagementReports']

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
		return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)


	def with_url(self, raw_url: str) -> GetConfigurationPolicyNonComplianceSummaryReportRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GetConfigurationPolicyNonComplianceSummaryReportRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GetConfigurationPolicyNonComplianceSummaryReportRequest(self.request_adapter, self.path_parameters)

