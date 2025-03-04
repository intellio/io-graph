# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .times_off import TimesOffRequest
	from .time_off_requests import TimeOffRequestsRequest
	from .time_off_reasons import TimeOffReasonsRequest
	from .time_cards import TimeCardsRequest
	from .swap_shifts_change_requests import SwapShiftsChangeRequestsRequest
	from .shifts import ShiftsRequest
	from .scheduling_groups import SchedulingGroupsRequest
	from .open_shifts import OpenShiftsRequest
	from .open_shift_change_requests import OpenShiftChangeRequestsRequest
	from .offer_shift_requests import OfferShiftRequestsRequest
	from .share import ShareRequest
	from .day_notes import DayNotesRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.schedule import Schedule
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ScheduleRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/joinedTeams/{team%2Did}/schedule", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Schedule:
		"""
		Get schedule from users
		The schedule of shifts for this team.
		"""
		tags = ['users.team']

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
		return await self.request_adapter.send_async(request_info, Schedule, error_mapping)

	async def put(
		self,
		body: Schedule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Schedule:
		"""
		Update the navigation property schedule in users
		
		"""
		tags = ['users.team']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PUT,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, Schedule, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property schedule for users
		
		"""
		tags = ['users.team']
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



	def with_url(self, raw_url: str) -> ScheduleRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ScheduleRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ScheduleRequest(self.request_adapter, self.path_parameters)

	def day_notes(self,
		user_id: str,
		team_id: str,
	) -> DayNotesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .day_notes import DayNotesRequest
		return DayNotesRequest(self.request_adapter, path_parameters)

	def share(self,
		user_id: str,
		team_id: str,
	) -> ShareRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .share import ShareRequest
		return ShareRequest(self.request_adapter, path_parameters)

	def offer_shift_requests(self,
		user_id: str,
		team_id: str,
	) -> OfferShiftRequestsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .offer_shift_requests import OfferShiftRequestsRequest
		return OfferShiftRequestsRequest(self.request_adapter, path_parameters)

	def open_shift_change_requests(self,
		user_id: str,
		team_id: str,
	) -> OpenShiftChangeRequestsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .open_shift_change_requests import OpenShiftChangeRequestsRequest
		return OpenShiftChangeRequestsRequest(self.request_adapter, path_parameters)

	def open_shifts(self,
		user_id: str,
		team_id: str,
	) -> OpenShiftsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .open_shifts import OpenShiftsRequest
		return OpenShiftsRequest(self.request_adapter, path_parameters)

	def scheduling_groups(self,
		user_id: str,
		team_id: str,
	) -> SchedulingGroupsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .scheduling_groups import SchedulingGroupsRequest
		return SchedulingGroupsRequest(self.request_adapter, path_parameters)

	def shifts(self,
		user_id: str,
		team_id: str,
	) -> ShiftsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .shifts import ShiftsRequest
		return ShiftsRequest(self.request_adapter, path_parameters)

	def swap_shifts_change_requests(self,
		user_id: str,
		team_id: str,
	) -> SwapShiftsChangeRequestsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .swap_shifts_change_requests import SwapShiftsChangeRequestsRequest
		return SwapShiftsChangeRequestsRequest(self.request_adapter, path_parameters)

	def time_cards(self,
		user_id: str,
		team_id: str,
	) -> TimeCardsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .time_cards import TimeCardsRequest
		return TimeCardsRequest(self.request_adapter, path_parameters)

	def time_off_reasons(self,
		user_id: str,
		team_id: str,
	) -> TimeOffReasonsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .time_off_reasons import TimeOffReasonsRequest
		return TimeOffReasonsRequest(self.request_adapter, path_parameters)

	def time_off_requests(self,
		user_id: str,
		team_id: str,
	) -> TimeOffRequestsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .time_off_requests import TimeOffRequestsRequest
		return TimeOffRequestsRequest(self.request_adapter, path_parameters)

	def times_off(self,
		user_id: str,
		team_id: str,
	) -> TimesOffRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["team%2Did"] =  team_id

		from .times_off import TimesOffRequest
		return TimesOffRequest(self.request_adapter, path_parameters)

