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
	from .troubleshoot import TroubleshootRequest
	from .restore import RestoreRequest
	from .rename import RenameRequest
	from .reboot import RebootRequest
	from .end_grace_period import EndGracePeriodRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.cloud_p_c import CloudPC
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByCloudPCIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs/{cloudPC%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudPC:
		"""
		Get cloudPC
		Read the properties and relationships of a specific cloudPC object.
		Find more info here: https://learn.microsoft.com/graph/api/cloudpc-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)

	async def patch(
		self,
		body: CloudPC,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPC:
		"""
		Update the navigation property cloudPCs in deviceManagement
		
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
		return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property cloudPCs for deviceManagement
		
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



	def with_url(self, raw_url: str) -> ByCloudPCIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCloudPCIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCloudPCIdRequest(self.request_adapter, self.path_parameters)

	def end_grace_period(self,
		cloudPC_id: str,
	) -> EndGracePeriodRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .end_grace_period import EndGracePeriodRequest
		return EndGracePeriodRequest(self.request_adapter, path_parameters)

	def reboot(self,
		cloudPC_id: str,
	) -> RebootRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .reboot import RebootRequest
		return RebootRequest(self.request_adapter, path_parameters)

	def rename(self,
		cloudPC_id: str,
	) -> RenameRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .rename import RenameRequest
		return RenameRequest(self.request_adapter, path_parameters)

	def restore(self,
		cloudPC_id: str,
	) -> RestoreRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def troubleshoot(self,
		cloudPC_id: str,
	) -> TroubleshootRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .troubleshoot import TroubleshootRequest
		return TroubleshootRequest(self.request_adapter, path_parameters)

