# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .learning_course_activities_with_externalcourseactivityid import LearningCourseActivitiesWithExternalcourseActivityIdRequest
	from .learning_course_activities import LearningCourseActivitiesRequest
	from .learning_contents_with_externalid import LearningContentsWithExternalIdRequest
	from .learning_contents import LearningContentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.learning_provider import LearningProvider


class ByLearningProviderIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/employeeExperience/learningProviders/{learningProvider%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> LearningProvider:
		"""
		Get learningProvider
		Read the properties and relationships of a learningProvider object.
		Find more info here: https://learn.microsoft.com/graph/api/learningprovider-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, LearningProvider, error_mapping)

	async def patch(
		self,
		body: LearningProvider,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> LearningProvider:
		"""
		Update learningProvider
		Update the properties of a learningProvider object.
		Find more info here: https://learn.microsoft.com/graph/api/learningprovider-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, LearningProvider, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete learningProvider
		Delete a learningProvider resource and remove its registration in Viva Learning for a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/employeeexperience-delete-learningproviders?view=graph-rest-1.0
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



	def with_url(self, raw_url: str) -> ByLearningProviderIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByLearningProviderIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByLearningProviderIdRequest(self.request_adapter, self.path_parameters)

	def learning_contents(self,
		learningProvider_id: str,
	) -> LearningContentsRequest:
		if learningProvider_id is None:
			raise TypeError("learningProvider_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["learningProvider%2Did"] =  learningProvider_id

		from .learning_contents import LearningContentsRequest
		return LearningContentsRequest(self.request_adapter, path_parameters)

	def learning_contents_with_externalid(self,
		learningProvider_id: str,
		externalId: str,
	) -> LearningContentsWithExternalIdRequest:
		if learningProvider_id is None:
			raise TypeError("learningProvider_id cannot be null.")
		if externalId is None:
			raise TypeError("externalId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["learningProvider%2Did"] =  learningProvider_id
		path_parameters["externalId"] =  externalId

		from .learning_contents_with_externalid import LearningContentsWithExternalIdRequest
		return LearningContentsWithExternalIdRequest(self.request_adapter, path_parameters)

	def learning_course_activities(self,
		learningProvider_id: str,
	) -> LearningCourseActivitiesRequest:
		if learningProvider_id is None:
			raise TypeError("learningProvider_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["learningProvider%2Did"] =  learningProvider_id

		from .learning_course_activities import LearningCourseActivitiesRequest
		return LearningCourseActivitiesRequest(self.request_adapter, path_parameters)

	def learning_course_activities_with_externalcourseactivityid(self,
		learningProvider_id: str,
		externalcourseActivityId: str,
	) -> LearningCourseActivitiesWithExternalcourseActivityIdRequest:
		if learningProvider_id is None:
			raise TypeError("learningProvider_id cannot be null.")
		if externalcourseActivityId is None:
			raise TypeError("externalcourseActivityId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["learningProvider%2Did"] =  learningProvider_id
		path_parameters["externalcourseActivityId"] =  externalcourseActivityId

		from .learning_course_activities_with_externalcourseactivityid import LearningCourseActivitiesWithExternalcourseActivityIdRequest
		return LearningCourseActivitiesWithExternalcourseActivityIdRequest(self.request_adapter, path_parameters)

