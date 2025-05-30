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
	from .count import CountRequest
	from .by_on_premises_agent_id import ByOnPremisesAgentIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.on_premises_agent import OnPremisesAgent
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.on_premises_agent_collection_response import OnPremisesAgentCollectionResponse


class AgentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}/agentGroups/{onPremisesAgentGroup%2Did}/agents", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnPremisesAgentCollectionResponse:
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
		return await self.request_adapter.send_async(request_info, OnPremisesAgentCollectionResponse, error_mapping)

	async def post(
		self,
		body: OnPremisesAgent,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnPremisesAgent:
		"""
		Create new navigation property to agents for onPremisesPublishingProfiles
		
		"""
		tags = ['onPremisesPublishingProfiles.onPremisesAgentGroup']

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
		return await self.request_adapter.send_async(request_info, OnPremisesAgent, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AgentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AgentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AgentsRequest(self.request_adapter, self.path_parameters)

	def by_on_premises_agent_id(self,
		onPremisesPublishingProfile_id: str,
		onPremisesAgentGroup_id: str,
		onPremisesAgent_id: str,
	) -> ByOnPremisesAgentIdRequest:
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

		from .by_on_premises_agent_id import ByOnPremisesAgentIdRequest
		return ByOnPremisesAgentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		onPremisesPublishingProfile_id: str,
		onPremisesAgentGroup_id: str,
	) -> CountRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")
		if onPremisesAgentGroup_id is None:
			raise TypeError("onPremisesAgentGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id
		path_parameters["onPremisesAgentGroup%2Did"] =  onPremisesAgentGroup_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

