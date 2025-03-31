# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_education_outcome_id import ByEducationOutcomeIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.education_outcome import EducationOutcome
from iograph_models.beta.education_outcome_collection_response import EducationOutcomeCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class OutcomesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/education/me/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}/outcomes", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EducationOutcomeCollectionResponse:
		"""
		Get outcomes from education
		
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
		return await self.request_adapter.send_async(request_info, EducationOutcomeCollectionResponse, error_mapping)

	async def post(
		self,
		body: EducationOutcome,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EducationOutcome:
		"""
		Create new navigation property to outcomes for education
		
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
		educationAssignment_id: str,
		educationSubmission_id: str,
		educationOutcome_id: str,
	) -> ByEducationOutcomeIdRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")
		if educationOutcome_id is None:
			raise TypeError("educationOutcome_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id
		path_parameters["educationOutcome%2Did"] =  educationOutcome_id

		from .by_education_outcome_id import ByEducationOutcomeIdRequest
		return ByEducationOutcomeIdRequest(self.request_adapter, path_parameters)

	def count(self,
		educationAssignment_id: str,
		educationSubmission_id: str,
	) -> CountRequest:
		if educationAssignment_id is None:
			raise TypeError("educationAssignment_id cannot be null.")
		if educationSubmission_id is None:
			raise TypeError("educationSubmission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["educationAssignment%2Did"] =  educationAssignment_id
		path_parameters["educationSubmission%2Did"] =  educationSubmission_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

