# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .reviewers import ReviewersRequest
	from .my_decisions import MyDecisionsRequest
	from .stop import StopRequest
	from .send_reminder import SendReminderRequest
	from .reset_decisions import ResetDecisionsRequest
	from .apply_decisions import ApplyDecisionsRequest
	from .instances import InstancesRequest
	from .decisions import DecisionsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_review import AccessReview


class ByAccessReviewIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/accessReviews/{accessReview%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReview:
		"""
		Get accessReview (deprecated)
		In the Microsoft Entra access reviews feature, retrieve an accessReview object.   To retrieve the reviewers of the access review, use the list accessReview reviewers API. To retrieve the decisions of the access review, use the list accessReview decisions API, or the list my accessReview decisions API. If this is a recurring access review, no decisions will be associated with the recurring access review series. Instead, use the instances relationship of that series to retrieve an accessReview collection of the past, current, and future instances of the access review. Each past and current instance will have decisions.
		Find more info here: https://learn.microsoft.com/graph/api/accessreview-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, AccessReview, error_mapping)

	async def patch(
		self,
		body: AccessReview,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReview:
		"""
		Update accessReview (deprecated)
		In the Microsoft Entra access reviews feature, update an existing accessReview object to change one or more of its properties. This API is not intended to change the reviewers or decisions of a review.  To change the reviewers, use the addReviewer or removeReviewer APIs.  To stop an already-started one-time review, or an already-started instance of a recurring review, early, use the stop API. To apply the decisions to the target group or app access rights, use the apply API. 
		Find more info here: https://learn.microsoft.com/graph/api/accessreview-update?view=graph-rest-beta
		"""
		tags = ['accessReviews.accessReview']

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
		return await self.request_adapter.send_async(request_info, AccessReview, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete accessReview (deprecated)
		In the Microsoft Entra access reviews feature, delete an accessReview object.
		Find more info here: https://learn.microsoft.com/graph/api/accessreview-delete?view=graph-rest-beta
		"""
		tags = ['accessReviews.accessReview']
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



	def with_url(self, raw_url: str) -> ByAccessReviewIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessReviewIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessReviewIdRequest(self.request_adapter, self.path_parameters)

	def decisions(self,
		accessReview_id: str,
	) -> DecisionsRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .decisions import DecisionsRequest
		return DecisionsRequest(self.request_adapter, path_parameters)

	def instances(self,
		accessReview_id: str,
	) -> InstancesRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .instances import InstancesRequest
		return InstancesRequest(self.request_adapter, path_parameters)

	def apply_decisions(self,
		accessReview_id: str,
	) -> ApplyDecisionsRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .apply_decisions import ApplyDecisionsRequest
		return ApplyDecisionsRequest(self.request_adapter, path_parameters)

	def reset_decisions(self,
		accessReview_id: str,
	) -> ResetDecisionsRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .reset_decisions import ResetDecisionsRequest
		return ResetDecisionsRequest(self.request_adapter, path_parameters)

	def send_reminder(self,
		accessReview_id: str,
	) -> SendReminderRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .send_reminder import SendReminderRequest
		return SendReminderRequest(self.request_adapter, path_parameters)

	def stop(self,
		accessReview_id: str,
	) -> StopRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .stop import StopRequest
		return StopRequest(self.request_adapter, path_parameters)

	def my_decisions(self,
		accessReview_id: str,
	) -> MyDecisionsRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .my_decisions import MyDecisionsRequest
		return MyDecisionsRequest(self.request_adapter, path_parameters)

	def reviewers(self,
		accessReview_id: str,
	) -> ReviewersRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id

		from .reviewers import ReviewersRequest
		return ReviewersRequest(self.request_adapter, path_parameters)

