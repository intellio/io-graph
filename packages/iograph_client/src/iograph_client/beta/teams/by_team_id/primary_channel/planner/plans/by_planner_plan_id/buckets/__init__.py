# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_planner_bucket_id import ByPlannerBucketIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.planner_bucket_collection_response import PlannerBucketCollectionResponse
from iograph_models.beta.planner_bucket import PlannerBucket


class BucketsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teams/{team%2Did}/primaryChannel/planner/plans/{plannerPlan%2Did}/buckets", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerBucketCollectionResponse:
		"""
		Get buckets from teams
		Collection of buckets in the plan. Read-only. Nullable.
		"""
		tags = ['teams.channel']

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
		return await self.request_adapter.send_async(request_info, PlannerBucketCollectionResponse, error_mapping)

	async def post(
		self,
		body: PlannerBucket,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PlannerBucket:
		"""
		Create new navigation property to buckets for teams
		
		"""
		tags = ['teams.channel']

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
		return await self.request_adapter.send_async(request_info, PlannerBucket, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> BucketsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BucketsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BucketsRequest(self.request_adapter, self.path_parameters)

	def by_planner_bucket_id(self,
		team_id: str,
		plannerPlan_id: str,
		plannerBucket_id: str,
	) -> ByPlannerBucketIdRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")
		if plannerBucket_id is None:
			raise TypeError("plannerBucket_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id
		path_parameters["plannerBucket%2Did"] =  plannerBucket_id

		from .by_planner_bucket_id import ByPlannerBucketIdRequest
		return ByPlannerBucketIdRequest(self.request_adapter, path_parameters)

	def count(self,
		team_id: str,
		plannerPlan_id: str,
	) -> CountRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def delta(self,
		team_id: str,
		plannerPlan_id: str,
	) -> DeltaRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id

		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, path_parameters)

