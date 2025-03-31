# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .insights import InsightsRequest
	from ............request_adapter import HttpxRequestAdapter
from iograph_models.beta.access_review_instance_decision_item import AccessReviewInstanceDecisionItem
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByAccessReviewInstanceDecisionItemId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/pendingAccessReviewInstances/{accessReviewInstance%2Did}/decisions/{accessReviewInstanceDecisionItem%2Did}/instance/stages/{accessReviewStage%2Did}/decisions/{accessReviewInstanceDecisionItem%2Did1}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessReviewInstanceDecisionItem:
		"""
		Get decisions from me
		Each user reviewed in an accessReviewStage has a decision item representing if they were approved, denied, or not yet reviewed.
		"""
		tags = ['me.accessReviewInstance']

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
		return await self.request_adapter.send_async(request_info, AccessReviewInstanceDecisionItem, error_mapping)

	async def patch(
		self,
		body: AccessReviewInstanceDecisionItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessReviewInstanceDecisionItem:
		"""
		Update the navigation property decisions in me
		
		"""
		tags = ['me.accessReviewInstance']

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
		return await self.request_adapter.send_async(request_info, AccessReviewInstanceDecisionItem, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property decisions for me
		
		"""
		tags = ['me.accessReviewInstance']
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



	def with_url(self, raw_url: str) -> ByAccessReviewInstanceDecisionItemId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessReviewInstanceDecisionItemId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessReviewInstanceDecisionItemId1Request(self.request_adapter, self.path_parameters)

	def insights(self,
		accessReviewInstance_id: str,
		accessReviewInstanceDecisionItem_id: str,
		accessReviewStage_id: str,
		accessReviewInstanceDecisionItem_id1: str,
	) -> InsightsRequest:
		if accessReviewInstance_id is None:
			raise TypeError("accessReviewInstance_id cannot be null.")
		if accessReviewInstanceDecisionItem_id is None:
			raise TypeError("accessReviewInstanceDecisionItem_id cannot be null.")
		if accessReviewStage_id is None:
			raise TypeError("accessReviewStage_id cannot be null.")
		if accessReviewInstanceDecisionItem_id1 is None:
			raise TypeError("accessReviewInstanceDecisionItem_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessReviewInstance%2Did"] =  accessReviewInstance_id
		path_parameters["accessReviewInstanceDecisionItem%2Did"] =  accessReviewInstanceDecisionItem_id
		path_parameters["accessReviewStage%2Did"] =  accessReviewStage_id
		path_parameters["accessReviewInstanceDecisionItem%2Did1"] =  accessReviewInstanceDecisionItem_id1

		from .insights import InsightsRequest
		return InsightsRequest(self.request_adapter, path_parameters)

