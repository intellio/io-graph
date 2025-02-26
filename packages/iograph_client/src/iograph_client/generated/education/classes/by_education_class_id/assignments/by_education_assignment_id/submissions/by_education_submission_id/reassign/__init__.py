# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.education_submission import EducationSubmission
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ReassignRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}/reassign"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationSubmission:
		"""
		Invoke action reassign
		Reassign the submission to the student with feedback for review. Only teachers can perform this action.  Include the Prefer: include-unknown-enum-members header when you call this method; otherwise, a reassigned submission is treated as a returned submission. This means that the reassigned status is mapped to the returned status, and reassignedDateTime and reassignedBy properties are mapped to returnedDateTime and returnedBy respectively. If the header Prefer: include-unknown-enum-members is provided, a reassigned submission retains the reassigned status. For details, see the examples section.
		Find more info here: https://learn.microsoft.com/graph/api/educationsubmission-reassign?view=graph-rest-1.0
		"""
		tags = ['education.educationClass']

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


