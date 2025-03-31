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
	from .graph_windows_web_app import GraphWindowsWebAppRequest
	from .graph_windows_universal_app_x import GraphWindowsUniversalAppXRequest
	from .graph_windows_mobile_m_s_i import GraphWindowsMobileMSIRequest
	from .graph_windows_app_x import GraphWindowsAppXRequest
	from .graph_win32_lob_app import GraphWin32LobAppRequest
	from .graph_microsoft_store_for_business_app import GraphMicrosoftStoreForBusinessAppRequest
	from .graph_managed_mobile_lob_app import GraphManagedMobileLobAppRequest
	from .graph_managed_i_o_s_lob_app import GraphManagedIOSLobAppRequest
	from .graph_managed_android_lob_app import GraphManagedAndroidLobAppRequest
	from .graph_mac_o_s_lob_app import GraphMacOSLobAppRequest
	from .graph_mac_o_s_dmg_app import GraphMacOSDmgAppRequest
	from .graph_ios_vpp_app import GraphIosVppAppRequest
	from .graph_ios_store_app import GraphIosStoreAppRequest
	from .graph_ios_lob_app import GraphIosLobAppRequest
	from .graph_android_store_app import GraphAndroidStoreAppRequest
	from .graph_android_lob_app import GraphAndroidLobAppRequest
	from .count import CountRequest
	from .by_mobile_app_id import ByMobileAppIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.mobile_app import MobileApp
from iograph_models.v1.mobile_app_collection_response import MobileAppCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class MobileAppsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileApps", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MobileAppCollectionResponse:
		"""
		List windowsMobileMSIs
		List properties and relationships of the windowsMobileMSI objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-apps-windowsmobilemsi-list?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.mobileApp']

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
		return await self.request_adapter.send_async(request_info, MobileAppCollectionResponse, error_mapping)

	async def post(
		self,
		body: MobileApp,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MobileApp:
		"""
		Create managedIOSStoreApp
		Create a new managedIOSStoreApp object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-apps-managediosstoreapp-create?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.mobileApp']

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
		return await self.request_adapter.send_async(request_info, MobileApp, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MobileAppsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MobileAppsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MobileAppsRequest(self.request_adapter, self.path_parameters)

	def by_mobile_app_id(self,
		mobileApp_id: str,
	) -> ByMobileAppIdRequest:
		if mobileApp_id is None:
			raise TypeError("mobileApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileApp%2Did"] =  mobileApp_id

		from .by_mobile_app_id import ByMobileAppIdRequest
		return ByMobileAppIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_android_lob_app(self,
	) -> GraphAndroidLobAppRequest:
		from .graph_android_lob_app import GraphAndroidLobAppRequest
		return GraphAndroidLobAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_android_store_app(self,
	) -> GraphAndroidStoreAppRequest:
		from .graph_android_store_app import GraphAndroidStoreAppRequest
		return GraphAndroidStoreAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_ios_lob_app(self,
	) -> GraphIosLobAppRequest:
		from .graph_ios_lob_app import GraphIosLobAppRequest
		return GraphIosLobAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_ios_store_app(self,
	) -> GraphIosStoreAppRequest:
		from .graph_ios_store_app import GraphIosStoreAppRequest
		return GraphIosStoreAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_ios_vpp_app(self,
	) -> GraphIosVppAppRequest:
		from .graph_ios_vpp_app import GraphIosVppAppRequest
		return GraphIosVppAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_mac_o_s_dmg_app(self,
	) -> GraphMacOSDmgAppRequest:
		from .graph_mac_o_s_dmg_app import GraphMacOSDmgAppRequest
		return GraphMacOSDmgAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_mac_o_s_lob_app(self,
	) -> GraphMacOSLobAppRequest:
		from .graph_mac_o_s_lob_app import GraphMacOSLobAppRequest
		return GraphMacOSLobAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_managed_android_lob_app(self,
	) -> GraphManagedAndroidLobAppRequest:
		from .graph_managed_android_lob_app import GraphManagedAndroidLobAppRequest
		return GraphManagedAndroidLobAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_managed_i_o_s_lob_app(self,
	) -> GraphManagedIOSLobAppRequest:
		from .graph_managed_i_o_s_lob_app import GraphManagedIOSLobAppRequest
		return GraphManagedIOSLobAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_managed_mobile_lob_app(self,
	) -> GraphManagedMobileLobAppRequest:
		from .graph_managed_mobile_lob_app import GraphManagedMobileLobAppRequest
		return GraphManagedMobileLobAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_microsoft_store_for_business_app(self,
	) -> GraphMicrosoftStoreForBusinessAppRequest:
		from .graph_microsoft_store_for_business_app import GraphMicrosoftStoreForBusinessAppRequest
		return GraphMicrosoftStoreForBusinessAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_win32_lob_app(self,
	) -> GraphWin32LobAppRequest:
		from .graph_win32_lob_app import GraphWin32LobAppRequest
		return GraphWin32LobAppRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_windows_app_x(self,
	) -> GraphWindowsAppXRequest:
		from .graph_windows_app_x import GraphWindowsAppXRequest
		return GraphWindowsAppXRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_windows_mobile_m_s_i(self,
	) -> GraphWindowsMobileMSIRequest:
		from .graph_windows_mobile_m_s_i import GraphWindowsMobileMSIRequest
		return GraphWindowsMobileMSIRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_windows_universal_app_x(self,
	) -> GraphWindowsUniversalAppXRequest:
		from .graph_windows_universal_app_x import GraphWindowsUniversalAppXRequest
		return GraphWindowsUniversalAppXRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_windows_web_app(self,
	) -> GraphWindowsWebAppRequest:
		from .graph_windows_web_app import GraphWindowsWebAppRequest
		return GraphWindowsWebAppRequest(self.request_adapter, self.path_parameters)

