# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .learning_course_activities import LearningCourseActivitiesRequest
	from .learning_contents import LearningContentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.learning_provider import LearningProvider


class ByLearningProviderIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/employeeExperience/learningProviders/{learningProvider%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

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



	@property
	def learning_contents(self,
	) -> LearningContentsRequest:
		from .learning_contents import LearningContentsRequest
		return LearningContentsRequest(self.request_adapter, self.path_parameters)

	@property
	def learning_course_activities(self,
	) -> LearningCourseActivitiesRequest:
		from .learning_course_activities import LearningCourseActivitiesRequest
		return LearningCourseActivitiesRequest(self.request_adapter, self.path_parameters)

