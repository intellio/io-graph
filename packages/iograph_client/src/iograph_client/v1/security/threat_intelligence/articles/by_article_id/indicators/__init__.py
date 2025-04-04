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
	from .by_article_indicator_id import ByArticleIndicatorIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.security_article_indicator_collection_response import SecurityArticleIndicatorCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class IndicatorsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence/articles/{article%2Did}/indicators", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityArticleIndicatorCollectionResponse:
		"""
		List indicators
		Get a list of articleIndicator objects that represent indicators of threat or compromise related to the contents of an article.
		Find more info here: https://learn.microsoft.com/graph/api/security-article-list-indicators?view=graph-rest-1.0
		"""
		tags = ['security.threatIntelligence']

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
		return await self.request_adapter.send_async(request_info, SecurityArticleIndicatorCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> IndicatorsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: IndicatorsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return IndicatorsRequest(self.request_adapter, self.path_parameters)

	def by_article_indicator_id(self,
		article_id: str,
		articleIndicator_id: str,
	) -> ByArticleIndicatorIdRequest:
		if article_id is None:
			raise TypeError("article_id cannot be null.")
		if articleIndicator_id is None:
			raise TypeError("articleIndicator_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["article%2Did"] =  article_id
		path_parameters["articleIndicator%2Did"] =  articleIndicator_id

		from .by_article_indicator_id import ByArticleIndicatorIdRequest
		return ByArticleIndicatorIdRequest(self.request_adapter, path_parameters)

	def count(self,
		article_id: str,
	) -> CountRequest:
		if article_id is None:
			raise TypeError("article_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["article%2Did"] =  article_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

