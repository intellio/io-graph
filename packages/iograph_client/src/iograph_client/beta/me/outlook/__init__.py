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
	from .tasks import TasksRequest
	from .task_groups import TaskGroupsRequest
	from .task_folders import TaskFoldersRequest
	from .supported_time_zones_with_timezonestandard import SupportedTimeZonesWithTimeZoneStandardRequest
	from .supported_time_zones import SupportedTimeZonesRequest
	from .supported_languages import SupportedLanguagesRequest
	from .master_categories import MasterCategoriesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.outlook_user import OutlookUser


class OutlookRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/outlook", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OutlookUser:
		"""
		Get outlook from me
		Selective Outlook services available to the user. Read-only. Nullable.
		"""
		tags = ['me.outlookUser']

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

	@property
	def master_categories(self,
	) -> MasterCategoriesRequest:
		from .master_categories import MasterCategoriesRequest
		return MasterCategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def supported_languages(self,
	) -> SupportedLanguagesRequest:
		from .supported_languages import SupportedLanguagesRequest
		return SupportedLanguagesRequest(self.request_adapter, self.path_parameters)

	@property
	def supported_time_zones(self,
	) -> SupportedTimeZonesRequest:
		from .supported_time_zones import SupportedTimeZonesRequest
		return SupportedTimeZonesRequest(self.request_adapter, self.path_parameters)

	def supported_time_zones_with_timezonestandard(self,
		TimeZoneStandard: str,
	) -> SupportedTimeZonesWithTimeZoneStandardRequest:
		if TimeZoneStandard is None:
			raise TypeError("TimeZoneStandard cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["TimeZoneStandard"] =  TimeZoneStandard

		from .supported_time_zones_with_timezonestandard import SupportedTimeZonesWithTimeZoneStandardRequest
		return SupportedTimeZonesWithTimeZoneStandardRequest(self.request_adapter, path_parameters)

	@property
	def task_folders(self,
	) -> TaskFoldersRequest:
		from .task_folders import TaskFoldersRequest
		return TaskFoldersRequest(self.request_adapter, self.path_parameters)

	@property
	def task_groups(self,
	) -> TaskGroupsRequest:
		from .task_groups import TaskGroupsRequest
		return TaskGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def tasks(self,
	) -> TasksRequest:
		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, self.path_parameters)

