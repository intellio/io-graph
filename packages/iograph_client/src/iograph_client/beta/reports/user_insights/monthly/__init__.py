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
	from .summary import SummaryRequest
	from .sign_ups import SignUpsRequest
	from .requests import RequestsRequest
	from .mfa_registered_users import MfaRegisteredUsersRequest
	from .mfa_completions import MfaCompletionsRequest
	from .inactive_users_by_application import InactiveUsersByApplicationRequest
	from .inactive_users import InactiveUsersRequest
	from .authentications import AuthenticationsRequest
	from .active_users import ActiveUsersRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class MonthlyRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/reports/userInsights/monthly", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MonthlyUserInsightMetricsRoot:
		"""
		Get monthly from reports
		Summaries of monthly user activities on apps registered in your tenant that is configured for Microsoft Entra External ID for customers.
		"""
		tags = ['reports.userInsightsRoot']

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
		return await self.request_adapter.send_async(request_info, MonthlyUserInsightMetricsRoot, error_mapping)

	async def patch(
		self,
		body: MonthlyUserInsightMetricsRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MonthlyUserInsightMetricsRoot:
		"""
		Update the navigation property monthly in reports
		
		"""
		tags = ['reports.userInsightsRoot']

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
		return await self.request_adapter.send_async(request_info, MonthlyUserInsightMetricsRoot, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property monthly for reports
		
		"""
		tags = ['reports.userInsightsRoot']
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



	def with_url(self, raw_url: str) -> MonthlyRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MonthlyRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MonthlyRequest(self.request_adapter, self.path_parameters)

	@property
	def active_users(self,
	) -> ActiveUsersRequest:
		from .active_users import ActiveUsersRequest
		return ActiveUsersRequest(self.request_adapter, self.path_parameters)

	@property
	def authentications(self,
	) -> AuthenticationsRequest:
		from .authentications import AuthenticationsRequest
		return AuthenticationsRequest(self.request_adapter, self.path_parameters)

	@property
	def inactive_users(self,
	) -> InactiveUsersRequest:
		from .inactive_users import InactiveUsersRequest
		return InactiveUsersRequest(self.request_adapter, self.path_parameters)

	@property
	def inactive_users_by_application(self,
	) -> InactiveUsersByApplicationRequest:
		from .inactive_users_by_application import InactiveUsersByApplicationRequest
		return InactiveUsersByApplicationRequest(self.request_adapter, self.path_parameters)

	@property
	def mfa_completions(self,
	) -> MfaCompletionsRequest:
		from .mfa_completions import MfaCompletionsRequest
		return MfaCompletionsRequest(self.request_adapter, self.path_parameters)

	@property
	def mfa_registered_users(self,
	) -> MfaRegisteredUsersRequest:
		from .mfa_registered_users import MfaRegisteredUsersRequest
		return MfaRegisteredUsersRequest(self.request_adapter, self.path_parameters)

	@property
	def requests(self,
	) -> RequestsRequest:
		from .requests import RequestsRequest
		return RequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def sign_ups(self,
	) -> SignUpsRequest:
		from .sign_ups import SignUpsRequest
		return SignUpsRequest(self.request_adapter, self.path_parameters)

	@property
	def summary(self,
	) -> SummaryRequest:
		from .summary import SummaryRequest
		return SummaryRequest(self.request_adapter, self.path_parameters)

