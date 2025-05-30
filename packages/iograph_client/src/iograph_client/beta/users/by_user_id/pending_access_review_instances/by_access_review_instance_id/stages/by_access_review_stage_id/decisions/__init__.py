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
	from .record_all_decisions import RecordAllDecisionsRequest
	from .filter_by_current_user_with_on import FilterByCurrentUserWithOnRequest
	from .count import CountRequest
	from .by_access_review_instance_decision_item_id import ByAccessReviewInstanceDecisionItemIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.access_review_instance_decision_item_collection_response import AccessReviewInstanceDecisionItemCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_review_instance_decision_item import AccessReviewInstanceDecisionItem


class DecisionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/pendingAccessReviewInstances/{accessReviewInstance%2Did}/stages/{accessReviewStage%2Did}/decisions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReviewInstanceDecisionItemCollectionResponse:
		"""
		Get decisions from users
		Each user reviewed in an accessReviewStage has a decision item representing if they were approved, denied, or not yet reviewed.
		"""
		tags = ['users.accessReviewInstance']

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
		return await self.request_adapter.send_async(request_info, AccessReviewInstanceDecisionItemCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessReviewInstanceDecisionItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReviewInstanceDecisionItem:
		"""
		Create new navigation property to decisions for users
		
		"""
		tags = ['users.accessReviewInstance']

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
		return await self.request_adapter.send_async(request_info, AccessReviewInstanceDecisionItem, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DecisionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DecisionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DecisionsRequest(self.request_adapter, self.path_parameters)

	def by_access_review_instance_decision_item_id(self,
		user_id: str,
		accessReviewInstance_id: str,
		accessReviewStage_id: str,
		accessReviewInstanceDecisionItem_id: str,
	) -> ByAccessReviewInstanceDecisionItemIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")
		if accessReviewStage_id is None:
			raise TypeError("accessReviewStage_id cannot be null.")
		if accessReviewInstanceDecisionItem_id is None:
			raise TypeError("accessReviewInstanceDecisionItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id
		path_parameters["accessReviewStage%2Did"] =  accessReviewStage_id
		path_parameters["accessReviewInstanceDecisionItem%2Did"] =  accessReviewInstanceDecisionItem_id

		from .by_access_review_instance_decision_item_id import ByAccessReviewInstanceDecisionItemIdRequest
		return ByAccessReviewInstanceDecisionItemIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		accessReviewInstance_id: str,
		accessReviewStage_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")
		if accessReviewStage_id is None:
			raise TypeError("accessReviewStage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id
		path_parameters["accessReviewStage%2Did"] =  accessReviewStage_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def filter_by_current_user_with_on(self,
		user_id: str,
		accessReviewInstance_id: str,
		accessReviewStage_id: str,
		on: str,
	) -> FilterByCurrentUserWithOnRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")
		if accessReviewStage_id is None:
			raise TypeError("accessReviewStage_id cannot be null.")
		if on is None:
			raise TypeError("on cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id
		path_parameters["accessReviewStage%2Did"] =  accessReviewStage_id
		path_parameters["on"] =  on

		from .filter_by_current_user_with_on import FilterByCurrentUserWithOnRequest
		return FilterByCurrentUserWithOnRequest(self.request_adapter, path_parameters)

	def record_all_decisions(self,
		user_id: str,
		accessReviewInstance_id: str,
		accessReviewStage_id: str,
	) -> RecordAllDecisionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")
		if accessReviewStage_id is None:
			raise TypeError("accessReviewStage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id
		path_parameters["accessReviewStage%2Did"] =  accessReviewStage_id

		from .record_all_decisions import RecordAllDecisionsRequest
		return RecordAllDecisionsRequest(self.request_adapter, path_parameters)

