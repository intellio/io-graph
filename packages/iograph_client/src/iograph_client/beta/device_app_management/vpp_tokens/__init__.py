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
	from .sync_license_counts import SyncLicenseCountsRequest
	from .get_licenses_for_app_with_bundleid import GetLicensesForAppWithBundleIdRequest
	from .count import CountRequest
	from .by_vpp_token_id import ByVppTokenIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.vpp_token import VppToken
from iograph_models.beta.vpp_token_collection_response import VppTokenCollectionResponse


class VppTokensRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/vppTokens", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VppTokenCollectionResponse:
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
		return await self.request_adapter.send_async(request_info, VppTokenCollectionResponse, error_mapping)

	async def post(
		self,
		body: VppToken,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VppToken:
		"""
		Create new navigation property to vppTokens for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.vppToken']

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
		return await self.request_adapter.send_async(request_info, VppToken, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> VppTokensRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: VppTokensRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return VppTokensRequest(self.request_adapter, self.path_parameters)

	def by_vpp_token_id(self,
		vppToken_id: str,
	) -> ByVppTokenIdRequest:
		if vppToken_id is None:
			raise TypeError("vppToken_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["vppToken%2Did"] =  vppToken_id

		from .by_vpp_token_id import ByVppTokenIdRequest
		return ByVppTokenIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	def get_licenses_for_app_with_bundleid(self,
		bundleId: str,
	) -> GetLicensesForAppWithBundleIdRequest:
		if bundleId is None:
			raise TypeError("bundleId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bundleId"] =  bundleId

		from .get_licenses_for_app_with_bundleid import GetLicensesForAppWithBundleIdRequest
		return GetLicensesForAppWithBundleIdRequest(self.request_adapter, path_parameters)

	@property
	def sync_license_counts(self,
	) -> SyncLicenseCountsRequest:
		from .sync_license_counts import SyncLicenseCountsRequest
		return SyncLicenseCountsRequest(self.request_adapter, self.path_parameters)

