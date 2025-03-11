# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .team import TeamRequest
	from .allowed_members import AllowedMembersRequest
	from ............request_adapter import HttpxRequestAdapter
from iograph_models.beta.shared_with_channel_team_info import SharedWithChannelTeamInfo
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class BySharedWithChannelTeamInfoIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamwork/teamTemplates/{teamTemplate%2Did}/definitions/{teamTemplateDefinition%2Did}/teamDefinition/channels/{channel%2Did}/sharedWithTeams/{sharedWithChannelTeamInfo%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SharedWithChannelTeamInfo:
		"""
		Get sharedWithTeams from teamwork
		A collection of teams with which a channel is shared.
		"""
		tags = ['teamwork.teamTemplate']

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
		return await self.request_adapter.send_async(request_info, SharedWithChannelTeamInfo, error_mapping)

	async def patch(
		self,
		body: SharedWithChannelTeamInfo,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SharedWithChannelTeamInfo:
		"""
		Update the navigation property sharedWithTeams in teamwork
		
		"""
		tags = ['teamwork.teamTemplate']

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
		return await self.request_adapter.send_async(request_info, SharedWithChannelTeamInfo, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property sharedWithTeams for teamwork
		
		"""
		tags = ['teamwork.teamTemplate']
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



	def with_url(self, raw_url: str) -> BySharedWithChannelTeamInfoIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySharedWithChannelTeamInfoIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySharedWithChannelTeamInfoIdRequest(self.request_adapter, self.path_parameters)

	def allowed_members(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
		channel_id: str,
		sharedWithChannelTeamInfo_id: str,
	) -> AllowedMembersRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")
		if sharedWithChannelTeamInfo_id is None:
			raise TypeError("sharedWithChannelTeamInfo_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id
		path_parameters["sharedWithChannelTeamInfo%2Did"] =  sharedWithChannelTeamInfo_id

		from .allowed_members import AllowedMembersRequest
		return AllowedMembersRequest(self.request_adapter, path_parameters)

	def team(self,
		teamTemplate_id: str,
		teamTemplateDefinition_id: str,
		channel_id: str,
		sharedWithChannelTeamInfo_id: str,
	) -> TeamRequest:
		if teamTemplate_id is None:
			raise TypeError("teamTemplate_id cannot be null.")
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")
		if sharedWithChannelTeamInfo_id is None:
			raise TypeError("sharedWithChannelTeamInfo_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplate%2Did"] =  teamTemplate_id
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id
		path_parameters["sharedWithChannelTeamInfo%2Did"] =  sharedWithChannelTeamInfo_id

		from .team import TeamRequest
		return TeamRequest(self.request_adapter, path_parameters)

