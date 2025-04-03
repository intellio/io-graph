# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_access_review_id import ByAccessReviewIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_review import AccessReview
from iograph_models.beta.access_review_collection_response import AccessReviewCollectionResponse


class AccessReviewsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/accessReviews", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReviewCollectionResponse:
		"""
		List accessReviews (deprecated)
		Retrieve the accessReview objects for a particular businessFlowTemplate. A list of zero or more accessReview objects are returned, for each one-time and recurring access review that was created with that business flow template.  Business flow template IDs are case sensitive. If many access reviews match the filter, to improve efficiency and avoid timeouts, retrieve the result set in pages, by including both the $top query parameter with a page size, for example 100, and the $skip=0 query parameter in the request. These parameters can be included even when you don't anticipate that the request spans multiple pages. When a result set spans multiple pages, Microsoft Graph returns that page with an @odata.nextLink property in the response that contains a URL to the next page of results. If that property is present, continue making requests with the @odata.nextLink URL in each response, until all the results are returned, as described in paging Microsoft Graph data in your app. The accessReview objects returned by this API don't include nested structure properties such as settings, or relationships.  To retrieve an access review settings or relationships, use the get accessReview API.
		Find more info here: https://learn.microsoft.com/graph/api/accessreview-list?view=graph-rest-beta
		"""
		tags = ['accessReviews.accessReview']

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
		return await self.request_adapter.send_async(request_info, AccessReviewCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessReview,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReview:
		"""
		Create accessReview (deprecated)
		In the Microsoft Entra access reviews feature, create a new accessReview object. Before making this request, the caller must have previously retrieved the list of business flow templates, to have the value of businessFlowTemplateId to include in the request. After making this request, the caller should create a programControl, to link the access review to a program.  
		Find more info here: https://learn.microsoft.com/graph/api/accessreview-create?view=graph-rest-beta
		"""
		tags = ['accessReviews.accessReview']

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
		return await self.request_adapter.send_async(request_info, AccessReview, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AccessReviewsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AccessReviewsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AccessReviewsRequest(self.request_adapter, self.path_parameters)

	def by_access_review_id(self,
		accessReview_id: str,
	) -> ByAccessReviewIdRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .by_access_review_id import ByAccessReviewIdRequest
		return ByAccessReviewIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

