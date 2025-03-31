# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.beta.education_submission import EducationSubmission
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ReassignRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/users/{educationUser%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}/reassign", path_parameters)

	async def post(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationSubmission:
		"""
		Invoke action reassign
		Reassign the submission to the student with feedback for review. Only teachers can perform this action.  Include the Prefer: include-unknown-enum-members header when you call this method; otherwise, a reassigned submission will be treated as a returned submission. This means that the reassigned status will be mapped to the returned status, and reassignedDateTime and reassignedBy properties will be mapped to returnedDateTime and returnedBy respectively. If the header Prefer: include-unknown-enum-members is provided, a reassigned submission retains the reassigned status. For details, see the examples section.
		Find more info here: https://learn.microsoft.com/graph/api/educationsubmission-reassign?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EducationSubmission, error_mapping)


	def with_url(self, raw_url: str) -> ReassignRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ReassignRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ReassignRequest(self.request_adapter, self.path_parameters)

