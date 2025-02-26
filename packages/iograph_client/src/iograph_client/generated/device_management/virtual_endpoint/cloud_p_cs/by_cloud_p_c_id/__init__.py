# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.cloud_p_c import CloudPC


class ByCloudPCIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs/{cloudPC%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

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



	@property
	def end_grace_period(self,
	) -> EndGracePeriodRequest:
		from .end_grace_period import EndGracePeriodRequest
		return EndGracePeriodRequest(self.request_adapter, self.path_parameters)

	@property
	def reboot(self,
	) -> RebootRequest:
		from .reboot import RebootRequest
		return RebootRequest(self.request_adapter, self.path_parameters)

	@property
	def rename(self,
	) -> RenameRequest:
		from .rename import RenameRequest
		return RenameRequest(self.request_adapter, self.path_parameters)

	@property
	def restore(self,
	) -> RestoreRequest:
		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, self.path_parameters)

	@property
	def troubleshoot(self,
	) -> TroubleshootRequest:
		from .troubleshoot import TroubleshootRequest
		return TroubleshootRequest(self.request_adapter, self.path_parameters)

