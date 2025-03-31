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
	from .disconnect import DisconnectRequest
	from .connect import ConnectRequest
	from .count import CountRequest
	from .by_chrome_o_s_onboarding_settings_id import ByChromeOSOnboardingSettingsIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.chrome_o_s_onboarding_settings_collection_response import ChromeOSOnboardingSettingsCollectionResponse


class ChromeOSOnboardingSettingsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/chromeOSOnboardingSettings", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ChromeOSOnboardingSettingsCollectionResponse:
		"""
		Get chromeOSOnboardingSettings from deviceManagement
		Collection of ChromeOSOnboardingSettings settings associated with account.
		"""
		tags = ['deviceManagement.chromeOSOnboardingSettings']

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
		return await self.request_adapter.send_async(request_info, ChromeOSOnboardingSettingsCollectionResponse, error_mapping)

	async def post(
		self,
		body: ChromeOSOnboardingSettings,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ChromeOSOnboardingSettings:
		"""
		Create new navigation property to chromeOSOnboardingSettings for deviceManagement
		
		"""
		tags = ['deviceManagement.chromeOSOnboardingSettings']

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
		return await self.request_adapter.send_async(request_info, ChromeOSOnboardingSettings, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ChromeOSOnboardingSettingsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ChromeOSOnboardingSettingsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ChromeOSOnboardingSettingsRequest(self.request_adapter, self.path_parameters)

	def by_chrome_o_s_onboarding_settings_id(self,
		chromeOSOnboardingSettings_id: str,
	) -> ByChromeOSOnboardingSettingsIdRequest:
		if chromeOSOnboardingSettings_id is None:
			raise TypeError("chromeOSOnboardingSettings_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["chromeOSOnboardingSettings%2Did"] =  chromeOSOnboardingSettings_id

		from .by_chrome_o_s_onboarding_settings_id import ByChromeOSOnboardingSettingsIdRequest
		return ByChromeOSOnboardingSettingsIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def connect(self,
	) -> ConnectRequest:
		from .connect import ConnectRequest
		return ConnectRequest(self.request_adapter, self.path_parameters)

	@property
	def disconnect(self,
	) -> DisconnectRequest:
		from .disconnect import DisconnectRequest
		return DisconnectRequest(self.request_adapter, self.path_parameters)

