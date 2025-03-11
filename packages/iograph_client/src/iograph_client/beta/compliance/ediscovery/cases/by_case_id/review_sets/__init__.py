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
	from .by_review_set_id import ByReviewSetIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.ediscovery_review_set_collection_response import EdiscoveryReviewSetCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.ediscovery_review_set import EdiscoveryReviewSet


class ReviewSetsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/reviewSets", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoveryReviewSetCollectionResponse:
		"""
		Get reviewSet
		Retrieve the properties and relationships of a reviewSet object.
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryReviewSetCollectionResponse, error_mapping)

	async def post(
		self,
		body: EdiscoveryReviewSet,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EdiscoveryReviewSet:
		"""
		Create reviewSet
		Create a new reviewSet object. The request body contains the display name of the review set, which is the only writable property.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-case-post-reviewsets?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryReviewSet, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ReviewSetsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ReviewSetsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ReviewSetsRequest(self.request_adapter, self.path_parameters)

	def by_review_set_id(self,
		case_id: str,
		reviewSet_id: str,
	) -> ByReviewSetIdRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if reviewSet_id is None:
			raise TypeError("reviewSet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["reviewSet%2Did"] =  reviewSet_id

		from .by_review_set_id import ByReviewSetIdRequest
		return ByReviewSetIdRequest(self.request_adapter, path_parameters)

	def count(self,
		case_id: str,
	) -> CountRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

