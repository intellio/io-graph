# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.set_review_status_post_request import Set_review_statusPostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SetReviewStatusRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/cloudPCs/{cloudPC%2Did}/setReviewStatus", path_parameters)

	async def post(
		self,
		body: Set_review_statusPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action setReviewStatus
		Set the review status of a specific Cloud PC device using the Cloud PC ID. Use this API to set the review status of a Cloud PC to in review if you consider a Cloud PC suspicious. After the review is completed, use this API again to set the Cloud PC back to a normal state.
		Find more info here: https://learn.microsoft.com/graph/api/cloudpc-setreviewstatus?view=graph-rest-beta
		"""
		tags = ['me.cloudPC']

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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


	def with_url(self, raw_url: str) -> SetReviewStatusRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SetReviewStatusRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SetReviewStatusRequest(self.request_adapter, self.path_parameters)

