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
	from .submissions import SubmissionsRequest
	from .rubric import RubricRequest
	from .resources import ResourcesRequest
	from .set_up_resources_folder import SetUpResourcesFolderRequest
	from .set_up_feedback_resources_folder import SetUpFeedbackResourcesFolderRequest
	from .publish import PublishRequest
	from .deactivate import DeactivateRequest
	from .activate import ActivateRequest
	from .grading_category import GradingCategoryRequest
	from .categories import CategoriesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.education_assignment import EducationAssignment
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByEducationAssignmentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/me/assignments/{educationAssignment%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationAssignment:
		"""
		Get assignments from education
		Assignments belonging to the user.
		"""
		tags = ['education.educationUser']

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
		return await self.request_adapter.send_async(request_info, EducationAssignment, error_mapping)

	async def patch(
		self,
		body: EducationAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationAssignment:
		"""
		Update the navigation property assignments in education
		
		"""
		tags = ['education.educationUser']

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
		return await self.request_adapter.send_async(request_info, EducationAssignment, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property assignments for education
		
		"""
		tags = ['education.educationUser']
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



	def with_url(self, raw_url: str) -> ByEducationAssignmentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEducationAssignmentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEducationAssignmentIdRequest(self.request_adapter, self.path_parameters)

	def categories(self,
		educationAssignment_id: str,
	) -> CategoriesRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .categories import CategoriesRequest
		return CategoriesRequest(self.request_adapter, path_parameters)

	def grading_category(self,
		educationAssignment_id: str,
	) -> GradingCategoryRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .grading_category import GradingCategoryRequest
		return GradingCategoryRequest(self.request_adapter, path_parameters)

	def activate(self,
		educationAssignment_id: str,
	) -> ActivateRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .activate import ActivateRequest
		return ActivateRequest(self.request_adapter, path_parameters)

	def deactivate(self,
		educationAssignment_id: str,
	) -> DeactivateRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .deactivate import DeactivateRequest
		return DeactivateRequest(self.request_adapter, path_parameters)

	def publish(self,
		educationAssignment_id: str,
	) -> PublishRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .publish import PublishRequest
		return PublishRequest(self.request_adapter, path_parameters)

	def set_up_feedback_resources_folder(self,
		educationAssignment_id: str,
	) -> SetUpFeedbackResourcesFolderRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .set_up_feedback_resources_folder import SetUpFeedbackResourcesFolderRequest
		return SetUpFeedbackResourcesFolderRequest(self.request_adapter, path_parameters)

	def set_up_resources_folder(self,
		educationAssignment_id: str,
	) -> SetUpResourcesFolderRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .set_up_resources_folder import SetUpResourcesFolderRequest
		return SetUpResourcesFolderRequest(self.request_adapter, path_parameters)

	def resources(self,
		educationAssignment_id: str,
	) -> ResourcesRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, path_parameters)

	def rubric(self,
		educationAssignment_id: str,
	) -> RubricRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .rubric import RubricRequest
		return RubricRequest(self.request_adapter, path_parameters)

	def submissions(self,
		educationAssignment_id: str,
	) -> SubmissionsRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .submissions import SubmissionsRequest
		return SubmissionsRequest(self.request_adapter, path_parameters)

