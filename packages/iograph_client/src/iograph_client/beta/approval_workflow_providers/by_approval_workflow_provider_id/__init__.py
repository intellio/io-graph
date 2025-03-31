# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .policy_templates import PolicyTemplatesRequest
	from .business_flows_with_requests_awaiting_my_decision import BusinessFlowsWithRequestsAwaitingMyDecisionRequest
	from .business_flows import BusinessFlowsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.approval_workflow_provider import ApprovalWorkflowProvider
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByApprovalWorkflowProviderIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/approvalWorkflowProviders/{approvalWorkflowProvider%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ApprovalWorkflowProvider:
		"""
		Get entity from approvalWorkflowProviders by key
		
		"""
		tags = ['approvalWorkflowProviders.approvalWorkflowProvider']

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
		return await self.request_adapter.send_async(request_info, ApprovalWorkflowProvider, error_mapping)

	async def patch(
		self,
		body: ApprovalWorkflowProvider,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ApprovalWorkflowProvider:
		"""
		Update entity in approvalWorkflowProviders
		
		"""
		tags = ['approvalWorkflowProviders.approvalWorkflowProvider']

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
		return await self.request_adapter.send_async(request_info, ApprovalWorkflowProvider, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from approvalWorkflowProviders
		
		"""
		tags = ['approvalWorkflowProviders.approvalWorkflowProvider']
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



	def with_url(self, raw_url: str) -> ByApprovalWorkflowProviderIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByApprovalWorkflowProviderIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByApprovalWorkflowProviderIdRequest(self.request_adapter, self.path_parameters)

	def business_flows(self,
		approvalWorkflowProvider_id: str,
	) -> BusinessFlowsRequest:
		if approvalWorkflowProvider_id is None:
			raise TypeError("approvalWorkflowProvider_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["approvalWorkflowProvider%2Did"] =  approvalWorkflowProvider_id

		from .business_flows import BusinessFlowsRequest
		return BusinessFlowsRequest(self.request_adapter, path_parameters)

	def business_flows_with_requests_awaiting_my_decision(self,
		approvalWorkflowProvider_id: str,
	) -> BusinessFlowsWithRequestsAwaitingMyDecisionRequest:
		if approvalWorkflowProvider_id is None:
			raise TypeError("approvalWorkflowProvider_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["approvalWorkflowProvider%2Did"] =  approvalWorkflowProvider_id

		from .business_flows_with_requests_awaiting_my_decision import BusinessFlowsWithRequestsAwaitingMyDecisionRequest
		return BusinessFlowsWithRequestsAwaitingMyDecisionRequest(self.request_adapter, path_parameters)

	def policy_templates(self,
		approvalWorkflowProvider_id: str,
	) -> PolicyTemplatesRequest:
		if approvalWorkflowProvider_id is None:
			raise TypeError("approvalWorkflowProvider_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["approvalWorkflowProvider%2Did"] =  approvalWorkflowProvider_id

		from .policy_templates import PolicyTemplatesRequest
		return PolicyTemplatesRequest(self.request_adapter, path_parameters)

