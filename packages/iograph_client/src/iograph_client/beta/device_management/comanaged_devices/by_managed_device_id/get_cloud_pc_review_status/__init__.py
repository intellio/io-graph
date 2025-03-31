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
from iograph_models.beta.cloud_pc_review_status import CloudPcReviewStatus
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class GetCloudPcReviewStatusRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/comanagedDevices/{managedDevice%2Did}/getCloudPcReviewStatus()", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPcReviewStatus:
		"""
		Invoke function getCloudPcReviewStatus
		Get the review status of a specific Cloud PC device.
		Find more info here: https://learn.microsoft.com/graph/api/manageddevice-getcloudpcreviewstatus?view=graph-rest-beta
		"""
		tags = ['deviceManagement.managedDevice']

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
		return await self.request_adapter.send_async(request_info, CloudPcReviewStatus, error_mapping)


	def with_url(self, raw_url: str) -> GetCloudPcReviewStatusRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GetCloudPcReviewStatusRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GetCloudPcReviewStatusRequest(self.request_adapter, self.path_parameters)

