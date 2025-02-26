# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_federated_identity_credential_id import ByFederatedIdentityCredentialIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.federated_identity_credential import FederatedIdentityCredential
from iograph_models.models.federated_identity_credential_collection_response import FederatedIdentityCredentialCollectionResponse


class FederatedIdentityCredentialsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/federatedIdentityCredentials"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> FederatedIdentityCredentialCollectionResponse:
		"""
		Get federatedIdentityCredentials from servicePrincipals
		Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).
		"""
		tags = ['servicePrincipals.federatedIdentityCredential']

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
		return await self.request_adapter.send_async(request_info, FederatedIdentityCredentialCollectionResponse, error_mapping)

	async def post(
		self,
		body: FederatedIdentityCredential,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> FederatedIdentityCredential:
		"""
		Create new navigation property to federatedIdentityCredentials for servicePrincipals
		
		"""
		tags = ['servicePrincipals.federatedIdentityCredential']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, FederatedIdentityCredential, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_federated_identity_credential_id(self,
		servicePrincipal_id: str,
		federatedIdentityCredential_id: str,
	) -> ByFederatedIdentityCredentialIdRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if federatedIdentityCredential_id is None:
			raise TypeError("federatedIdentityCredential_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["federatedIdentityCredential%2Did"] =  federatedIdentityCredential_id

		from .by_federated_identity_credential_id import ByFederatedIdentityCredentialIdRequest
		return ByFederatedIdentityCredentialIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

