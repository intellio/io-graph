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
	from .supported_time_zones_with_timezonestandard import SupportedTimeZonesWithTimeZoneStandardRequest
	from .supported_time_zones import SupportedTimeZonesRequest
	from .supported_languages import SupportedLanguagesRequest
	from .master_categories import MasterCategoriesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.outlook_user import OutlookUser


class OutlookRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/outlook", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OutlookUser:
		"""
		Get outlook from users
		
		"""
		tags = ['users.outlookUser']

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
		return await self.request_adapter.send_async(request_info, OutlookUser, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> OutlookRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OutlookRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OutlookRequest(self.request_adapter, self.path_parameters)

	def master_categories(self,
		user_id: str,
	) -> MasterCategoriesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .master_categories import MasterCategoriesRequest
		return MasterCategoriesRequest(self.request_adapter, path_parameters)

	def supported_languages(self,
		user_id: str,
	) -> SupportedLanguagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .supported_languages import SupportedLanguagesRequest
		return SupportedLanguagesRequest(self.request_adapter, path_parameters)

	def supported_time_zones(self,
		user_id: str,
	) -> SupportedTimeZonesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .supported_time_zones import SupportedTimeZonesRequest
		return SupportedTimeZonesRequest(self.request_adapter, path_parameters)

	def supported_time_zones_with_timezonestandard(self,
		user_id: str,
		TimeZoneStandard: str,
	) -> SupportedTimeZonesWithTimeZoneStandardRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if TimeZoneStandard is None:
			raise TypeError("TimeZoneStandard cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["TimeZoneStandard"] =  TimeZoneStandard

		from .supported_time_zones_with_timezonestandard import SupportedTimeZonesWithTimeZoneStandardRequest
		return SupportedTimeZonesWithTimeZoneStandardRequest(self.request_adapter, path_parameters)

