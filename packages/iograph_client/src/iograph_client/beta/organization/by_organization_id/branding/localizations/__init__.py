# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_organizational_branding_localization_id import ByOrganizationalBrandingLocalizationIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.organizational_branding_localization import OrganizationalBrandingLocalization
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.organizational_branding_localization_collection_response import OrganizationalBrandingLocalizationCollectionResponse


class LocalizationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}/branding/localizations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OrganizationalBrandingLocalizationCollectionResponse:
		"""
		List localizations
		Retrieve all localization branding objects, including the default branding.
		Find more info here: https://learn.microsoft.com/graph/api/organizationalbranding-list-localizations?view=graph-rest-beta
		"""
		tags = ['organization.organizationalBranding']

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
		return await self.request_adapter.send_async(request_info, OrganizationalBrandingLocalizationCollectionResponse, error_mapping)

	async def post(
		self,
		body: OrganizationalBrandingLocalization,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OrganizationalBrandingLocalization:
		"""
		Create organizationalBrandingLocalization
		Create a new organizationalBrandingLocalization object. This creates a localized branding and at the same time, the default branding if it doesn't exist. The default branding is created only once. It's loaded when a localized branding isn't configured for the user's browser language. To retrieve the default branding, see Get branding.
		Find more info here: https://learn.microsoft.com/graph/api/organizationalbranding-post-localizations?view=graph-rest-beta
		"""
		tags = ['organization.organizationalBranding']

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
		return await self.request_adapter.send_async(request_info, OrganizationalBrandingLocalization, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> LocalizationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LocalizationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LocalizationsRequest(self.request_adapter, self.path_parameters)

	def by_organizational_branding_localization_id(self,
		organization_id: str,
		organizationalBrandingLocalization_id: str,
	) -> ByOrganizationalBrandingLocalizationIdRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")
		if organizationalBrandingLocalization_id is None:
			raise TypeError("organizationalBrandingLocalization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id
		path_parameters["organizationalBrandingLocalization%2Did"] =  organizationalBrandingLocalization_id

		from .by_organizational_branding_localization_id import ByOrganizationalBrandingLocalizationIdRequest
		return ByOrganizationalBrandingLocalizationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		organization_id: str,
	) -> CountRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

