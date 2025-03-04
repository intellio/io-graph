# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_virtual_event_registration_question_base_id import ByVirtualEventRegistrationQuestionBaseIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.virtual_event_registration_question_base_collection_response import VirtualEventRegistrationQuestionBaseCollectionResponse


class QuestionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/webinars/{virtualEventWebinar%2Did}/registrationConfiguration/questions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEventRegistrationQuestionBaseCollectionResponse:
		"""
		List questions
		Get a list of all registration questions for a webinar. The list can include either predefined registration questions or custom registration questions.
		Find more info here: https://learn.microsoft.com/graph/api/virtualeventregistrationconfiguration-list-questions?view=graph-rest-1.0
		"""
		tags = ['solutions.virtualEventsRoot']

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
		return await self.request_adapter.send_async(request_info, VirtualEventRegistrationQuestionBaseCollectionResponse, error_mapping)

	async def post(
		self,
		body: VirtualEventRegistrationQuestionBase,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VirtualEventRegistrationQuestionBase:
		"""
		Create virtualEventRegistrationCustomQuestion
		Create a registration question for a webinar. You can create either a predefined registration question or a custom registration question.
		Find more info here: https://learn.microsoft.com/graph/api/virtualeventregistrationconfiguration-post-questions?view=graph-rest-1.0
		"""
		tags = ['solutions.virtualEventsRoot']

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
		return await self.request_adapter.send_async(request_info, VirtualEventRegistrationQuestionBase, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> QuestionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: QuestionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return QuestionsRequest(self.request_adapter, self.path_parameters)

	def by_virtual_event_registration_question_base_id(self,
		virtualEventWebinar_id: str,
		virtualEventRegistrationQuestionBase_id: str,
	) -> ByVirtualEventRegistrationQuestionBaseIdRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")
		if virtualEventRegistrationQuestionBase_id is None:
			raise TypeError("virtualEventRegistrationQuestionBase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id
		path_parameters["virtualEventRegistrationQuestionBase%2Did"] =  virtualEventRegistrationQuestionBase_id

		from .by_virtual_event_registration_question_base_id import ByVirtualEventRegistrationQuestionBaseIdRequest
		return ByVirtualEventRegistrationQuestionBaseIdRequest(self.request_adapter, path_parameters)

	def count(self,
		virtualEventWebinar_id: str,
	) -> CountRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

