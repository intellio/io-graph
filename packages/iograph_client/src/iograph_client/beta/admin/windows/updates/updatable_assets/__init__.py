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
	from .windows_updates_unenroll_assets_by_id import WindowsUpdatesUnenrollAssetsByIdRequest
	from .windows_updates_unenroll_assets import WindowsUpdatesUnenrollAssetsRequest
	from .windows_updates_enroll_assets_by_id import WindowsUpdatesEnrollAssetsByIdRequest
	from .windows_updates_enroll_assets import WindowsUpdatesEnrollAssetsRequest
	from .count import CountRequest
	from .by_updatable_asset_id import ByUpdatableAssetIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset
from iograph_models.beta.windows_updates_updatable_asset_collection_response import WindowsUpdatesUpdatableAssetCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class UpdatableAssetsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/updatableAssets", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsUpdatesUpdatableAssetCollectionResponse:
		"""
		List updatableAssets
		Get a list of updatableAsset objects and their properties. Listing updatable assets returns updatableAsset resources of the following derived types: azureADDevice and updatableAssetGroup. Use list azureADDevice resources or list updatableAssetGroup resources to filter and get resources of only one of the derived types.
		Find more info here: https://learn.microsoft.com/graph/api/adminwindowsupdates-list-updatableassets?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesUpdatableAssetCollectionResponse, error_mapping)

	async def post(
		self,
		body: WindowsUpdatesUpdatableAsset,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsUpdatesUpdatableAsset:
		"""
		Create updatableAssetGroup
		Create a new updatableAssetGroup object. The updatableAssetGroup resource inherits from updatableAsset.
		Find more info here: https://learn.microsoft.com/graph/api/adminwindowsupdates-post-updatableassets-updatableassetgroup?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesUpdatableAsset, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UpdatableAssetsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UpdatableAssetsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UpdatableAssetsRequest(self.request_adapter, self.path_parameters)

	def by_updatable_asset_id(self,
		updatableAsset_id: str,
	) -> ByUpdatableAssetIdRequest:
		if updatableAsset_id is None:
			raise TypeError("updatableAsset_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["updatableAsset%2Did"] =  updatableAsset_id

		from .by_updatable_asset_id import ByUpdatableAssetIdRequest
		return ByUpdatableAssetIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_updates_enroll_assets(self,
	) -> WindowsUpdatesEnrollAssetsRequest:
		from .windows_updates_enroll_assets import WindowsUpdatesEnrollAssetsRequest
		return WindowsUpdatesEnrollAssetsRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_updates_enroll_assets_by_id(self,
	) -> WindowsUpdatesEnrollAssetsByIdRequest:
		from .windows_updates_enroll_assets_by_id import WindowsUpdatesEnrollAssetsByIdRequest
		return WindowsUpdatesEnrollAssetsByIdRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_updates_unenroll_assets(self,
	) -> WindowsUpdatesUnenrollAssetsRequest:
		from .windows_updates_unenroll_assets import WindowsUpdatesUnenrollAssetsRequest
		return WindowsUpdatesUnenrollAssetsRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_updates_unenroll_assets_by_id(self,
	) -> WindowsUpdatesUnenrollAssetsByIdRequest:
		from .windows_updates_unenroll_assets_by_id import WindowsUpdatesUnenrollAssetsByIdRequest
		return WindowsUpdatesUnenrollAssetsByIdRequest(self.request_adapter, self.path_parameters)

