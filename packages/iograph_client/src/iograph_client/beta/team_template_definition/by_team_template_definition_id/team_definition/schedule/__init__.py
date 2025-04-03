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
	from .times_off import TimesOffRequest
	from .time_off_requests import TimeOffRequestsRequest
	from .time_off_reasons import TimeOffReasonsRequest
	from .time_cards import TimeCardsRequest
	from .swap_shifts_change_requests import SwapShiftsChangeRequestsRequest
	from .shifts_role_definitions import ShiftsRoleDefinitionsRequest
	from .shifts import ShiftsRequest
	from .scheduling_groups import SchedulingGroupsRequest
	from .open_shifts import OpenShiftsRequest
	from .open_shift_change_requests import OpenShiftChangeRequestsRequest
	from .offer_shift_requests import OfferShiftRequestsRequest
	from .share import ShareRequest
	from .day_notes import DayNotesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.schedule import Schedule


class ScheduleRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamTemplateDefinition/{teamTemplateDefinition%2Did}/teamDefinition/schedule", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Schedule:
		"""
		Get schedule from teamTemplateDefinition
		The schedule of shifts for this team.
		"""
		tags = ['teamTemplateDefinition.team']

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
		Update the navigation property schedule in teamTemplateDefinition
		
		"""
		tags = ['teamTemplateDefinition.team']

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
		Delete navigation property schedule for teamTemplateDefinition
		
		"""
		tags = ['teamTemplateDefinition.team']
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
		teamTemplateDefinition_id: str,
	) -> DayNotesRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .day_notes import DayNotesRequest
		return DayNotesRequest(self.request_adapter, path_parameters)

	def share(self,
		teamTemplateDefinition_id: str,
	) -> ShareRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .share import ShareRequest
		return ShareRequest(self.request_adapter, path_parameters)

	def offer_shift_requests(self,
		teamTemplateDefinition_id: str,
	) -> OfferShiftRequestsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .offer_shift_requests import OfferShiftRequestsRequest
		return OfferShiftRequestsRequest(self.request_adapter, path_parameters)

	def open_shift_change_requests(self,
		teamTemplateDefinition_id: str,
	) -> OpenShiftChangeRequestsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .open_shift_change_requests import OpenShiftChangeRequestsRequest
		return OpenShiftChangeRequestsRequest(self.request_adapter, path_parameters)

	def open_shifts(self,
		teamTemplateDefinition_id: str,
	) -> OpenShiftsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .open_shifts import OpenShiftsRequest
		return OpenShiftsRequest(self.request_adapter, path_parameters)

	def scheduling_groups(self,
		teamTemplateDefinition_id: str,
	) -> SchedulingGroupsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .scheduling_groups import SchedulingGroupsRequest
		return SchedulingGroupsRequest(self.request_adapter, path_parameters)

	def shifts(self,
		teamTemplateDefinition_id: str,
	) -> ShiftsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .shifts import ShiftsRequest
		return ShiftsRequest(self.request_adapter, path_parameters)

	def shifts_role_definitions(self,
		teamTemplateDefinition_id: str,
	) -> ShiftsRoleDefinitionsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .shifts_role_definitions import ShiftsRoleDefinitionsRequest
		return ShiftsRoleDefinitionsRequest(self.request_adapter, path_parameters)

	def swap_shifts_change_requests(self,
		teamTemplateDefinition_id: str,
	) -> SwapShiftsChangeRequestsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .swap_shifts_change_requests import SwapShiftsChangeRequestsRequest
		return SwapShiftsChangeRequestsRequest(self.request_adapter, path_parameters)

	def time_cards(self,
		teamTemplateDefinition_id: str,
	) -> TimeCardsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .time_cards import TimeCardsRequest
		return TimeCardsRequest(self.request_adapter, path_parameters)

	def time_off_reasons(self,
		teamTemplateDefinition_id: str,
	) -> TimeOffReasonsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .time_off_reasons import TimeOffReasonsRequest
		return TimeOffReasonsRequest(self.request_adapter, path_parameters)

	def time_off_requests(self,
		teamTemplateDefinition_id: str,
	) -> TimeOffRequestsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .time_off_requests import TimeOffRequestsRequest
		return TimeOffRequestsRequest(self.request_adapter, path_parameters)

	def times_off(self,
		teamTemplateDefinition_id: str,
	) -> TimesOffRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id

		from .times_off import TimesOffRequest
		return TimesOffRequest(self.request_adapter, path_parameters)

