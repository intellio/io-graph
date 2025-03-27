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
	from .upload_agent import UploadAgentRequest
	from .renew import RenewRequest
	from .commit import CommitRequest
	from .cancel import CancelRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.exact_match_session import ExactMatchSession
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByExactMatchSessionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/dataClassification/exactMatchDataStores/{exactMatchDataStore%2Did}/sessions/{exactMatchSession%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExactMatchSession:
		"""
		Get sessions from dataClassification
		
		"""
		tags = ['dataClassification.exactMatchDataStore']

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
		return await self.request_adapter.send_async(request_info, ExactMatchSession, error_mapping)

	async def patch(
		self,
		body: ExactMatchSession,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ExactMatchSession:
		"""
		Update the navigation property sessions in dataClassification
		
		"""
		tags = ['dataClassification.exactMatchDataStore']

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
		return await self.request_adapter.send_async(request_info, ExactMatchSession, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property sessions for dataClassification
		
		"""
		tags = ['dataClassification.exactMatchDataStore']
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



	def with_url(self, raw_url: str) -> ByExactMatchSessionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByExactMatchSessionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByExactMatchSessionIdRequest(self.request_adapter, self.path_parameters)

	def cancel(self,
		exactMatchDataStore_id: str,
		exactMatchSession_id: str,
	) -> CancelRequest:
		if exactMatchDataStore_id is None:
			raise TypeError("exactMatchDataStore_id cannot be null.")
		if exactMatchSession_id is None:
			raise TypeError("exactMatchSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["exactMatchDataStore%2Did"] =  exactMatchDataStore_id
		path_parameters["exactMatchSession%2Did"] =  exactMatchSession_id

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def commit(self,
		exactMatchDataStore_id: str,
		exactMatchSession_id: str,
	) -> CommitRequest:
		if exactMatchDataStore_id is None:
			raise TypeError("exactMatchDataStore_id cannot be null.")
		if exactMatchSession_id is None:
			raise TypeError("exactMatchSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["exactMatchDataStore%2Did"] =  exactMatchDataStore_id
		path_parameters["exactMatchSession%2Did"] =  exactMatchSession_id

		from .commit import CommitRequest
		return CommitRequest(self.request_adapter, path_parameters)

	def renew(self,
		exactMatchDataStore_id: str,
		exactMatchSession_id: str,
	) -> RenewRequest:
		if exactMatchDataStore_id is None:
			raise TypeError("exactMatchDataStore_id cannot be null.")
		if exactMatchSession_id is None:
			raise TypeError("exactMatchSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["exactMatchDataStore%2Did"] =  exactMatchDataStore_id
		path_parameters["exactMatchSession%2Did"] =  exactMatchSession_id

		from .renew import RenewRequest
		return RenewRequest(self.request_adapter, path_parameters)

	def upload_agent(self,
		exactMatchDataStore_id: str,
		exactMatchSession_id: str,
	) -> UploadAgentRequest:
		if exactMatchDataStore_id is None:
			raise TypeError("exactMatchDataStore_id cannot be null.")
		if exactMatchSession_id is None:
			raise TypeError("exactMatchSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["exactMatchDataStore%2Did"] =  exactMatchDataStore_id
		path_parameters["exactMatchSession%2Did"] =  exactMatchSession_id

		from .upload_agent import UploadAgentRequest
		return UploadAgentRequest(self.request_adapter, path_parameters)

