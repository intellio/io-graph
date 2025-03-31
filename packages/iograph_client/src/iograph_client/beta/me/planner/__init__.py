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
	from .tasks import TasksRequest
	from .roster_plans import RosterPlansRequest
	from .recent_plans import RecentPlansRequest
	from .plans import PlansRequest
	from .my_day_tasks import MyDayTasksRequest
	from .favorite_plans import FavoritePlansRequest
	from .all import AllRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.planner_user import PlannerUser
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class PlannerRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/planner", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerUser:
		"""
		Get plannerUser
		Retrieve the properties and relationships of a plannerUser object. The returned properties include the user's favorite plans and recently viewed plans. 
		Find more info here: https://learn.microsoft.com/graph/api/planneruser-get?view=graph-rest-beta
		"""
		tags = ['me.plannerUser']

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
		return await self.request_adapter.send_async(request_info, PlannerUser, error_mapping)

	async def patch(
		self,
		body: PlannerUser,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PlannerUser:
		"""
		Update plannerUser
		Update the properties of a plannerUser object. You can use this operation to add or remove plans from a user's favorite plans list, and to indicate which plans the user has recently viewed.
		Find more info here: https://learn.microsoft.com/graph/api/planneruser-update?view=graph-rest-beta
		"""
		tags = ['me.plannerUser']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag value.', 'required': True, 'schema': {'type': 'string'}}]

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
		return await self.request_adapter.send_async(request_info, PlannerUser, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property planner for me
		
		"""
		tags = ['me.plannerUser']
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



	def with_url(self, raw_url: str) -> PlannerRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PlannerRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PlannerRequest(self.request_adapter, self.path_parameters)

	@property
	def all(self,
	) -> AllRequest:
		from .all import AllRequest
		return AllRequest(self.request_adapter, self.path_parameters)

	@property
	def favorite_plans(self,
	) -> FavoritePlansRequest:
		from .favorite_plans import FavoritePlansRequest
		return FavoritePlansRequest(self.request_adapter, self.path_parameters)

	@property
	def my_day_tasks(self,
	) -> MyDayTasksRequest:
		from .my_day_tasks import MyDayTasksRequest
		return MyDayTasksRequest(self.request_adapter, self.path_parameters)

	@property
	def plans(self,
	) -> PlansRequest:
		from .plans import PlansRequest
		return PlansRequest(self.request_adapter, self.path_parameters)

	@property
	def recent_plans(self,
	) -> RecentPlansRequest:
		from .recent_plans import RecentPlansRequest
		return RecentPlansRequest(self.request_adapter, self.path_parameters)

	@property
	def roster_plans(self,
	) -> RosterPlansRequest:
		from .roster_plans import RosterPlansRequest
		return RosterPlansRequest(self.request_adapter, self.path_parameters)

	@property
	def tasks(self,
	) -> TasksRequest:
		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, self.path_parameters)

