# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .ediscovery_apply_tags import EdiscoveryApplyTagsRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.beta.ediscovery_review_set_query import EdiscoveryReviewSetQuery
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByReviewSetQueryIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/reviewSets/{reviewSet%2Did}/queries/{reviewSetQuery%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoveryReviewSetQuery:
		"""
		Get reviewSetQuery
		Retrieve the properties and relationships of an eDiscovery reviewSetQuery object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-reviewsetquery-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EdiscoveryReviewSetQuery, error_mapping)

	async def patch(
		self,
		body: EdiscoveryReviewSetQuery,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EdiscoveryReviewSetQuery:
		"""
		Update reviewSetQuery
		Update the properties of an eDiscovery reviewSetQuery.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-reviewsetquery-update?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryReviewSetQuery, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete reviewSetQuery
		Delete a reviewSetQuery object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-reviewsetquery-delete?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']
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



	def with_url(self, raw_url: str) -> ByReviewSetQueryIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByReviewSetQueryIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByReviewSetQueryIdRequest(self.request_adapter, self.path_parameters)

	def ediscovery_apply_tags(self,
		case_id: str,
		reviewSet_id: str,
		reviewSetQuery_id: str,
	) -> EdiscoveryApplyTagsRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if reviewSet_id is None:
			raise TypeError("reviewSet_id cannot be null.")
		if reviewSetQuery_id is None:
			raise TypeError("reviewSetQuery_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["reviewSet%2Did"] =  reviewSet_id
		path_parameters["reviewSetQuery%2Did"] =  reviewSetQuery_id

		from .ediscovery_apply_tags import EdiscoveryApplyTagsRequest
		return EdiscoveryApplyTagsRequest(self.request_adapter, path_parameters)

