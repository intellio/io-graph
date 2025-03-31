# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_education_outcome_id import ByEducationOutcomeIdRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.beta.education_outcome import EducationOutcome
from iograph_models.beta.education_outcome_collection_response import EducationOutcomeCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class OutcomesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}/outcomes", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationOutcomeCollectionResponse:
		"""
		List outcomes
		Retrieve a list of educationOutcome objects. There are four types of outcomes: educationPointsOutcome, educationFeedbackOutcome, educationRubricOutcome, and educationFeedbackResourceOutcome. Only teachers, students, and applications with application permissions can perform this operation. A submission for a credit assignment (one that has no point value and no rubric) has an educationFeedbackOutcome. (It might also return an educationPointsOutcome, but that outcome is ignored.) A submission for a points assignment (one that has a point value assigned) has both an educationFeedbackOutcome and an educationPointsOutcome. A submission for an assignment with an attached rubric, if the rubric is a credit rubric (no points), has an educationFeedbackOutcome and an educationRubricOutcome. (It might also return an educationPointsOutcome, but that outcome is ignored.) A submission for an assignment with an attached rubric, if the rubric is a points rubric, has an educationFeedbackOutcome, an educationPointsOutcome, and an educationRubricOutcome. A submission for a feedback resource has an educationFeedbackResourceOutcome. All outcome types have a regular and a published property appropriate to that type of outcome; for example, points and publishedPoints, feedback and publishedFeedback. The regular property is the most recent value updated by the teacher; the published property is the most recent value returned to the student.
		Find more info here: https://learn.microsoft.com/graph/api/educationsubmission-list-outcomes?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EducationOutcomeCollectionResponse, error_mapping)

	async def post(
		self,
		body: EducationOutcome,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationOutcome:
		"""
		Create educationFeedbackResourceOutcome
		Create a new feedback resource for a submission. Only a teacher can perform this operation. To create a new file-based resource, upload the file to the feedback resources folder associated with the assignment. If the file doesn't exist or is not in that folder, the POST request will fail.
		Find more info here: https://learn.microsoft.com/graph/api/educationfeedbackresourceoutcome-post-outcomes?view=graph-rest-beta
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
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, EducationOutcome, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> OutcomesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OutcomesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OutcomesRequest(self.request_adapter, self.path_parameters)

	def by_education_outcome_id(self,
		educationClass_id: str,
		educationAssignment_id: str,
		educationSubmission_id: str,
		educationOutcome_id: str,
	) -> ByEducationOutcomeIdRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")
		if educationOutcome_id is None:
			raise TypeError("educationOutcome_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id
		path_parameters["educationOutcome%2Did"] =  educationOutcome_id

		from .by_education_outcome_id import ByEducationOutcomeIdRequest
		return ByEducationOutcomeIdRequest(self.request_adapter, path_parameters)

	def count(self,
		educationClass_id: str,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> CountRequest:
		if educationClass_id is None:
			raise TypeError("educationClass_id cannot be null.")
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationClass%2Did"] =  educationClass_id
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

