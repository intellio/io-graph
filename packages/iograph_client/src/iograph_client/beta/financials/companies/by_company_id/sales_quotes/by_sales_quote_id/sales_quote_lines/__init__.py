# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_sales_quote_line_id import BySalesQuoteLineIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.sales_quote_line_collection_response import SalesQuoteLineCollectionResponse


class SalesQuoteLinesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/salesQuotes/{salesQuote%2Did}/salesQuoteLines", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SalesQuoteLineCollectionResponse:
		"""
		Get salesQuoteLines from financials
		
		"""
		tags = ['financials.company']

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
		return await self.request_adapter.send_async(request_info, SalesQuoteLineCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> SalesQuoteLinesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SalesQuoteLinesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SalesQuoteLinesRequest(self.request_adapter, self.path_parameters)

	def by_sales_quote_line_id(self,
		company_id: UUID,
		salesQuote_id: UUID,
		salesQuoteLine_id: str,
	) -> BySalesQuoteLineIdRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesQuote_id is None:
			raise TypeError("salesQuote_id cannot be null.")
		if salesQuoteLine_id is None:
			raise TypeError("salesQuoteLine_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesQuote%2Did"] =  salesQuote_id
		path_parameters["salesQuoteLine%2Did"] =  salesQuoteLine_id

		from .by_sales_quote_line_id import BySalesQuoteLineIdRequest
		return BySalesQuoteLineIdRequest(self.request_adapter, path_parameters)

	def count(self,
		company_id: UUID,
		salesQuote_id: UUID,
	) -> CountRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesQuote_id is None:
			raise TypeError("salesQuote_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesQuote%2Did"] =  salesQuote_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

