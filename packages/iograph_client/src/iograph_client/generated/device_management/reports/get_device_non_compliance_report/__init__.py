# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.get_device_non_compliance_report_post_request import Get_device_non_compliance_reportPostRequest


class GetDeviceNonComplianceReportRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/reports/getDeviceNonComplianceReport"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Get_device_non_compliance_reportPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> bytes:
		"""
		Invoke action getDeviceNonComplianceReport
		Not yet documented
		Find more info here: https://learn.microsoft.com/graph/api/intune-reporting-devicemanagementreports-getdevicenoncompliancereport?view=graph-rest-1.0
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


