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
	from .service_principal_risk_detections import ServicePrincipalRiskDetectionsRequest
	from .risky_users import RiskyUsersRequest
	from .risky_service_principals import RiskyServicePrincipalsRequest
	from .risk_detections import RiskDetectionsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.identity_protection_root import IdentityProtectionRoot
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class IdentityProtectionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityProtection", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityProtectionRoot:
		"""
		Get identityProtection
		
		"""
		tags = ['identityProtection.identityProtectionRoot']

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
		return await self.request_adapter.send_async(request_info, IdentityProtectionRoot, error_mapping)

	async def patch(
		self,
		body: IdentityProtectionRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityProtectionRoot:
		"""
		Update identityProtection
		
		"""
		tags = ['identityProtection.identityProtectionRoot']

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
		return await self.request_adapter.send_async(request_info, IdentityProtectionRoot, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> IdentityProtectionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: IdentityProtectionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return IdentityProtectionRequest(self.request_adapter, self.path_parameters)

	@property
	def risk_detections(self,
	) -> RiskDetectionsRequest:
		from .risk_detections import RiskDetectionsRequest
		return RiskDetectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def risky_service_principals(self,
	) -> RiskyServicePrincipalsRequest:
		from .risky_service_principals import RiskyServicePrincipalsRequest
		return RiskyServicePrincipalsRequest(self.request_adapter, self.path_parameters)

	@property
	def risky_users(self,
	) -> RiskyUsersRequest:
		from .risky_users import RiskyUsersRequest
		return RiskyUsersRequest(self.request_adapter, self.path_parameters)

	@property
	def service_principal_risk_detections(self,
	) -> ServicePrincipalRiskDetectionsRequest:
		from .service_principal_risk_detections import ServicePrincipalRiskDetectionsRequest
		return ServicePrincipalRiskDetectionsRequest(self.request_adapter, self.path_parameters)

