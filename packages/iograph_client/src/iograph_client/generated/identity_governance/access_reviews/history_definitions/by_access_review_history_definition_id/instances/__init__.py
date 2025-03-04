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
	from .by_access_review_history_instance_id import ByAccessReviewHistoryInstanceIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.access_review_history_instance_collection_response import AccessReviewHistoryInstanceCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.access_review_history_instance import AccessReviewHistoryInstance


class InstancesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/accessReviews/historyDefinitions/{accessReviewHistoryDefinition%2Did}/instances", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReviewHistoryInstanceCollectionResponse:
		"""
		List instances (of an accessReviewHistoryDefinition)
		Retrieve the instances of an access review history definition created in the last 30 days.
		Find more info here: https://learn.microsoft.com/graph/api/accessreviewhistorydefinition-list-instances?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, AccessReviewHistoryInstanceCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessReviewHistoryInstance,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReviewHistoryInstance:
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
		return await self.request_adapter.send_async(request_info, AccessReviewHistoryInstance, error_mapping)

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

	def by_access_review_history_instance_id(self,
		accessReviewHistoryDefinition_id: str,
		accessReviewHistoryInstance_id: str,
	) -> ByAccessReviewHistoryInstanceIdRequest:
		if accessReviewHistoryDefinition_id is None:
			raise TypeError("accessReviewHistoryDefinition_id cannot be null.")
		if accessReviewHistoryInstance_id is None:
			raise TypeError("accessReviewHistoryInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReviewHistoryDefinition%2Did"] =  accessReviewHistoryDefinition_id
		path_parameters["accessReviewHistoryInstance%2Did"] =  accessReviewHistoryInstance_id

		from .by_access_review_history_instance_id import ByAccessReviewHistoryInstanceIdRequest
		return ByAccessReviewHistoryInstanceIdRequest(self.request_adapter, path_parameters)

	def count(self,
		accessReviewHistoryDefinition_id: str,
	) -> CountRequest:
		if accessReviewHistoryDefinition_id is None:
			raise TypeError("accessReviewHistoryDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReviewHistoryDefinition%2Did"] =  accessReviewHistoryDefinition_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

