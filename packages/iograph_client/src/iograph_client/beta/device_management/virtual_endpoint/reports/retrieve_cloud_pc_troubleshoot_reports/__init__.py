# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.retrieve_cloud_pc_troubleshoot_reports_post_request import Retrieve_cloud_pc_troubleshoot_reportsPostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class RetrieveCloudPcTroubleshootReportsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/reports/retrieveCloudPcTroubleshootReports", path_parameters)

	async def post(
		self,
		body: Retrieve_cloud_pc_troubleshoot_reportsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> bytes:
		"""
		Invoke action retrieveCloudPcTroubleshootReports
		Get troubleshooting reports for Cloud PCs. You can get a regional troubleshooting report, a report with troubleshooting details, a report with troubleshooting trends, or a report on the number of troubleshooting issues.
		Find more info here: https://learn.microsoft.com/graph/api/cloudpcreports-retrievecloudpctroubleshootreports?view=graph-rest-beta
		"""
		tags = ['deviceManagement.virtualEndpoint']

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


	def with_url(self, raw_url: str) -> RetrieveCloudPcTroubleshootReportsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RetrieveCloudPcTroubleshootReportsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RetrieveCloudPcTroubleshootReportsRequest(self.request_adapter, self.path_parameters)

