# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.get_managed_app_diagnostic_statuses_response import GetManagedAppDiagnosticStatusesResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class GetManagedAppDiagnosticStatusesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/getManagedAppDiagnosticStatuses()", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GetManagedAppDiagnosticStatusesResponse:
		"""
		Invoke function getManagedAppDiagnosticStatuses
		Gets diagnostics validation status for a given user.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-user-getmanagedappdiagnosticstatuses?view=graph-rest-1.0
		"""
		tags = ['users.user.Functions']

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
		return await self.request_adapter.send_async(request_info, GetManagedAppDiagnosticStatusesResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")

	def with_url(self, raw_url: str) -> GetManagedAppDiagnosticStatusesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GetManagedAppDiagnosticStatusesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GetManagedAppDiagnosticStatusesRequest(self.request_adapter, self.path_parameters)

