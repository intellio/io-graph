# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .security_score import SecurityScoreRequest
	from .security_alerts import SecurityAlertsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.partner_security_partner_security import PartnerSecurityPartnerSecurity


class PartnerRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/partner", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PartnerSecurityPartnerSecurity:
		"""
		Get partner from security
		A container that safeguards the Microsoft Azure resources of Microsoft Cloud Solution Provider (CSP) partners’ customers, including alerts, scores, and all aspects of security.
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
		return await self.request_adapter.send_async(request_info, PartnerSecurityPartnerSecurity, error_mapping)

	async def patch(
		self,
		body: PartnerSecurityPartnerSecurity,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PartnerSecurityPartnerSecurity:
		"""
		Update the navigation property partner in security
		
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
		return await self.request_adapter.send_async(request_info, PartnerSecurityPartnerSecurity, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property partner for security
		
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



	def with_url(self, raw_url: str) -> PartnerRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PartnerRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PartnerRequest(self.request_adapter, self.path_parameters)

	@property
	def security_alerts(self,
	) -> SecurityAlertsRequest:
		from .security_alerts import SecurityAlertsRequest
		return SecurityAlertsRequest(self.request_adapter, self.path_parameters)

	@property
	def security_score(self,
	) -> SecurityScoreRequest:
		from .security_score import SecurityScoreRequest
		return SecurityScoreRequest(self.request_adapter, self.path_parameters)

