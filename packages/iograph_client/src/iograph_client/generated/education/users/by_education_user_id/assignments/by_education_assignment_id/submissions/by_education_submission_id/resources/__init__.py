# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_education_submission_resource_id import ByEducationSubmissionResourceIdRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.education_submission_resource_collection_response import EducationSubmissionResourceCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.education_submission_resource import EducationSubmissionResource


class ResourcesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/education/users/{educationUser%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}/resources"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationSubmissionResourceCollectionResponse:
		"""
		Get resources from education
		
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
		return await self.request_adapter.send_async(request_info, EducationSubmissionResourceCollectionResponse, error_mapping)

	async def post(
		self,
		body: EducationSubmissionResource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationSubmissionResource:
		"""
		Create new navigation property to resources for education
		
		"""
		tags = ['education.educationUser']

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
		return await self.request_adapter.send_async(request_info, EducationSubmissionResource, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_education_submission_resource_id(self,
		educationUser_id: str,
		educationAssignment_id: str,
		educationSubmission_id: str,
		educationSubmissionResource_id: str,
	) -> ByEducationSubmissionResourceIdRequest:
		if educationUser_id is None:
			raise TypeError("educationUser_id cannot be null.")
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")
		if educationSubmissionResource_id is None:
			raise TypeError("educationSubmissionResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationUser%2Did"] =  educationUser_id
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id
		path_parameters["educationSubmissionResource%2Did"] =  educationSubmissionResource_id

		from .by_education_submission_resource_id import ByEducationSubmissionResourceIdRequest
		return ByEducationSubmissionResourceIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

