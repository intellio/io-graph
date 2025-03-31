# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .host import HostRequest
	from .history import HistoryRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.security_whois_record import SecurityWhoisRecord
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByWhoisRecordIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence/whoisRecords/{whoisRecord%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityWhoisRecord:
		"""
		Get whoisRecord
		Get the specified whoisRecord resource.  Specify the desired whoisRecord in one of the following two ways:
- Identify a host and get its current whoisRecord. 
- Specify an id value to get the corresponding whoisRecord.
		Find more info here: https://learn.microsoft.com/graph/api/security-whoisrecord-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityWhoisRecord, error_mapping)

	async def patch(
		self,
		body: SecurityWhoisRecord,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityWhoisRecord:
		"""
		Update the navigation property whoisRecords in security
		
		"""
		tags = ['security.threatIntelligence']

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
		return await self.request_adapter.send_async(request_info, SecurityWhoisRecord, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property whoisRecords for security
		
		"""
		tags = ['security.threatIntelligence']
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



	def with_url(self, raw_url: str) -> ByWhoisRecordIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWhoisRecordIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWhoisRecordIdRequest(self.request_adapter, self.path_parameters)

	def history(self,
		whoisRecord_id: str,
	) -> HistoryRequest:
		if whoisRecord_id is None:
			raise TypeError("whoisRecord_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["whoisRecord%2Did"] =  whoisRecord_id

		from .history import HistoryRequest
		return HistoryRequest(self.request_adapter, path_parameters)

	def host(self,
		whoisRecord_id: str,
	) -> HostRequest:
		if whoisRecord_id is None:
			raise TypeError("whoisRecord_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["whoisRecord%2Did"] =  whoisRecord_id

		from .host import HostRequest
		return HostRequest(self.request_adapter, path_parameters)

