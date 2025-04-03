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
	from .published_resources import PublishedResourcesRequest
	from .connectors import ConnectorsRequest
	from .connector_groups import ConnectorGroupsRequest
	from .application_segments import ApplicationSegmentsRequest
	from .agents import AgentsRequest
	from .agent_groups import AgentGroupsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.on_premises_publishing_profile import OnPremisesPublishingProfile


class ByOnPremisesPublishingProfileIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/onPremisesPublishingProfiles/{onPremisesPublishingProfile%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnPremisesPublishingProfile:
		"""
		Get entity from onPremisesPublishingProfiles by key
		
		"""
		tags = ['onPremisesPublishingProfiles.onPremisesPublishingProfile']

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
		return await self.request_adapter.send_async(request_info, OnPremisesPublishingProfile, error_mapping)

	async def patch(
		self,
		body: OnPremisesPublishingProfile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnPremisesPublishingProfile:
		"""
		Update entity in onPremisesPublishingProfiles
		
		"""
		tags = ['onPremisesPublishingProfiles.onPremisesPublishingProfile']

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
		return await self.request_adapter.send_async(request_info, OnPremisesPublishingProfile, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from onPremisesPublishingProfiles
		
		"""
		tags = ['onPremisesPublishingProfiles.onPremisesPublishingProfile']
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



	def with_url(self, raw_url: str) -> ByOnPremisesPublishingProfileIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOnPremisesPublishingProfileIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOnPremisesPublishingProfileIdRequest(self.request_adapter, self.path_parameters)

	def agent_groups(self,
		onPremisesPublishingProfile_id: str,
	) -> AgentGroupsRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id

		from .agent_groups import AgentGroupsRequest
		return AgentGroupsRequest(self.request_adapter, path_parameters)

	def agents(self,
		onPremisesPublishingProfile_id: str,
	) -> AgentsRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id

		from .agents import AgentsRequest
		return AgentsRequest(self.request_adapter, path_parameters)

	def application_segments(self,
		onPremisesPublishingProfile_id: str,
	) -> ApplicationSegmentsRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id

		from .application_segments import ApplicationSegmentsRequest
		return ApplicationSegmentsRequest(self.request_adapter, path_parameters)

	def connector_groups(self,
		onPremisesPublishingProfile_id: str,
	) -> ConnectorGroupsRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id

		from .connector_groups import ConnectorGroupsRequest
		return ConnectorGroupsRequest(self.request_adapter, path_parameters)

	def connectors(self,
		onPremisesPublishingProfile_id: str,
	) -> ConnectorsRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id

		from .connectors import ConnectorsRequest
		return ConnectorsRequest(self.request_adapter, path_parameters)

	def published_resources(self,
		onPremisesPublishingProfile_id: str,
	) -> PublishedResourcesRequest:
		if onPremisesPublishingProfile_id is None:
			raise TypeError("onPremisesPublishingProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onPremisesPublishingProfile%2Did"] =  onPremisesPublishingProfile_id

		from .published_resources import PublishedResourcesRequest
		return PublishedResourcesRequest(self.request_adapter, path_parameters)

