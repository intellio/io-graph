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
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_organization_id import ByOrganizationIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.organization import Organization
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.organization_collection_response import OrganizationCollectionResponse


class OrganizationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/organization", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OrganizationCollectionResponse:
		"""
		List organizations
		Retrieve a list of organization objects. There's only one organization object in the collection.
		Find more info here: https://learn.microsoft.com/graph/api/organization-list?view=graph-rest-1.0
		"""
		tags = ['organization.organization']

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
		return await self.request_adapter.send_async(request_info, OrganizationCollectionResponse, error_mapping)

	async def post(
		self,
		body: Organization,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Organization:
		"""
		Add new entity to organization
		
		"""
		tags = ['organization.organization']

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
		return await self.request_adapter.send_async(request_info, Organization, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> OrganizationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OrganizationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OrganizationRequest(self.request_adapter, self.path_parameters)

	def by_organization_id(self,
		organization_id: str,
	) -> ByOrganizationIdRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .by_organization_id import ByOrganizationIdRequest
		return ByOrganizationIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def delta(self,
	) -> DeltaRequest:
		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, self.path_parameters)

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

