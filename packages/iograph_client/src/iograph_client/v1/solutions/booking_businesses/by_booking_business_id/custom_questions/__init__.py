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
	from .count import CountRequest
	from .by_booking_custom_question_id import ByBookingCustomQuestionIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.booking_custom_question import BookingCustomQuestion
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.booking_custom_question_collection_response import BookingCustomQuestionCollectionResponse


class CustomQuestionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/bookingBusinesses/{bookingBusiness%2Did}/customQuestions", path_parameters)

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


	def with_url(self, raw_url: str) -> CustomQuestionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CustomQuestionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CustomQuestionsRequest(self.request_adapter, self.path_parameters)

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

	def count(self,
		bookingBusiness_id: str,
	) -> CountRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

