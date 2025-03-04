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
	from .count import CountRequest
	from .by_shared_with_channel_team_info_id import BySharedWithChannelTeamInfoIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.shared_with_channel_team_info import SharedWithChannelTeamInfo
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.shared_with_channel_team_info_collection_response import SharedWithChannelTeamInfoCollectionResponse


class SharedWithTeamsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamwork/deletedTeams/{deletedTeam%2Did}/channels/{channel%2Did}/sharedWithTeams", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SharedWithChannelTeamInfoCollectionResponse:
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
		return await self.request_adapter.send_async(request_info, SharedWithChannelTeamInfoCollectionResponse, error_mapping)

	async def post(
		self,
		body: SharedWithChannelTeamInfo,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SharedWithChannelTeamInfo:
		"""
		Create new navigation property to sharedWithTeams for teamwork
		
		"""
		tags = ['teamwork.deletedTeam']

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
		return await self.request_adapter.send_async(request_info, SharedWithChannelTeamInfo, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SharedWithTeamsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SharedWithTeamsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SharedWithTeamsRequest(self.request_adapter, self.path_parameters)

	def by_shared_with_channel_team_info_id(self,
		deletedTeam_id: str,
		channel_id: str,
		sharedWithChannelTeamInfo_id: str,
	) -> BySharedWithChannelTeamInfoIdRequest:
		if deletedTeam_id is None:
			raise TypeError("deletedTeam_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")
		if sharedWithChannelTeamInfo_id is None:
			raise TypeError("sharedWithChannelTeamInfo_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deletedTeam%2Did"] =  deletedTeam_id
		path_parameters["channel%2Did"] =  channel_id
		path_parameters["sharedWithChannelTeamInfo%2Did"] =  sharedWithChannelTeamInfo_id

		from .by_shared_with_channel_team_info_id import BySharedWithChannelTeamInfoIdRequest
		return BySharedWithChannelTeamInfoIdRequest(self.request_adapter, path_parameters)

	def count(self,
		deletedTeam_id: str,
		channel_id: str,
	) -> CountRequest:
		if deletedTeam_id is None:
			raise TypeError("deletedTeam_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deletedTeam%2Did"] =  deletedTeam_id
		path_parameters["channel%2Did"] =  channel_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

