# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_exchange_restore_session_id import ByExchangeRestoreSessionIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.exchange_restore_session import ExchangeRestoreSession
from iograph_models.beta.exchange_restore_session_collection_response import ExchangeRestoreSessionCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ExchangeRestoreSessionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/exchangeRestoreSessions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExchangeRestoreSessionCollectionResponse:
		"""
		Get exchangeRestoreSessions from solutions
		The list of Exchange restore sessions available in the tenant.
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, ExchangeRestoreSessionCollectionResponse, error_mapping)

	async def post(
		self,
		body: ExchangeRestoreSession,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ExchangeRestoreSession:
		"""
		Create new navigation property to exchangeRestoreSessions for solutions
		
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, ExchangeRestoreSession, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ExchangeRestoreSessionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ExchangeRestoreSessionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ExchangeRestoreSessionsRequest(self.request_adapter, self.path_parameters)

	def by_exchange_restore_session_id(self,
		exchangeRestoreSession_id: str,
	) -> ByExchangeRestoreSessionIdRequest:
		if exchangeRestoreSession_id is None:
			raise TypeError("exchangeRestoreSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["exchangeRestoreSession%2Did"] =  exchangeRestoreSession_id

		from .by_exchange_restore_session_id import ByExchangeRestoreSessionIdRequest
		return ByExchangeRestoreSessionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

