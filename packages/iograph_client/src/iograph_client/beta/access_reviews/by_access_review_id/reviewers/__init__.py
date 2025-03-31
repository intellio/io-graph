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
	from .count import CountRequest
	from .by_access_review_reviewer_id import ByAccessReviewReviewerIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.access_review_reviewer_collection_response import AccessReviewReviewerCollectionResponse
from iograph_models.beta.access_review_reviewer import AccessReviewReviewer
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ReviewersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/accessReviews/{accessReview%2Did}/reviewers", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReviewReviewerCollectionResponse:
		"""
		List accessReview reviewers (deprecated)
		In the Microsoft Entra access reviews feature, retrieve the reviewers of an accessReview object.
		Find more info here: https://learn.microsoft.com/graph/api/accessreview-listreviewers?view=graph-rest-beta
		"""
		tags = ['accessReviews.accessReviewReviewer']

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
		return await self.request_adapter.send_async(request_info, AccessReviewReviewerCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessReviewReviewer,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReviewReviewer:
		"""
		Add accessReview reviewer (deprecated)
		In the Microsoft Entra access reviews feature, update an existing accessReview object to add another user as a reviewer.  This operation is only permitted for an access review that isn't yet completed, and only for an access review where the reviewers are explicitly specified. This operation isn't permitted for an access review in which users review their own access, and not intended for an access review in which the group owners are assigned as the reviewers. 
		Find more info here: https://learn.microsoft.com/graph/api/accessreview-addreviewer?view=graph-rest-beta
		"""
		tags = ['accessReviews.accessReviewReviewer']

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
		return await self.request_adapter.send_async(request_info, AccessReviewReviewer, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ReviewersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ReviewersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ReviewersRequest(self.request_adapter, self.path_parameters)

	def by_access_review_reviewer_id(self,
		accessReview_id: str,
		accessReviewReviewer_id: str,
	) -> ByAccessReviewReviewerIdRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")
		if accessReviewReviewer_id is None:
			raise TypeError("accessReviewReviewer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id
		path_parameters["accessReviewReviewer%2Did"] =  accessReviewReviewer_id

		from .by_access_review_reviewer_id import ByAccessReviewReviewerIdRequest
		return ByAccessReviewReviewerIdRequest(self.request_adapter, path_parameters)

	def count(self,
		accessReview_id: str,
	) -> CountRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

