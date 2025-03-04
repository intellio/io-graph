# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .workflow_templates import WorkflowTemplatesRequest
	from .workflows import WorkflowsRequest
	from .task_definitions import TaskDefinitionsRequest
	from .settings import SettingsRequest
	from .insights import InsightsRequest
	from .deleted_items import DeletedItemsRequest
	from .custom_task_extensions import CustomTaskExtensionsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.identity_governance_lifecycle_workflows_container import IdentityGovernanceLifecycleWorkflowsContainer


class LifecycleWorkflowsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernanceLifecycleWorkflowsContainer:
		"""
		Get lifecycleWorkflows from identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceLifecycleWorkflowsContainer, error_mapping)

	async def patch(
		self,
		body: IdentityGovernanceLifecycleWorkflowsContainer,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityGovernanceLifecycleWorkflowsContainer:
		"""
		Update the navigation property lifecycleWorkflows in identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, IdentityGovernanceLifecycleWorkflowsContainer, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property lifecycleWorkflows for identityGovernance
		
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



	def with_url(self, raw_url: str) -> LifecycleWorkflowsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LifecycleWorkflowsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LifecycleWorkflowsRequest(self.request_adapter, self.path_parameters)

	@property
	def custom_task_extensions(self,
	) -> CustomTaskExtensionsRequest:
		from .custom_task_extensions import CustomTaskExtensionsRequest
		return CustomTaskExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def deleted_items(self,
	) -> DeletedItemsRequest:
		from .deleted_items import DeletedItemsRequest
		return DeletedItemsRequest(self.request_adapter, self.path_parameters)

	@property
	def insights(self,
	) -> InsightsRequest:
		from .insights import InsightsRequest
		return InsightsRequest(self.request_adapter, self.path_parameters)

	@property
	def settings(self,
	) -> SettingsRequest:
		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def task_definitions(self,
	) -> TaskDefinitionsRequest:
		from .task_definitions import TaskDefinitionsRequest
		return TaskDefinitionsRequest(self.request_adapter, self.path_parameters)

	@property
	def workflows(self,
	) -> WorkflowsRequest:
		from .workflows import WorkflowsRequest
		return WorkflowsRequest(self.request_adapter, self.path_parameters)

	@property
	def workflow_templates(self,
	) -> WorkflowTemplatesRequest:
		from .workflow_templates import WorkflowTemplatesRequest
		return WorkflowTemplatesRequest(self.request_adapter, self.path_parameters)

