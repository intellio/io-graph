# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .learning_providers import LearningProvidersRequest
	from .learning_course_activities_with_externalcourseactivityid import LearningCourseActivitiesWithExternalcourseActivityIdRequest
	from .learning_course_activities import LearningCourseActivitiesRequest
	from .engagement_async_operations import EngagementAsyncOperationsRequest
	from .communities import CommunitiesRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.employee_experience import EmployeeExperience
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class EmployeeExperienceRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/employeeExperience", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EmployeeExperience:
		"""
		Get employeeExperience
		
		"""
		tags = ['employeeExperience.employeeExperience']

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
		return await self.request_adapter.send_async(request_info, EmployeeExperience, error_mapping)

	async def patch(
		self,
		body: EmployeeExperience,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EmployeeExperience:
		"""
		Update employeeExperience
		
		"""
		tags = ['employeeExperience.employeeExperience']

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
		return await self.request_adapter.send_async(request_info, EmployeeExperience, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")


	def with_url(self, raw_url: str) -> EmployeeExperienceRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EmployeeExperienceRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EmployeeExperienceRequest(self.request_adapter, self.path_parameters)

	@property
	def communities(self,
	) -> CommunitiesRequest:
		from .communities import CommunitiesRequest
		return CommunitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def engagement_async_operations(self,
	) -> EngagementAsyncOperationsRequest:
		from .engagement_async_operations import EngagementAsyncOperationsRequest
		return EngagementAsyncOperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def learning_course_activities(self,
	) -> LearningCourseActivitiesRequest:
		from .learning_course_activities import LearningCourseActivitiesRequest
		return LearningCourseActivitiesRequest(self.request_adapter, self.path_parameters)

	def learning_course_activities_with_externalcourseactivityid(self,
		externalcourseActivityId: str,
	) -> LearningCourseActivitiesWithExternalcourseActivityIdRequest:
		if externalcourseActivityId is None:
			raise TypeError("externalcourseActivityId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalcourseActivityId"] =  externalcourseActivityId

		from .learning_course_activities_with_externalcourseactivityid import LearningCourseActivitiesWithExternalcourseActivityIdRequest
		return LearningCourseActivitiesWithExternalcourseActivityIdRequest(self.request_adapter, path_parameters)

	@property
	def learning_providers(self,
	) -> LearningProvidersRequest:
		from .learning_providers import LearningProvidersRequest
		return LearningProvidersRequest(self.request_adapter, self.path_parameters)

