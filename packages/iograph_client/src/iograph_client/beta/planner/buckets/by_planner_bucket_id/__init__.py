# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tasks import TasksRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.planner_bucket import PlannerBucket


class ByPlannerBucketIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/planner/buckets/{plannerBucket%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerBucket:
		"""
		Get plannerBucket
		Retrieve the properties and relationships of a plannerBucket object.
		Find more info here: https://learn.microsoft.com/graph/api/plannerbucket-get?view=graph-rest-beta
		"""
		tags = ['planner.plannerBucket']

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
		return await self.request_adapter.send_async(request_info, PlannerBucket, error_mapping)

	async def patch(
		self,
		body: PlannerBucket,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PlannerBucket:
		"""
		Update plannerbucket
		Update the properties of plannerbucket object.
		Find more info here: https://learn.microsoft.com/graph/api/plannerbucket-update?view=graph-rest-beta
		"""
		tags = ['planner.plannerBucket']
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
		return await self.request_adapter.send_async(request_info, PlannerBucket, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete plannerBucket
		Delete plannerBucket.
		Find more info here: https://learn.microsoft.com/graph/api/plannerbucket-delete?view=graph-rest-beta
		"""
		tags = ['planner.plannerBucket']
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



	def with_url(self, raw_url: str) -> ByPlannerBucketIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPlannerBucketIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPlannerBucketIdRequest(self.request_adapter, self.path_parameters)

	def tasks(self,
		plannerBucket_id: str,
	) -> TasksRequest:
		if plannerBucket_id is None:
			raise TypeError("plannerBucket_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["plannerBucket%2Did"] =  plannerBucket_id

		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, path_parameters)

