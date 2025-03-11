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
	from .sync_licenses import SyncLicensesRequest
	from .revoke_licenses import RevokeLicensesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.vpp_token import VppToken
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByVppTokenIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/vppTokens/{vppToken%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VppToken:
		"""
		Get vppTokens from deviceAppManagement
		List of Vpp tokens for this organization.
		"""
		tags = ['deviceAppManagement.vppToken']

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
		return await self.request_adapter.send_async(request_info, VppToken, error_mapping)

	async def patch(
		self,
		body: VppToken,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VppToken:
		"""
		Update the navigation property vppTokens in deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.vppToken']

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
		return await self.request_adapter.send_async(request_info, VppToken, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property vppTokens for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.vppToken']
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



	def with_url(self, raw_url: str) -> ByVppTokenIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByVppTokenIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByVppTokenIdRequest(self.request_adapter, self.path_parameters)

	def revoke_licenses(self,
		vppToken_id: str,
	) -> RevokeLicensesRequest:
		if vppToken_id is None:
			raise TypeError("vppToken_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["vppToken%2Did"] =  vppToken_id

		from .revoke_licenses import RevokeLicensesRequest
		return RevokeLicensesRequest(self.request_adapter, path_parameters)

	def sync_licenses(self,
		vppToken_id: str,
	) -> SyncLicensesRequest:
		if vppToken_id is None:
			raise TypeError("vppToken_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["vppToken%2Did"] =  vppToken_id

		from .sync_licenses import SyncLicensesRequest
		return SyncLicensesRequest(self.request_adapter, path_parameters)

