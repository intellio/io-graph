# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_booking_custom_question_id import ByBookingCustomQuestionIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.booking_custom_question import BookingCustomQuestion
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.booking_custom_question_collection_response import BookingCustomQuestionCollectionResponse


class CustomQuestionsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/solutions/bookingBusinesses/{bookingBusiness%2Did}/customQuestions"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BookingCustomQuestionCollectionResponse:
		"""
		List customQuestions
		Get the bookingCustomQuestion resources associated with a bookingBusiness.
		Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-list-customquestions?view=graph-rest-1.0
		"""
		tags = ['solutions.bookingBusiness']

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
		return await self.request_adapter.send_async(request_info, BookingCustomQuestionCollectionResponse, error_mapping)

	async def post(
		self,
		body: BookingCustomQuestion,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BookingCustomQuestion:
		"""
		Create bookingCustomQuestion
		Create a new bookingCustomQuestion object.
		Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-post-customquestions?view=graph-rest-1.0
		"""
		tags = ['solutions.bookingBusiness']

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
		return await self.request_adapter.send_async(request_info, BookingCustomQuestion, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_booking_custom_question_id(self,
		bookingBusiness_id: str,
		bookingCustomQuestion_id: str,
	) -> ByBookingCustomQuestionIdRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")
		if bookingCustomQuestion_id is None:
			raise TypeError("bookingCustomQuestion_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id
		path_parameters["bookingCustomQuestion%2Did"] =  bookingCustomQuestion_id

		from .by_booking_custom_question_id import ByBookingCustomQuestionIdRequest
		return ByBookingCustomQuestionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

