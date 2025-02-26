# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_teamwork_tag_member_id import ByTeamworkTagMemberIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.teamwork_tag_member import TeamworkTagMember
from iograph_models.models.teamwork_tag_member_collection_response import TeamworkTagMemberCollectionResponse


class MembersRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/teams/{team%2Did}/tags/{teamworkTag%2Did}/members"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TeamworkTagMemberCollectionResponse:
		"""
		List members in a teamworkTag
		Get a list of the members of a standard tag in a team and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/teamworktagmember-list?view=graph-rest-1.0
		"""
		tags = ['teams.teamworkTag']

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
		return await self.request_adapter.send_async(request_info, TeamworkTagMemberCollectionResponse, error_mapping)

	async def post(
		self,
		body: TeamworkTagMember,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TeamworkTagMember:
		"""
		Create teamworkTagMember
		Create a new teamworkTagMember object in a team.
		Find more info here: https://learn.microsoft.com/graph/api/teamworktagmember-post?view=graph-rest-1.0
		"""
		tags = ['teams.teamworkTag']

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
		return await self.request_adapter.send_async(request_info, TeamworkTagMember, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_teamwork_tag_member_id(self,
		team_id: str,
		teamworkTag_id: str,
		teamworkTagMember_id: str,
	) -> ByTeamworkTagMemberIdRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if teamworkTag_id is None:
			raise TypeError("teamworkTag_id cannot be null.")
		if teamworkTagMember_id is None:
			raise TypeError("teamworkTagMember_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id
		path_parameters["teamworkTag%2Did"] =  teamworkTag_id
		path_parameters["teamworkTagMember%2Did"] =  teamworkTagMember_id

		from .by_teamwork_tag_member_id import ByTeamworkTagMemberIdRequest
		return ByTeamworkTagMemberIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

