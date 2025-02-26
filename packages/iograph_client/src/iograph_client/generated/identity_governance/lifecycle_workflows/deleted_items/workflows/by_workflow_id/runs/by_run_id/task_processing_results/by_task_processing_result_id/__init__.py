# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .task import TaskRequest
	from .subject import SubjectRequest
	from .identity_governance_resume import IdentityGovernanceResumeRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.identity_governance_task_processing_result import IdentityGovernanceTaskProcessingResult


class ByTaskProcessingResultIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}/runs/{run%2Did}/taskProcessingResults/{taskProcessingResult%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceTaskProcessingResult:
		"""
		Get taskProcessingResults from identityGovernance
		The related taskProcessingResults.
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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceTaskProcessingResult, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	@property
	def identity_governance_resume(self,
	) -> IdentityGovernanceResumeRequest:
		from .identity_governance_resume import IdentityGovernanceResumeRequest
		return IdentityGovernanceResumeRequest(self.request_adapter, self.path_parameters)

	@property
	def subject(self,
	) -> SubjectRequest:
		from .subject import SubjectRequest
		return SubjectRequest(self.request_adapter, self.path_parameters)

	@property
	def task(self,
	) -> TaskRequest:
		from .task import TaskRequest
		return TaskRequest(self.request_adapter, self.path_parameters)

