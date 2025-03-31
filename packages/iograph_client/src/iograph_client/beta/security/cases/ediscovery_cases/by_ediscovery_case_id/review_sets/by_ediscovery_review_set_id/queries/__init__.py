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
	from .count import CountRequest
	from .by_ediscovery_review_set_query_id import ByEdiscoveryReviewSetQueryIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.security_ediscovery_review_set_query import SecurityEdiscoveryReviewSetQuery
from iograph_models.beta.security_ediscovery_review_set_query_collection_response import SecurityEdiscoveryReviewSetQueryCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class QueriesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/reviewSets/{ediscoveryReviewSet%2Did}/queries", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityEdiscoveryReviewSetQueryCollectionResponse:
		"""
		List queries
		Get the list of queries associated with an eDiscovery review set.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoveryreviewset-list-queries?view=graph-rest-beta
		"""
		tags = ['security.casesRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryReviewSetQueryCollectionResponse, error_mapping)

	async def post(
		self,
		body: SecurityEdiscoveryReviewSetQuery,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityEdiscoveryReviewSetQuery:
		"""
		Create ediscoveryReviewSetQuery
		Create a new ediscoveryReviewSetQuery object.
		Find more info here: https://learn.microsoft.com/graph/api/security-ediscoveryreviewset-post-queries?view=graph-rest-beta
		"""
		tags = ['security.casesRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityEdiscoveryReviewSetQuery, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> QueriesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: QueriesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return QueriesRequest(self.request_adapter, self.path_parameters)

	def by_ediscovery_review_set_query_id(self,
		ediscoveryCase_id: str,
		ediscoveryReviewSet_id: str,
		ediscoveryReviewSetQuery_id: str,
	) -> ByEdiscoveryReviewSetQueryIdRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryReviewSet_id is None:
			raise TypeError("ediscoveryReviewSet_id cannot be null.")
		if ediscoveryReviewSetQuery_id is None:
			raise TypeError("ediscoveryReviewSetQuery_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryReviewSet%2Did"] =  ediscoveryReviewSet_id
		path_parameters["ediscoveryReviewSetQuery%2Did"] =  ediscoveryReviewSetQuery_id

		from .by_ediscovery_review_set_query_id import ByEdiscoveryReviewSetQueryIdRequest
		return ByEdiscoveryReviewSetQueryIdRequest(self.request_adapter, path_parameters)

	def count(self,
		ediscoveryCase_id: str,
		ediscoveryReviewSet_id: str,
	) -> CountRequest:
		if ediscoveryCase_id is None:
			raise TypeError("ediscoveryCase_id cannot be null.")
		if ediscoveryReviewSet_id is None:
			raise TypeError("ediscoveryReviewSet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ediscoveryCase%2Did"] =  ediscoveryCase_id
		path_parameters["ediscoveryReviewSet%2Did"] =  ediscoveryReviewSet_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

