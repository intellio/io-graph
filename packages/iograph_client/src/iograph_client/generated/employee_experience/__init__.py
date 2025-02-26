# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .learning_providers import LearningProvidersRequest
	from .learning_course_activities import LearningCourseActivitiesRequest
	from .engagement_async_operations import EngagementAsyncOperationsRequest
	from .communities import CommunitiesRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.employee_experience import EmployeeExperience
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class EmployeeExperienceRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/employeeExperience"
		self.path_parameters: dict[str, Any] = path_parameters

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

	@property
	def learning_providers(self,
	) -> LearningProvidersRequest:
		from .learning_providers import LearningProvidersRequest
		return LearningProvidersRequest(self.request_adapter, self.path_parameters)

