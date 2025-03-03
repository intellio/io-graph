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
	from .by_access_review_instance_id import ByAccessReviewInstanceIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.access_review_instance_collection_response import AccessReviewInstanceCollectionResponse
from iograph_models.models.access_review_instance import AccessReviewInstance
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class InstancesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/accessReviews/definitions/{accessReviewScheduleDefinition%2Did}/instances", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReviewInstanceCollectionResponse:
		"""
		List instances
		Get a list of the accessReviewInstance objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/accessreviewscheduledefinition-list-instances?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.accessReviewSet']

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
		return await self.request_adapter.send_async(request_info, AccessReviewInstanceCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessReviewInstance,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReviewInstance:
		"""
		Create new navigation property to instances for identityGovernance
		
		"""
		tags = ['identityGovernance.accessReviewSet']

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
		return await self.request_adapter.send_async(request_info, AccessReviewInstance, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> InstancesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: InstancesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return InstancesRequest(self.request_adapter, self.path_parameters)

	def by_access_review_instance_id(self,
		accessReviewScheduleDefinition_id: str,
		accessReviewInstance_id: str,
	) -> ByAccessReviewInstanceIdRequest:
		if accessReviewScheduleDefinition_id is None:
			raise TypeError("accessReviewScheduleDefinition_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReviewScheduleDefinition%2Did"] =  accessReviewScheduleDefinition_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id

		from .by_access_review_instance_id import ByAccessReviewInstanceIdRequest
		return ByAccessReviewInstanceIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

