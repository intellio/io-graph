# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .square_logo_dark import SquareLogoDarkRequest
	from .square_logo import SquareLogoRequest
	from .header_logo import HeaderLogoRequest
	from .favicon import FaviconRequest
	from .custom_c_s_s import CustomCSSRequest
	from .banner_logo import BannerLogoRequest
	from .background_image import BackgroundImageRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.organizational_branding_localization import OrganizationalBrandingLocalization
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByOrganizationalBrandingLocalizationIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/organization/{organization%2Did}/branding/localizations/{organizationalBrandingLocalization%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OrganizationalBrandingLocalization:
		"""
		Get organizationalBrandingLocalization
		Read the properties and relationships of an organizationalBrandingLocalization object. To retrieve a localization branding object, specify the value of id in the URL.
		Find more info here: https://learn.microsoft.com/graph/api/organizationalbrandinglocalization-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, OrganizationalBrandingLocalization, error_mapping)

	async def patch(
		self,
		body: OrganizationalBrandingLocalization,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OrganizationalBrandingLocalization:
		"""
		Update organizationalBrandingLocalization
		Update the properties of an organizationalBrandingLocalization object for a specific localization.
		Find more info here: https://learn.microsoft.com/graph/api/organizationalbrandinglocalization-update?view=graph-rest-1.0
		"""
		tags = ['organization.organizationalBranding']

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
		return await self.request_adapter.send_async(request_info, OrganizationalBrandingLocalization, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete organizationalBrandingLocalization
		Delete a localized branding object. To delete the organizationalBrandingLocalization object, all images (Stream types) must first be removed from the object.
		Find more info here: https://learn.microsoft.com/graph/api/organizationalbrandinglocalization-delete?view=graph-rest-1.0
		"""
		tags = ['organization.organizationalBranding']
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



	@property
	def background_image(self,
	) -> BackgroundImageRequest:
		from .background_image import BackgroundImageRequest
		return BackgroundImageRequest(self.request_adapter, self.path_parameters)

	@property
	def banner_logo(self,
	) -> BannerLogoRequest:
		from .banner_logo import BannerLogoRequest
		return BannerLogoRequest(self.request_adapter, self.path_parameters)

	@property
	def custom_c_s_s(self,
	) -> CustomCSSRequest:
		from .custom_c_s_s import CustomCSSRequest
		return CustomCSSRequest(self.request_adapter, self.path_parameters)

	@property
	def favicon(self,
	) -> FaviconRequest:
		from .favicon import FaviconRequest
		return FaviconRequest(self.request_adapter, self.path_parameters)

	@property
	def header_logo(self,
	) -> HeaderLogoRequest:
		from .header_logo import HeaderLogoRequest
		return HeaderLogoRequest(self.request_adapter, self.path_parameters)

	@property
	def square_logo(self,
	) -> SquareLogoRequest:
		from .square_logo import SquareLogoRequest
		return SquareLogoRequest(self.request_adapter, self.path_parameters)

	@property
	def square_logo_dark(self,
	) -> SquareLogoDarkRequest:
		from .square_logo_dark import SquareLogoDarkRequest
		return SquareLogoDarkRequest(self.request_adapter, self.path_parameters)

