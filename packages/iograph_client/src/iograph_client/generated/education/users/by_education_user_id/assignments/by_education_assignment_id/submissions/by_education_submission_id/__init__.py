# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .submitted_resources import SubmittedResourcesRequest
	from .resources import ResourcesRequest
	from .outcomes import OutcomesRequest
	from .unsubmit import UnsubmitRequest
	from .submit import SubmitRequest
	from .set_up_resources_folder import SetUpResourcesFolderRequest
	from .return import ReturnRequest
	from .reassign import ReassignRequest
	from .excuse import ExcuseRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.education_submission import EducationSubmission
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByEducationSubmissionIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/education/users/{educationUser%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationSubmission:
		"""
		Get submissions from education
		Once published, there's a submission object for each student representing their work and grade. Read-only. Nullable.
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
		return await self.request_adapter.send_async(request_info, EducationSubmission, error_mapping)

	async def patch(
		self,
		body: EducationSubmission,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationSubmission:
		"""
		Update the navigation property submissions in education
		
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
		return await self.request_adapter.send_async(request_info, EducationSubmission, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property submissions for education
		
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



	@property
	def excuse(self,
	) -> ExcuseRequest:
		from .excuse import ExcuseRequest
		return ExcuseRequest(self.request_adapter, self.path_parameters)

	@property
	def reassign(self,
	) -> ReassignRequest:
		from .reassign import ReassignRequest
		return ReassignRequest(self.request_adapter, self.path_parameters)

	@property
	def return(self,
	) -> ReturnRequest:
		from .return import ReturnRequest
		return ReturnRequest(self.request_adapter, self.path_parameters)

	@property
	def set_up_resources_folder(self,
	) -> SetUpResourcesFolderRequest:
		from .set_up_resources_folder import SetUpResourcesFolderRequest
		return SetUpResourcesFolderRequest(self.request_adapter, self.path_parameters)

	@property
	def submit(self,
	) -> SubmitRequest:
		from .submit import SubmitRequest
		return SubmitRequest(self.request_adapter, self.path_parameters)

	@property
	def unsubmit(self,
	) -> UnsubmitRequest:
		from .unsubmit import UnsubmitRequest
		return UnsubmitRequest(self.request_adapter, self.path_parameters)

	@property
	def outcomes(self,
	) -> OutcomesRequest:
		from .outcomes import OutcomesRequest
		return OutcomesRequest(self.request_adapter, self.path_parameters)

	@property
	def resources(self,
	) -> ResourcesRequest:
		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def submitted_resources(self,
	) -> SubmittedResourcesRequest:
		from .submitted_resources import SubmittedResourcesRequest
		return SubmittedResourcesRequest(self.request_adapter, self.path_parameters)

