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
from iograph_models.beta.cloud_pc_bulk_remote_action_result import CloudPcBulkRemoteActionResult
from iograph_models.beta.bulk_reprovision_cloud_pc_post_request import Bulk_reprovision_cloud_pcPostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class BulkReprovisionCloudPcRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/managedDevices/bulkReprovisionCloudPc", path_parameters)

	async def post(
		self,
		body: Bulk_reprovision_cloud_pcPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPcBulkRemoteActionResult:
		"""
		Invoke action bulkReprovisionCloudPc
		Bulk reprovision a set of Cloud PC devices with Intune managed device IDs.
		Find more info here: https://learn.microsoft.com/graph/api/manageddevice-bulkreprovisioncloudpc?view=graph-rest-beta
		"""
		tags = ['me.managedDevice']

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
		return await self.request_adapter.send_async(request_info, CloudPcBulkRemoteActionResult, error_mapping)


	def with_url(self, raw_url: str) -> BulkReprovisionCloudPcRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BulkReprovisionCloudPcRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BulkReprovisionCloudPcRequest(self.request_adapter, self.path_parameters)

