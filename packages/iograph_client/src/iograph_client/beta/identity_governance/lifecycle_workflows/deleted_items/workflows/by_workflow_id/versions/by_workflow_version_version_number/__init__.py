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
	from .tasks import TasksRequest
	from .last_modified_by import LastModifiedByRequest
	from .created_by import CreatedByRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.identity_governance_workflow_version import IdentityGovernanceWorkflowVersion


class ByWorkflowVersionVersionNumberRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}/versions/{workflowVersion%2DversionNumber}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceWorkflowVersion:
		"""
		Get versions from identityGovernance
		The workflow versions that are available.
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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceWorkflowVersion, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByWorkflowVersionVersionNumberRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWorkflowVersionVersionNumberRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWorkflowVersionVersionNumberRequest(self.request_adapter, self.path_parameters)

	def created_by(self,
		workflow_id: str,
		workflowVersion_versionNumber: int,
	) -> CreatedByRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")
		if workflowVersion_versionNumber is None:
			raise TypeError("workflowVersion_versionNumber cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id
		path_parameters["workflowVersion%2DversionNumber"] =  workflowVersion_versionNumber

		from .created_by import CreatedByRequest
		return CreatedByRequest(self.request_adapter, path_parameters)

	def last_modified_by(self,
		workflow_id: str,
		workflowVersion_versionNumber: int,
	) -> LastModifiedByRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")
		if workflowVersion_versionNumber is None:
			raise TypeError("workflowVersion_versionNumber cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id
		path_parameters["workflowVersion%2DversionNumber"] =  workflowVersion_versionNumber

		from .last_modified_by import LastModifiedByRequest
		return LastModifiedByRequest(self.request_adapter, path_parameters)

	def tasks(self,
		workflow_id: str,
		workflowVersion_versionNumber: int,
	) -> TasksRequest:
		if workflow_id is None:
			raise TypeError("workflow_id cannot be null.")
		if workflowVersion_versionNumber is None:
			raise TypeError("workflowVersion_versionNumber cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["workflow%2Did"] =  workflow_id
		path_parameters["workflowVersion%2DversionNumber"] =  workflowVersion_versionNumber

		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, path_parameters)

