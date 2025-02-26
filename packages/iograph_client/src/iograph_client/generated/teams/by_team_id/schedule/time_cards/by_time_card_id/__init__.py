# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .start_break import StartBreakRequest
	from .end_break import EndBreakRequest
	from .confirm import ConfirmRequest
	from .clock_out import ClockOutRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.time_card import TimeCard
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByTimeCardIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/teams/{team%2Did}/schedule/timeCards/{timeCard%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TimeCard:
		"""
		Get timeCards from teams
		The time cards in the schedule.
		"""
		tags = ['teams.schedule']

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
		return await self.request_adapter.send_async(request_info, TimeCard, error_mapping)

	async def patch(
		self,
		body: TimeCard,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TimeCard:
		"""
		Update the navigation property timeCards in teams
		
		"""
		tags = ['teams.schedule']

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
		return await self.request_adapter.send_async(request_info, TimeCard, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete timeCard
		Delete a timeCard instance in a schedule.
		Find more info here: https://learn.microsoft.com/graph/api/schedule-delete-timecards?view=graph-rest-1.0
		"""
		tags = ['teams.schedule']
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



	@property
	def clock_out(self,
	) -> ClockOutRequest:
		from .clock_out import ClockOutRequest
		return ClockOutRequest(self.request_adapter, self.path_parameters)

	@property
	def confirm(self,
	) -> ConfirmRequest:
		from .confirm import ConfirmRequest
		return ConfirmRequest(self.request_adapter, self.path_parameters)

	@property
	def end_break(self,
	) -> EndBreakRequest:
		from .end_break import EndBreakRequest
		return EndBreakRequest(self.request_adapter, self.path_parameters)

	@property
	def start_break(self,
	) -> StartBreakRequest:
		from .start_break import StartBreakRequest
		return StartBreakRequest(self.request_adapter, self.path_parameters)

