# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
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
	from .decisions import DecisionsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_review import AccessReview


class ByAccessReviewId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/accessReviews/{accessReview%2Did}/instances/{accessReview%2Did1}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReview:
		"""
		Get instances from accessReviews
		The collection of access reviews instances past, present, and future, if this object is a recurring access review.
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
		Update the navigation property instances in accessReviews
		
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
		Delete navigation property instances for accessReviews
		
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



	def with_url(self, raw_url: str) -> ByAccessReviewId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessReviewId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessReviewId1Request(self.request_adapter, self.path_parameters)

	def decisions(self,
		accessReview_id: str,
		accessReview_id1: str,
	) -> DecisionsRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")
		if accessReview_id1 is None:
			raise TypeError("accessReview_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id
		path_parameters["accessReview%2Did1"] =  accessReview_id1

		from .decisions import DecisionsRequest
		return DecisionsRequest(self.request_adapter, path_parameters)

	def apply_decisions(self,
		accessReview_id: str,
		accessReview_id1: str,
	) -> ApplyDecisionsRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")
		if accessReview_id1 is None:
			raise TypeError("accessReview_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id
		path_parameters["accessReview%2Did1"] =  accessReview_id1

		from .apply_decisions import ApplyDecisionsRequest
		return ApplyDecisionsRequest(self.request_adapter, path_parameters)

	def reset_decisions(self,
		accessReview_id: str,
		accessReview_id1: str,
	) -> ResetDecisionsRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")
		if accessReview_id1 is None:
			raise TypeError("accessReview_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id
		path_parameters["accessReview%2Did1"] =  accessReview_id1

		from .reset_decisions import ResetDecisionsRequest
		return ResetDecisionsRequest(self.request_adapter, path_parameters)

	def send_reminder(self,
		accessReview_id: str,
		accessReview_id1: str,
	) -> SendReminderRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")
		if accessReview_id1 is None:
			raise TypeError("accessReview_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id
		path_parameters["accessReview%2Did1"] =  accessReview_id1

		from .send_reminder import SendReminderRequest
		return SendReminderRequest(self.request_adapter, path_parameters)

	def stop(self,
		accessReview_id: str,
		accessReview_id1: str,
	) -> StopRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")
		if accessReview_id1 is None:
			raise TypeError("accessReview_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id
		path_parameters["accessReview%2Did1"] =  accessReview_id1

		from .stop import StopRequest
		return StopRequest(self.request_adapter, path_parameters)

	def my_decisions(self,
		accessReview_id: str,
		accessReview_id1: str,
	) -> MyDecisionsRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")
		if accessReview_id1 is None:
			raise TypeError("accessReview_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id
		path_parameters["accessReview%2Did1"] =  accessReview_id1

		from .my_decisions import MyDecisionsRequest
		return MyDecisionsRequest(self.request_adapter, path_parameters)

	def reviewers(self,
		accessReview_id: str,
		accessReview_id1: str,
	) -> ReviewersRequest:
		if accessReview_id is None:
			raise TypeError("accessReview_id cannot be null.")
		if accessReview_id1 is None:
			raise TypeError("accessReview_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReview%2Did"] =  accessReview_id
		path_parameters["accessReview%2Did1"] =  accessReview_id1

		from .reviewers import ReviewersRequest
		return ReviewersRequest(self.request_adapter, path_parameters)

