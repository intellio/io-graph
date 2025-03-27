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
	from .terms_of_use import TermsOfUseRequest
	from .role_management_alerts import RoleManagementAlertsRequest
	from .privileged_access import PrivilegedAccessRequest
	from .permissions_management import PermissionsManagementRequest
	from .permissions_analytics import PermissionsAnalyticsRequest
	from .lifecycle_workflows import LifecycleWorkflowsRequest
	from .entitlement_management import EntitlementManagementRequest
	from .app_consent import AppConsentRequest
	from .access_reviews import AccessReviewsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.identity_governance import IdentityGovernance


class IdentityGovernanceRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityGovernance:
		"""
		Get identityGovernance
		
		"""
		tags = ['identityGovernance.identityGovernance']

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
		return await self.request_adapter.send_async(request_info, IdentityGovernance, error_mapping)

	async def patch(
		self,
		body: IdentityGovernance,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityGovernance:
		"""
		Update identityGovernance
		
		"""
		tags = ['identityGovernance.identityGovernance']

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
		return await self.request_adapter.send_async(request_info, IdentityGovernance, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> IdentityGovernanceRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: IdentityGovernanceRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return IdentityGovernanceRequest(self.request_adapter, self.path_parameters)

	@property
	def access_reviews(self,
	) -> AccessReviewsRequest:
		from .access_reviews import AccessReviewsRequest
		return AccessReviewsRequest(self.request_adapter, self.path_parameters)

	@property
	def app_consent(self,
	) -> AppConsentRequest:
		from .app_consent import AppConsentRequest
		return AppConsentRequest(self.request_adapter, self.path_parameters)

	@property
	def entitlement_management(self,
	) -> EntitlementManagementRequest:
		from .entitlement_management import EntitlementManagementRequest
		return EntitlementManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def lifecycle_workflows(self,
	) -> LifecycleWorkflowsRequest:
		from .lifecycle_workflows import LifecycleWorkflowsRequest
		return LifecycleWorkflowsRequest(self.request_adapter, self.path_parameters)

	@property
	def permissions_analytics(self,
	) -> PermissionsAnalyticsRequest:
		from .permissions_analytics import PermissionsAnalyticsRequest
		return PermissionsAnalyticsRequest(self.request_adapter, self.path_parameters)

	@property
	def permissions_management(self,
	) -> PermissionsManagementRequest:
		from .permissions_management import PermissionsManagementRequest
		return PermissionsManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def privileged_access(self,
	) -> PrivilegedAccessRequest:
		from .privileged_access import PrivilegedAccessRequest
		return PrivilegedAccessRequest(self.request_adapter, self.path_parameters)

	@property
	def role_management_alerts(self,
	) -> RoleManagementAlertsRequest:
		from .role_management_alerts import RoleManagementAlertsRequest
		return RoleManagementAlertsRequest(self.request_adapter, self.path_parameters)

	@property
	def terms_of_use(self,
	) -> TermsOfUseRequest:
		from .terms_of_use import TermsOfUseRequest
		return TermsOfUseRequest(self.request_adapter, self.path_parameters)

