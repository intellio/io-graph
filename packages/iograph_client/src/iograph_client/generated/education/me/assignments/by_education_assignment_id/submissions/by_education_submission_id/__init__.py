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
	from .submitted_resources import SubmittedResourcesRequest
	from .resources import ResourcesRequest
	from .outcomes import OutcomesRequest
	from .unsubmit import UnsubmitRequest
	from .submit import SubmitRequest
	from .set_up_resources_folder import SetUpResourcesFolderRequest
	from .return import ReturnRequest
	from .reassign import ReassignRequest
	from .excuse import ExcuseRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.education_submission import EducationSubmission


class ByEducationSubmissionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/me/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}", path_parameters)

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



	def with_url(self, raw_url: str) -> ByEducationSubmissionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEducationSubmissionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEducationSubmissionIdRequest(self.request_adapter, self.path_parameters)

	def excuse(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> ExcuseRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .excuse import ExcuseRequest
		return ExcuseRequest(self.request_adapter, path_parameters)

	def reassign(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> ReassignRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .reassign import ReassignRequest
		return ReassignRequest(self.request_adapter, path_parameters)

	def return(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> ReturnRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .return import ReturnRequest
		return ReturnRequest(self.request_adapter, path_parameters)

	def set_up_resources_folder(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> SetUpResourcesFolderRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .set_up_resources_folder import SetUpResourcesFolderRequest
		return SetUpResourcesFolderRequest(self.request_adapter, path_parameters)

	def submit(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> SubmitRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .submit import SubmitRequest
		return SubmitRequest(self.request_adapter, path_parameters)

	def unsubmit(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> UnsubmitRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .unsubmit import UnsubmitRequest
		return UnsubmitRequest(self.request_adapter, path_parameters)

	def outcomes(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> OutcomesRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .outcomes import OutcomesRequest
		return OutcomesRequest(self.request_adapter, path_parameters)

	def resources(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> ResourcesRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, path_parameters)

	def submitted_resources(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> SubmittedResourcesRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .submitted_resources import SubmittedResourcesRequest
		return SubmittedResourcesRequest(self.request_adapter, path_parameters)

