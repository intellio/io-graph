# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .virtual_events import VirtualEventsRequest
	from .booking_currencies import BookingCurrenciesRequest
	from .booking_businesses import BookingBusinessesRequest
	from .backup_restore import BackupRestoreRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.solutions_root import SolutionsRoot
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class SolutionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SolutionsRoot:
		"""
		Get solutions
		
		"""
		tags = ['solutions.solutionsRoot']

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
		return await self.request_adapter.send_async(request_info, SolutionsRoot, error_mapping)

	async def patch(
		self,
		body: SolutionsRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SolutionsRoot:
		"""
		Update solutions
		
		"""
		tags = ['solutions.solutionsRoot']

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
		return await self.request_adapter.send_async(request_info, SolutionsRoot, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SolutionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SolutionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SolutionsRequest(self.request_adapter, self.path_parameters)

	@property
	def backup_restore(self,
	) -> BackupRestoreRequest:
		from .backup_restore import BackupRestoreRequest
		return BackupRestoreRequest(self.request_adapter, self.path_parameters)

	@property
	def booking_businesses(self,
	) -> BookingBusinessesRequest:
		from .booking_businesses import BookingBusinessesRequest
		return BookingBusinessesRequest(self.request_adapter, self.path_parameters)

	@property
	def booking_currencies(self,
	) -> BookingCurrenciesRequest:
		from .booking_currencies import BookingCurrenciesRequest
		return BookingCurrenciesRequest(self.request_adapter, self.path_parameters)

	@property
	def virtual_events(self,
	) -> VirtualEventsRequest:
		from .virtual_events import VirtualEventsRequest
		return VirtualEventsRequest(self.request_adapter, self.path_parameters)

