# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sensitivity_labels import SensitivityLabelsRequest
	from .sensitive_types import SensitiveTypesRequest
	from .classify_file import ClassifyFileRequest
	from .classify_exact_matches import ClassifyExactMatchesRequest
	from .jobs import JobsRequest
	from .exact_match_upload_agents import ExactMatchUploadAgentsRequest
	from .exact_match_data_stores import ExactMatchDataStoresRequest
	from .evaluate_label_jobs import EvaluateLabelJobsRequest
	from .evaluate_dlp_policies_jobs import EvaluateDlpPoliciesJobsRequest
	from .classify_text_jobs import ClassifyTextJobsRequest
	from .classify_file_jobs import ClassifyFileJobsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.data_classification_service import DataClassificationService
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DataClassificationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/dataClassification", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DataClassificationService:
		"""
		Get dataClassification
		
		"""
		tags = ['dataClassification.dataClassificationService']

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
		return await self.request_adapter.send_async(request_info, DataClassificationService, error_mapping)

	async def patch(
		self,
		body: DataClassificationService,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DataClassificationService:
		"""
		Update dataClassification
		
		"""
		tags = ['dataClassification.dataClassificationService']

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
		return await self.request_adapter.send_async(request_info, DataClassificationService, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DataClassificationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DataClassificationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DataClassificationRequest(self.request_adapter, self.path_parameters)

	@property
	def classify_file_jobs(self,
	) -> ClassifyFileJobsRequest:
		from .classify_file_jobs import ClassifyFileJobsRequest
		return ClassifyFileJobsRequest(self.request_adapter, self.path_parameters)

	@property
	def classify_text_jobs(self,
	) -> ClassifyTextJobsRequest:
		from .classify_text_jobs import ClassifyTextJobsRequest
		return ClassifyTextJobsRequest(self.request_adapter, self.path_parameters)

	@property
	def evaluate_dlp_policies_jobs(self,
	) -> EvaluateDlpPoliciesJobsRequest:
		from .evaluate_dlp_policies_jobs import EvaluateDlpPoliciesJobsRequest
		return EvaluateDlpPoliciesJobsRequest(self.request_adapter, self.path_parameters)

	@property
	def evaluate_label_jobs(self,
	) -> EvaluateLabelJobsRequest:
		from .evaluate_label_jobs import EvaluateLabelJobsRequest
		return EvaluateLabelJobsRequest(self.request_adapter, self.path_parameters)

	@property
	def exact_match_data_stores(self,
	) -> ExactMatchDataStoresRequest:
		from .exact_match_data_stores import ExactMatchDataStoresRequest
		return ExactMatchDataStoresRequest(self.request_adapter, self.path_parameters)

	@property
	def exact_match_upload_agents(self,
	) -> ExactMatchUploadAgentsRequest:
		from .exact_match_upload_agents import ExactMatchUploadAgentsRequest
		return ExactMatchUploadAgentsRequest(self.request_adapter, self.path_parameters)

	@property
	def jobs(self,
	) -> JobsRequest:
		from .jobs import JobsRequest
		return JobsRequest(self.request_adapter, self.path_parameters)

	@property
	def classify_exact_matches(self,
	) -> ClassifyExactMatchesRequest:
		from .classify_exact_matches import ClassifyExactMatchesRequest
		return ClassifyExactMatchesRequest(self.request_adapter, self.path_parameters)

	@property
	def classify_file(self,
	) -> ClassifyFileRequest:
		from .classify_file import ClassifyFileRequest
		return ClassifyFileRequest(self.request_adapter, self.path_parameters)

	@property
	def sensitive_types(self,
	) -> SensitiveTypesRequest:
		from .sensitive_types import SensitiveTypesRequest
		return SensitiveTypesRequest(self.request_adapter, self.path_parameters)

	@property
	def sensitivity_labels(self,
	) -> SensitivityLabelsRequest:
		from .sensitivity_labels import SensitivityLabelsRequest
		return SensitivityLabelsRequest(self.request_adapter, self.path_parameters)

