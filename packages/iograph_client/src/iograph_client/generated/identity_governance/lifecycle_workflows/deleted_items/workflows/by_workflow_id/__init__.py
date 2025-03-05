# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
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
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.identity_governance_workflow import IdentityGovernanceWorkflow
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByWorkflowIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceWorkflow:
		"""
		Get deletedItemContainer (a deleted lifecycle workflow)
		Retrieve a deleted workflow object.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-deleteditemcontainer-get?view=graph-rest-1.0
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

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete deletedItemContainer (permanently delete a deleted lifecycle workflow)
		Delete a workflow object.
		Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-deleteditemcontainer-delete?view=graph-rest-1.0
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

	def created_by(self,
		workflow_id: str,
	) -> CreatedByRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .created_by import CreatedByRequest
		return CreatedByRequest(self.request_adapter, path_parameters)

	def execution_scope(self,
		workflow_id: str,
	) -> ExecutionScopeRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .execution_scope import ExecutionScopeRequest
		return ExecutionScopeRequest(self.request_adapter, path_parameters)

	def last_modified_by(self,
		workflow_id: str,
	) -> LastModifiedByRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .last_modified_by import LastModifiedByRequest
		return LastModifiedByRequest(self.request_adapter, path_parameters)

	def identity_governance_activate(self,
		workflow_id: str,
	) -> IdentityGovernanceActivateRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .identity_governance_activate import IdentityGovernanceActivateRequest
		return IdentityGovernanceActivateRequest(self.request_adapter, path_parameters)

	def identity_governance_create_new_version(self,
		workflow_id: str,
	) -> IdentityGovernanceCreateNewVersionRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .identity_governance_create_new_version import IdentityGovernanceCreateNewVersionRequest
		return IdentityGovernanceCreateNewVersionRequest(self.request_adapter, path_parameters)

	def identity_governance_restore(self,
		workflow_id: str,
	) -> IdentityGovernanceRestoreRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .identity_governance_restore import IdentityGovernanceRestoreRequest
		return IdentityGovernanceRestoreRequest(self.request_adapter, path_parameters)

	def runs(self,
		workflow_id: str,
	) -> RunsRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .runs import RunsRequest
		return RunsRequest(self.request_adapter, path_parameters)

	def task_reports(self,
		workflow_id: str,
	) -> TaskReportsRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .task_reports import TaskReportsRequest
		return TaskReportsRequest(self.request_adapter, path_parameters)

	def tasks(self,
		workflow_id: str,
	) -> TasksRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, path_parameters)

	def user_processing_results(self,
		workflow_id: str,
	) -> UserProcessingResultsRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .user_processing_results import UserProcessingResultsRequest
		return UserProcessingResultsRequest(self.request_adapter, path_parameters)

	def versions(self,
		workflow_id: str,
	) -> VersionsRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id

		from .versions import VersionsRequest
		return VersionsRequest(self.request_adapter, path_parameters)

