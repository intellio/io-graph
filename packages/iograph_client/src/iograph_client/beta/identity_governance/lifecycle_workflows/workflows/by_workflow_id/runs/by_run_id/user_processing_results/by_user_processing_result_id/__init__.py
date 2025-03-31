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
	from .task_processing_results import TaskProcessingResultsRequest
	from .subject import SubjectRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.beta.identity_governance_user_processing_result import IdentityGovernanceUserProcessingResult
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserProcessingResultIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}/runs/{run%2Did}/userProcessingResults/{userProcessingResult%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceUserProcessingResult:
		"""
		Get userProcessingResult
		Get the user processing result of a user processing result of a run.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-userprocessingresult-get?view=graph-rest-beta
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']

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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceUserProcessingResult, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByUserProcessingResultIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserProcessingResultIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserProcessingResultIdRequest(self.request_adapter, self.path_parameters)

	def subject(self,
		workflow_id: str,
		run_id: str,
		userProcessingResult_id: str,
	) -> SubjectRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")
		if run_id is None:
			raise TypeError("run_id cannot be null.")
		if userProcessingResult_id is None:
			raise TypeError("userProcessingResult_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id
		path_parameters["run%2Did"] =  run_id
		path_parameters["userProcessingResult%2Did"] =  userProcessingResult_id

		from .subject import SubjectRequest
		return SubjectRequest(self.request_adapter, path_parameters)

	def task_processing_results(self,
		workflow_id: str,
		run_id: str,
		userProcessingResult_id: str,
	) -> TaskProcessingResultsRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")
		if run_id is None:
			raise TypeError("run_id cannot be null.")
		if userProcessingResult_id is None:
			raise TypeError("userProcessingResult_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id
		path_parameters["run%2Did"] =  run_id
		path_parameters["userProcessingResult%2Did"] =  userProcessingResult_id

		from .task_processing_results import TaskProcessingResultsRequest
		return TaskProcessingResultsRequest(self.request_adapter, path_parameters)

