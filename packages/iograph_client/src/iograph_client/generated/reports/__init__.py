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
	from .security import SecurityRequest
	from .partners import PartnersRequest
	from .monthly_print_usage_by_user import MonthlyPrintUsageByUserRequest
	from .monthly_print_usage_by_printer import MonthlyPrintUsageByPrinterRequest
	from .daily_print_usage_by_user import DailyPrintUsageByUserRequest
	from .daily_print_usage_by_printer import DailyPrintUsageByPrinterRequest
	from .authentication_methods import AuthenticationMethodsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.report_root import ReportRoot
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ReportsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/reports", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ReportRoot:
		"""
		Get reportRoot
		Read properties and relationships of the reportRoot object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-reportroot-get?view=graph-rest-1.0
		"""
		tags = ['reports.reportRoot']

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
		return await self.request_adapter.send_async(request_info, ReportRoot, error_mapping)

	async def patch(
		self,
		body: ReportRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ReportRoot:
		"""
		Update reportRoot
		Update the properties of a reportRoot object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-reportroot-update?view=graph-rest-1.0
		"""
		tags = ['reports.reportRoot']

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
		return await self.request_adapter.send_async(request_info, ReportRoot, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ReportsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ReportsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_methods(self,
	) -> AuthenticationMethodsRequest:
		from .authentication_methods import AuthenticationMethodsRequest
		return AuthenticationMethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def daily_print_usage_by_printer(self,
	) -> DailyPrintUsageByPrinterRequest:
		from .daily_print_usage_by_printer import DailyPrintUsageByPrinterRequest
		return DailyPrintUsageByPrinterRequest(self.request_adapter, self.path_parameters)

	@property
	def daily_print_usage_by_user(self,
	) -> DailyPrintUsageByUserRequest:
		from .daily_print_usage_by_user import DailyPrintUsageByUserRequest
		return DailyPrintUsageByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def monthly_print_usage_by_printer(self,
	) -> MonthlyPrintUsageByPrinterRequest:
		from .monthly_print_usage_by_printer import MonthlyPrintUsageByPrinterRequest
		return MonthlyPrintUsageByPrinterRequest(self.request_adapter, self.path_parameters)

	@property
	def monthly_print_usage_by_user(self,
	) -> MonthlyPrintUsageByUserRequest:
		from .monthly_print_usage_by_user import MonthlyPrintUsageByUserRequest
		return MonthlyPrintUsageByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def partners(self,
	) -> PartnersRequest:
		from .partners import PartnersRequest
		return PartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def security(self,
	) -> SecurityRequest:
		from .security import SecurityRequest
		return SecurityRequest(self.request_adapter, self.path_parameters)

