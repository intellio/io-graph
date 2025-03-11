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
	from .agent_groups import AgentGroupsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.on_premises_agent import OnPremisesAgent
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByOnPremisesAgentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}/agentGroups/{onPremisesAgentGroup%2Did}/agents/{onPremisesAgent%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnPremisesAgent:
		"""
		Get agents from onPremisesPublishingProfiles
		List of onPremisesAgent that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
		"""
		tags = ['onPremisesPublishingProfiles.onPremisesAgentGroup']

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
		return await self.request_adapter.send_async(request_info, OnPremisesAgent, error_mapping)

	async def patch(
		self,
		body: OnPremisesAgent,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnPremisesAgent:
		"""
		Update the navigation property agents in onPremisesPublishingProfiles
		
		"""
		tags = ['onPremisesPublishingProfiles.onPremisesAgentGroup']

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
		return await self.request_adapter.send_async(request_info, OnPremisesAgent, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property agents for onPremisesPublishingProfiles
		
		"""
		tags = ['onPremisesPublishingProfiles.onPremisesAgentGroup']
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



	def with_url(self, raw_url: str) -> ByOnPremisesAgentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOnPremisesAgentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOnPremisesAgentIdRequest(self.request_adapter, self.path_parameters)

	def agent_groups(self,
		onPremisesPublishingProfile_id: str,
		onPremisesAgentGroup_id: str,
		onPremisesAgent_id: str,
	) -> AgentGroupsRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")
		if onPremisesAgentGroup_id is None:
			raise TypeError("onPremisesAgentGroup_id cannot be null.")
		if onPremisesAgent_id is None:
			raise TypeError("onPremisesAgent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id
		path_parameters["onPremisesAgentGroup%2Did"] =  onPremisesAgentGroup_id
		path_parameters["onPremisesAgent%2Did"] =  onPremisesAgent_id

		from .agent_groups import AgentGroupsRequest
		return AgentGroupsRequest(self.request_adapter, path_parameters)

