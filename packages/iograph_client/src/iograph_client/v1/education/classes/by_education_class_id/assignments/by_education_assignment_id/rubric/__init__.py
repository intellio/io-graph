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
	from .ref import RefRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.education_rubric import EducationRubric


class RubricRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/rubric", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationRubric:
		"""
		Get educationRubric attached to educationAssignment
		Get the educationRubric object attached to an educationAssignment, if one exists. Only teachers, students, and applications with application permissions can perform this operation.
		Find more info here: https://learn.microsoft.com/graph/api/educationassignment-get-rubric?view=graph-rest-1.0
		"""
		tags = ['education.educationClass']

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
		return await self.request_adapter.send_async(request_info, EducationRubric, error_mapping)

	async def patch(
		self,
		body: EducationRubric,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationRubric:
		"""
		Attach educationRubric to an assignment
		Attach an existing educationRubric object to an educationAssignment. Only teachers can perform this operation.
		Find more info here: https://learn.microsoft.com/graph/api/educationassignment-put-rubric?view=graph-rest-1.0
		"""
		tags = ['education.educationClass']

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
		return await self.request_adapter.send_async(request_info, EducationRubric, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete educationRubric from educationAssignment
		Remove an educationRubric from an educationAssignment. This method doesn't delete the rubric itself and can only be performed by teachers.
		Find more info here: https://learn.microsoft.com/graph/api/educationassignment-delete-rubric?view=graph-rest-1.0
		"""
		tags = ['education.educationClass']
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



	def with_url(self, raw_url: str) -> RubricRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RubricRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RubricRequest(self.request_adapter, self.path_parameters)

	def ref(self,
		educationClass_id: str,
		educationAssignment_id: str,
	) -> RefRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

