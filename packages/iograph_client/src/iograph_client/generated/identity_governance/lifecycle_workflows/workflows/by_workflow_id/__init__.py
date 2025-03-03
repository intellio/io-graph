# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .versions import VersionsRequest
	from .user_processing_results import UserProcessingResultsRequest
	from .tasks import TasksRequest
	from .task_reports import TaskReportsRequest
	from .runs import RunsRequest
	from .identity_governance_restore import IdentityGovernanceRestoreRequest
	from .identity_governance_create_new_version import IdentityGovernanceCreateNewVersionRequest
	from .identity_governance_activate import IdentityGovernanceActivateRequest
	from .last_modified_by import LastModifiedByRequest
	from .execution_scope import ExecutionScopeRequest
	from .created_by import CreatedByRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.identity_governance_workflow import IdentityGovernanceWorkflow
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByWorkflowIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceWorkflow:
		"""
		Get workflow
		Read the properties and relationships of a workflow object.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-workflow-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceWorkflow, error_mapping)

	async def patch(
		self,
		body: IdentityGovernanceWorkflow,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityGovernanceWorkflow:
		"""
		Update workflow
		Update the properties of a workflow object. Only the properties listed in the request body table can be updated. To update any other workflow properties, see workflow: createNewVersion.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-workflow-update?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']

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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceWorkflow, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete workflow
		Delete a workflow object and its associated tasks, taskProcessingResults and versions. You can restore a deleted workflow and its associated objects within 30 days of deletion.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-workflow-delete?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.lifecycleWorkflowsContainer']
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



	def with_url(self, raw_url: str) -> ByWorkflowIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWorkflowIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWorkflowIdRequest(self.request_adapter, self.path_parameters)

	@property
	def created_by(self,
	) -> CreatedByRequest:
		from .created_by import CreatedByRequest
		return CreatedByRequest(self.request_adapter, self.path_parameters)

	@property
	def execution_scope(self,
	) -> ExecutionScopeRequest:
		from .execution_scope import ExecutionScopeRequest
		return ExecutionScopeRequest(self.request_adapter, self.path_parameters)

	@property
	def last_modified_by(self,
	) -> LastModifiedByRequest:
		from .last_modified_by import LastModifiedByRequest
		return LastModifiedByRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_governance_activate(self,
	) -> IdentityGovernanceActivateRequest:
		from .identity_governance_activate import IdentityGovernanceActivateRequest
		return IdentityGovernanceActivateRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_governance_create_new_version(self,
	) -> IdentityGovernanceCreateNewVersionRequest:
		from .identity_governance_create_new_version import IdentityGovernanceCreateNewVersionRequest
		return IdentityGovernanceCreateNewVersionRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_governance_restore(self,
	) -> IdentityGovernanceRestoreRequest:
		from .identity_governance_restore import IdentityGovernanceRestoreRequest
		return IdentityGovernanceRestoreRequest(self.request_adapter, self.path_parameters)

	@property
	def runs(self,
	) -> RunsRequest:
		from .runs import RunsRequest
		return RunsRequest(self.request_adapter, self.path_parameters)

	@property
	def task_reports(self,
	) -> TaskReportsRequest:
		from .task_reports import TaskReportsRequest
		return TaskReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def tasks(self,
	) -> TasksRequest:
		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, self.path_parameters)

	@property
	def user_processing_results(self,
	) -> UserProcessingResultsRequest:
		from .user_processing_results import UserProcessingResultsRequest
		return UserProcessingResultsRequest(self.request_adapter, self.path_parameters)

	@property
	def versions(self,
	) -> VersionsRequest:
		from .versions import VersionsRequest
		return VersionsRequest(self.request_adapter, self.path_parameters)

