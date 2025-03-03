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
	from .validate_properties import ValidatePropertiesRequest
	from .get_by_ids import GetByIdsRequest
	from .get_available_extension_properties import GetAvailableExtensionPropertiesRequest
	from .count import CountRequest
	from .by_service_principal_id import ByServicePrincipalIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.service_principal import ServicePrincipal
from iograph_models.models.service_principal_collection_response import ServicePrincipalCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ServicePrincipalsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ServicePrincipalCollectionResponse:
		"""
		List servicePrincipals
		Retrieve a list of servicePrincipal objects.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-list?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.servicePrincipal']
		header_parameters = [{'name': 'ConsistencyLevel', 'in': 'header', 'description': 'Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries', 'schema': {'type': 'string'}, 'examples': {'example-1': {'description': "$search and $count queries require the client to set the ConsistencyLevel HTTP header to 'eventual'.", 'value': 'eventual'}}}]

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
		return await self.request_adapter.send_async(request_info, ServicePrincipalCollectionResponse, error_mapping)

	async def post(
		self,
		body: ServicePrincipal,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ServicePrincipal:
		"""
		Create servicePrincipal
		Create a new servicePrincipal object.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-post-serviceprincipals?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.servicePrincipal']

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
		return await self.request_adapter.send_async(request_info, ServicePrincipal, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ServicePrincipalsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ServicePrincipalsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ServicePrincipalsRequest(self.request_adapter, self.path_parameters)

	def by_service_principal_id(self,
		servicePrincipal_id: str,
	) -> ByServicePrincipalIdRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .by_service_principal_id import ByServicePrincipalIdRequest
		return ByServicePrincipalIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def get_available_extension_properties(self,
	) -> GetAvailableExtensionPropertiesRequest:
		from .get_available_extension_properties import GetAvailableExtensionPropertiesRequest
		return GetAvailableExtensionPropertiesRequest(self.request_adapter, self.path_parameters)

	@property
	def get_by_ids(self,
	) -> GetByIdsRequest:
		from .get_by_ids import GetByIdsRequest
		return GetByIdsRequest(self.request_adapter, self.path_parameters)

	@property
	def validate_properties(self,
	) -> ValidatePropertiesRequest:
		from .validate_properties import ValidatePropertiesRequest
		return ValidatePropertiesRequest(self.request_adapter, self.path_parameters)

