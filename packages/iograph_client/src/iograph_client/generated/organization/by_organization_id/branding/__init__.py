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
	from .square_logo_dark import SquareLogoDarkRequest
	from .square_logo import SquareLogoRequest
	from .localizations import LocalizationsRequest
	from .header_logo import HeaderLogoRequest
	from .favicon import FaviconRequest
	from .custom_c_s_s import CustomCSSRequest
	from .banner_logo import BannerLogoRequest
	from .background_image import BackgroundImageRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.organizational_branding import OrganizationalBranding
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class BrandingRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}/branding", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OrganizationalBranding:
		"""
		Get organizationalBranding
		Retrieve the default organizational branding object, if the Accept-Language header is set to 0 or default. If no default organizational branding object exists, this method returns a 404 Not Found error. If the Accept-Language header is set to an existing locale identified by the value of its id, this method retrieves the branding for the specified locale. This method retrieves only non-Stream properties, for example, usernameHintText and signInPageText. To retrieve Stream types of the default branding, for example, bannerLogo and backgroundImage, use the GET organizationalBrandingLocalization method.
		Find more info here: https://learn.microsoft.com/graph/api/organizationalbranding-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, OrganizationalBranding, error_mapping)

	async def patch(
		self,
		body: OrganizationalBranding,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OrganizationalBranding:
		"""
		Update organizationalBranding
		Update the properties of the default branding object specified by the organizationalBranding resource.
		Find more info here: https://learn.microsoft.com/graph/api/organizationalbranding-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, OrganizationalBranding, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete organizationalBranding
		Delete the default organizational branding object. To delete the organizationalBranding object, all images (Stream types) must first be removed from the object.
		Find more info here: https://learn.microsoft.com/graph/api/organizationalbranding-delete?view=graph-rest-1.0
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



	def with_url(self, raw_url: str) -> BrandingRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BrandingRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BrandingRequest(self.request_adapter, self.path_parameters)

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
	def localizations(self,
	) -> LocalizationsRequest:
		from .localizations import LocalizationsRequest
		return LocalizationsRequest(self.request_adapter, self.path_parameters)

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

