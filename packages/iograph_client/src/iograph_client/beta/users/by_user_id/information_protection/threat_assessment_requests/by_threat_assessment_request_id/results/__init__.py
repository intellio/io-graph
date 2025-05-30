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
	from .count import CountRequest
	from .by_threat_assessment_result_id import ByThreatAssessmentResultIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.threat_assessment_result_collection_response import ThreatAssessmentResultCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.threat_assessment_result import ThreatAssessmentResult


class ResultsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/informationProtection/threatAssessmentRequests/{threatAssessmentRequest%2Did}/results", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ThreatAssessmentResultCollectionResponse:
		"""
		Get results from users
		A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.
		"""
		tags = ['users.informationProtection']

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
		return await self.request_adapter.send_async(request_info, ThreatAssessmentResultCollectionResponse, error_mapping)

	async def post(
		self,
		body: ThreatAssessmentResult,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ThreatAssessmentResult:
		"""
		Create new navigation property to results for users
		
		"""
		tags = ['users.informationProtection']

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
		return await self.request_adapter.send_async(request_info, ThreatAssessmentResult, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ResultsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ResultsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ResultsRequest(self.request_adapter, self.path_parameters)

	def by_threat_assessment_result_id(self,
		user_id: str,
		threatAssessmentRequest_id: str,
		threatAssessmentResult_id: str,
	) -> ByThreatAssessmentResultIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if threatAssessmentRequest_id is None:
			raise TypeError("threatAssessmentRequest_id cannot be null.")
		if threatAssessmentResult_id is None:
			raise TypeError("threatAssessmentResult_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["threatAssessmentRequest%2Did"] =  threatAssessmentRequest_id
		path_parameters["threatAssessmentResult%2Did"] =  threatAssessmentResult_id

		from .by_threat_assessment_result_id import ByThreatAssessmentResultIdRequest
		return ByThreatAssessmentResultIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		threatAssessmentRequest_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if threatAssessmentRequest_id is None:
			raise TypeError("threatAssessmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["threatAssessmentRequest%2Did"] =  threatAssessmentRequest_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

