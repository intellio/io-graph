# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_planner_roster_member_id import ByPlannerRosterMemberIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.planner_roster_member_collection_response import PlannerRosterMemberCollectionResponse
from iograph_models.beta.planner_roster_member import PlannerRosterMember


class MembersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/planner/rosters/{plannerRoster%2Did}/members", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerRosterMemberCollectionResponse:
		"""
		List plannerRosterMembers
		Get the list of plannerRosterMembers from a plannerRoster.
		Find more info here: https://learn.microsoft.com/graph/api/plannerroster-list-members?view=graph-rest-beta
		"""
		tags = ['planner.plannerRoster']

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
		return await self.request_adapter.send_async(request_info, PlannerRosterMemberCollectionResponse, error_mapping)

	async def post(
		self,
		body: PlannerRosterMember,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PlannerRosterMember:
		"""
		Create plannerRosterMember
		Add a member to the plannerRoster object.
		Find more info here: https://learn.microsoft.com/graph/api/plannerroster-post-members?view=graph-rest-beta
		"""
		tags = ['planner.plannerRoster']

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
		return await self.request_adapter.send_async(request_info, PlannerRosterMember, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MembersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MembersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MembersRequest(self.request_adapter, self.path_parameters)

	def by_planner_roster_member_id(self,
		plannerRoster_id: str,
		plannerRosterMember_id: str,
	) -> ByPlannerRosterMemberIdRequest:
		if plannerRoster_id is None:
			raise TypeError("plannerRoster_id cannot be null.")
		if plannerRosterMember_id is None:
			raise TypeError("plannerRosterMember_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["plannerRoster%2Did"] =  plannerRoster_id
		path_parameters["plannerRosterMember%2Did"] =  plannerRosterMember_id

		from .by_planner_roster_member_id import ByPlannerRosterMemberIdRequest
		return ByPlannerRosterMemberIdRequest(self.request_adapter, path_parameters)

	def count(self,
		plannerRoster_id: str,
	) -> CountRequest:
		if plannerRoster_id is None:
			raise TypeError("plannerRoster_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["plannerRoster%2Did"] =  plannerRoster_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

