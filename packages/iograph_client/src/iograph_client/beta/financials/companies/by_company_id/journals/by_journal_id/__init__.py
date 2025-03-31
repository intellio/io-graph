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
	from .post import PostRequest
	from .journal_lines import JournalLinesRequest
	from .account import AccountRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.journal import Journal
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByJournalIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/journals/{journal%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Journal:
		"""
		Get journals from financials
		
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
		return await self.request_adapter.send_async(request_info, Journal, error_mapping)

	async def patch(
		self,
		body: Journal,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Journal:
		"""
		Update the navigation property journals in financials
		
		"""
		tags = ['financials.company']

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
		return await self.request_adapter.send_async(request_info, Journal, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property journals for financials
		
		"""
		tags = ['financials.company']
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



	def with_url(self, raw_url: str) -> ByJournalIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByJournalIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByJournalIdRequest(self.request_adapter, self.path_parameters)

	def account(self,
		company_id: UUID,
		journal_id: UUID,
	) -> AccountRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if journal_id is None:
			raise TypeError("journal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["journal%2Did"] =  journal_id

		from .account import AccountRequest
		return AccountRequest(self.request_adapter, path_parameters)

	def journal_lines(self,
		company_id: UUID,
		journal_id: UUID,
	) -> JournalLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if journal_id is None:
			raise TypeError("journal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["journal%2Did"] =  journal_id

		from .journal_lines import JournalLinesRequest
		return JournalLinesRequest(self.request_adapter, path_parameters)

	def post(self,
		company_id: UUID,
		journal_id: UUID,
	) -> PostRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if journal_id is None:
			raise TypeError("journal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["journal%2Did"] =  journal_id

		from .post import PostRequest
		return PostRequest(self.request_adapter, path_parameters)

