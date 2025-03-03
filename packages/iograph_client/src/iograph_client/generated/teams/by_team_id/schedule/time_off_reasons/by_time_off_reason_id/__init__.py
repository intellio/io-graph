# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.time_off_reason import TimeOffReason
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByTimeOffReasonIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teams/{team%2Did}/schedule/timeOffReasons/{timeOffReason%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TimeOffReason:
		"""
		Get timeOffReason
		Retrieve the properties and relationships of a timeOffReason object by ID.
		Find more info here: https://learn.microsoft.com/graph/api/timeoffreason-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, TimeOffReason, error_mapping)

	async def patch(
		self,
		body: TimeOffReason,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TimeOffReason:
		"""
		Replace timeOffReason
		Replace an existing timeOffReason. If the specified timeOffReason doesn't exist, this method returns 404 Not found.
		Find more info here: https://learn.microsoft.com/graph/api/timeoffreason-put?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, TimeOffReason, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete timeOffReason
		Mark a timeOffReason as inactive by setting the isActive property. Every team must include at least one timeoff reason. This method doesn't remove the specified timeOffReason instance. timeOffItem instances that have been assigned this reason remain assigned to this reason.
		Find more info here: https://learn.microsoft.com/graph/api/timeoffreason-delete?view=graph-rest-1.0
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



	def with_url(self, raw_url: str) -> ByTimeOffReasonIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTimeOffReasonIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTimeOffReasonIdRequest(self.request_adapter, self.path_parameters)

