# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_calendar_group_id import ByCalendarGroupIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.calendar_group import CalendarGroup
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.calendar_group_collection_response import CalendarGroupCollectionResponse


class CalendarGroupsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/calendarGroups"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CalendarGroupCollectionResponse:
		"""
		Get calendarGroups from users
		The user's calendar groups. Read-only. Nullable.
		"""
		tags = ['users.calendarGroup']

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
		return await self.request_adapter.send_async(request_info, CalendarGroupCollectionResponse, error_mapping)

	async def post(
		self,
		body: CalendarGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CalendarGroup:
		"""
		Create new navigation property to calendarGroups for users
		
		"""
		tags = ['users.calendarGroup']

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
		return await self.request_adapter.send_async(request_info, CalendarGroup, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_calendar_group_id(self,
		user_id: str,
		calendarGroup_id: str,
	) -> ByCalendarGroupIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id

		from .by_calendar_group_id import ByCalendarGroupIdRequest
		return ByCalendarGroupIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

