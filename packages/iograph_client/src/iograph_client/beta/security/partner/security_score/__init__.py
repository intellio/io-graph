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
	from .requirements import RequirementsRequest
	from .history import HistoryRequest
	from .customer_insights import CustomerInsightsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.partner_security_partner_security_score import PartnerSecurityPartnerSecurityScore
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SecurityScoreRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/partner/securityScore", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PartnerSecurityPartnerSecurityScore:
		"""
		Get partnerSecurityScore
		Read the properties and relationships of a partnerSecurityScore object.
		Find more info here: https://learn.microsoft.com/graph/api/partner-security-partnersecurityscore-get?view=graph-rest-beta
		"""
		tags = ['security.partnerSecurity']

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
		return await self.request_adapter.send_async(request_info, PartnerSecurityPartnerSecurityScore, error_mapping)

	async def patch(
		self,
		body: PartnerSecurityPartnerSecurityScore,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PartnerSecurityPartnerSecurityScore:
		"""
		Update the navigation property securityScore in security
		
		"""
		tags = ['security.partnerSecurity']

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
		return await self.request_adapter.send_async(request_info, PartnerSecurityPartnerSecurityScore, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property securityScore for security
		
		"""
		tags = ['security.partnerSecurity']
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



	def with_url(self, raw_url: str) -> SecurityScoreRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SecurityScoreRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SecurityScoreRequest(self.request_adapter, self.path_parameters)

	@property
	def customer_insights(self,
	) -> CustomerInsightsRequest:
		from .customer_insights import CustomerInsightsRequest
		return CustomerInsightsRequest(self.request_adapter, self.path_parameters)

	@property
	def history(self,
	) -> HistoryRequest:
		from .history import HistoryRequest
		return HistoryRequest(self.request_adapter, self.path_parameters)

	@property
	def requirements(self,
	) -> RequirementsRequest:
		from .requirements import RequirementsRequest
		return RequirementsRequest(self.request_adapter, self.path_parameters)

