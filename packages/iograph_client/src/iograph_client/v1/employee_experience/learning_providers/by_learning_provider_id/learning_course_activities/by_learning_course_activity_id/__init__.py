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
from iograph_models.v1.learning_course_activity import LearningCourseActivity
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByLearningCourseActivityIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/employeeExperience/learningProviders/{learningProvider%2Did}/learningCourseActivities/{learningCourseActivity%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> LearningCourseActivity:
		"""
		Get learningCourseActivities from employeeExperience
		
		"""
		tags = ['employeeExperience.learningProvider']

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
		return await self.request_adapter.send_async(request_info, LearningCourseActivity, error_mapping)

	async def patch(
		self,
		body: LearningCourseActivity,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> LearningCourseActivity:
		"""
		Update learningCourseActivity
		Update the properties of a learningCourseActivity object. 
		Find more info here: https://learn.microsoft.com/graph/api/learningcourseactivity-update?view=graph-rest-1.0
		"""
		tags = ['employeeExperience.learningProvider']

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
		return await self.request_adapter.send_async(request_info, LearningCourseActivity, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete learningCourseActivity
		Delete a learningCourseActivity object using the course activity ID of either an assignment or a self-initiated activity.
		Find more info here: https://learn.microsoft.com/graph/api/learningcourseactivity-delete?view=graph-rest-1.0
		"""
		tags = ['employeeExperience.learningProvider']
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



	def with_url(self, raw_url: str) -> ByLearningCourseActivityIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByLearningCourseActivityIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByLearningCourseActivityIdRequest(self.request_adapter, self.path_parameters)

