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
	from .count import CountRequest
	from .by_qna_id import ByQnaIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.search_qna_collection_response import SearchQnaCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.search_qna import SearchQna


class QnasRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/search/qnas", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SearchQnaCollectionResponse:
		"""
		List qnas
		Get a list of the qna objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/search-searchentity-list-qnas?view=graph-rest-1.0
		"""
		tags = ['search.qna']

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
		return await self.request_adapter.send_async(request_info, SearchQnaCollectionResponse, error_mapping)

	async def post(
		self,
		body: SearchQna,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SearchQna:
		"""
		Create qna
		Create a new qna object.
		Find more info here: https://learn.microsoft.com/graph/api/search-searchentity-post-qnas?view=graph-rest-1.0
		"""
		tags = ['search.qna']

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
		return await self.request_adapter.send_async(request_info, SearchQna, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> QnasRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: QnasRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return QnasRequest(self.request_adapter, self.path_parameters)

	def by_qna_id(self,
		qna_id: str,
	) -> ByQnaIdRequest:
		if qna_id is None:
			raise TypeError("qna_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["qna%2Did"] =  qna_id

		from .by_qna_id import ByQnaIdRequest
		return ByQnaIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

