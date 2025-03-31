# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .templates import TemplatesRequest
	from .subscriptions_with_ocpsubscriptionid import SubscriptionsWithOcpSubscriptionIdRequest
	from .subscriptions_with_commercesubscriptionid import SubscriptionsWithCommerceSubscriptionIdRequest
	from .subscriptions import SubscriptionsRequest
	from .shared_email_domains import SharedEmailDomainsRequest
	from .recommendations import RecommendationsRequest
	from .public_key_infrastructure import PublicKeyInfrastructureRequest
	from .pending_external_user_profiles import PendingExternalUserProfilesRequest
	from .outbound_shared_user_profiles import OutboundSharedUserProfilesRequest
	from .on_premises_synchronization import OnPremisesSynchronizationRequest
	from .inbound_shared_user_profiles import InboundSharedUserProfilesRequest
	from .impacted_resources import ImpactedResourcesRequest
	from .federation_configurations import FederationConfigurationsRequest
	from .feature_rollout_policies import FeatureRolloutPoliciesRequest
	from .external_user_profiles import ExternalUserProfilesRequest
	from .device_local_credentials import DeviceLocalCredentialsRequest
	from .deleted_items import DeletedItemsRequest
	from .custom_security_attribute_definitions import CustomSecurityAttributeDefinitionsRequest
	from .certificate_authorities import CertificateAuthoritiesRequest
	from .authentication_method_devices import AuthenticationMethodDevicesRequest
	from .attribute_sets import AttributeSetsRequest
	from .administrative_units import AdministrativeUnitsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.directory import Directory
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DirectoryRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Directory:
		"""
		Get directory
		
		"""
		tags = ['directory.directory']

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
		return await self.request_adapter.send_async(request_info, Directory, error_mapping)

	async def patch(
		self,
		body: Directory,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Directory:
		"""
		Update directory
		
		"""
		tags = ['directory.directory']

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
		return await self.request_adapter.send_async(request_info, Directory, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DirectoryRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DirectoryRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DirectoryRequest(self.request_adapter, self.path_parameters)

	@property
	def administrative_units(self,
	) -> AdministrativeUnitsRequest:
		from .administrative_units import AdministrativeUnitsRequest
		return AdministrativeUnitsRequest(self.request_adapter, self.path_parameters)

	@property
	def attribute_sets(self,
	) -> AttributeSetsRequest:
		from .attribute_sets import AttributeSetsRequest
		return AttributeSetsRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_method_devices(self,
	) -> AuthenticationMethodDevicesRequest:
		from .authentication_method_devices import AuthenticationMethodDevicesRequest
		return AuthenticationMethodDevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def certificate_authorities(self,
	) -> CertificateAuthoritiesRequest:
		from .certificate_authorities import CertificateAuthoritiesRequest
		return CertificateAuthoritiesRequest(self.request_adapter, self.path_parameters)

	@property
	def custom_security_attribute_definitions(self,
	) -> CustomSecurityAttributeDefinitionsRequest:
		from .custom_security_attribute_definitions import CustomSecurityAttributeDefinitionsRequest
		return CustomSecurityAttributeDefinitionsRequest(self.request_adapter, self.path_parameters)

	@property
	def deleted_items(self,
	) -> DeletedItemsRequest:
		from .deleted_items import DeletedItemsRequest
		return DeletedItemsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_local_credentials(self,
	) -> DeviceLocalCredentialsRequest:
		from .device_local_credentials import DeviceLocalCredentialsRequest
		return DeviceLocalCredentialsRequest(self.request_adapter, self.path_parameters)

	@property
	def external_user_profiles(self,
	) -> ExternalUserProfilesRequest:
		from .external_user_profiles import ExternalUserProfilesRequest
		return ExternalUserProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def feature_rollout_policies(self,
	) -> FeatureRolloutPoliciesRequest:
		from .feature_rollout_policies import FeatureRolloutPoliciesRequest
		return FeatureRolloutPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def federation_configurations(self,
	) -> FederationConfigurationsRequest:
		from .federation_configurations import FederationConfigurationsRequest
		return FederationConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def impacted_resources(self,
	) -> ImpactedResourcesRequest:
		from .impacted_resources import ImpactedResourcesRequest
		return ImpactedResourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def inbound_shared_user_profiles(self,
	) -> InboundSharedUserProfilesRequest:
		from .inbound_shared_user_profiles import InboundSharedUserProfilesRequest
		return InboundSharedUserProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def on_premises_synchronization(self,
	) -> OnPremisesSynchronizationRequest:
		from .on_premises_synchronization import OnPremisesSynchronizationRequest
		return OnPremisesSynchronizationRequest(self.request_adapter, self.path_parameters)

	@property
	def outbound_shared_user_profiles(self,
	) -> OutboundSharedUserProfilesRequest:
		from .outbound_shared_user_profiles import OutboundSharedUserProfilesRequest
		return OutboundSharedUserProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def pending_external_user_profiles(self,
	) -> PendingExternalUserProfilesRequest:
		from .pending_external_user_profiles import PendingExternalUserProfilesRequest
		return PendingExternalUserProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def public_key_infrastructure(self,
	) -> PublicKeyInfrastructureRequest:
		from .public_key_infrastructure import PublicKeyInfrastructureRequest
		return PublicKeyInfrastructureRequest(self.request_adapter, self.path_parameters)

	@property
	def recommendations(self,
	) -> RecommendationsRequest:
		from .recommendations import RecommendationsRequest
		return RecommendationsRequest(self.request_adapter, self.path_parameters)

	@property
	def shared_email_domains(self,
	) -> SharedEmailDomainsRequest:
		from .shared_email_domains import SharedEmailDomainsRequest
		return SharedEmailDomainsRequest(self.request_adapter, self.path_parameters)

	@property
	def subscriptions(self,
	) -> SubscriptionsRequest:
		from .subscriptions import SubscriptionsRequest
		return SubscriptionsRequest(self.request_adapter, self.path_parameters)

	def subscriptions_with_commercesubscriptionid(self,
		commerceSubscriptionId: str,
	) -> SubscriptionsWithCommerceSubscriptionIdRequest:
		if commerceSubscriptionId is None:
			raise TypeError("commerceSubscriptionId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["commerceSubscriptionId"] =  commerceSubscriptionId

		from .subscriptions_with_commercesubscriptionid import SubscriptionsWithCommerceSubscriptionIdRequest
		return SubscriptionsWithCommerceSubscriptionIdRequest(self.request_adapter, path_parameters)

	def subscriptions_with_ocpsubscriptionid(self,
		ocpSubscriptionId: str,
	) -> SubscriptionsWithOcpSubscriptionIdRequest:
		if ocpSubscriptionId is None:
			raise TypeError("ocpSubscriptionId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["ocpSubscriptionId"] =  ocpSubscriptionId

		from .subscriptions_with_ocpsubscriptionid import SubscriptionsWithOcpSubscriptionIdRequest
		return SubscriptionsWithOcpSubscriptionIdRequest(self.request_adapter, path_parameters)

	@property
	def templates(self,
	) -> TemplatesRequest:
		from .templates import TemplatesRequest
		return TemplatesRequest(self.request_adapter, self.path_parameters)

