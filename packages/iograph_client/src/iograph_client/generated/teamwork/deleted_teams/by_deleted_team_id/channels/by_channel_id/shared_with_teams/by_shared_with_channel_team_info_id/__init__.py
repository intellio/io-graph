# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .team import TeamRequest
	from .allowed_members import AllowedMembersRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.shared_with_channel_team_info import SharedWithChannelTeamInfo
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class BySharedWithChannelTeamInfoIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamwork/deletedTeams/{deletedTeam%2Did}/channels/{channel%2Did}/sharedWithTeams/{sharedWithChannelTeamInfo%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SharedWithChannelTeamInfo:
		"""
		Get sharedWithTeams from teamwork
		A collection of teams with which a channel is shared.
		"""
		tags = ['teamwork.deletedTeam']

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
		tags = ['teamwork.deletedTeam']

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
		tags = ['teamwork.deletedTeam']
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

	@property
	def allowed_members(self,
	) -> AllowedMembersRequest:
		from .allowed_members import AllowedMembersRequest
		return AllowedMembersRequest(self.request_adapter, self.path_parameters)

	@property
	def team(self,
	) -> TeamRequest:
		from .team import TeamRequest
		return TeamRequest(self.request_adapter, self.path_parameters)

