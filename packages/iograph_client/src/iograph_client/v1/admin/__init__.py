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
	from .sharepoint import SharepointRequest
	from .service_announcement import ServiceAnnouncementRequest
	from .report_settings import ReportSettingsRequest
	from .people import PeopleRequest
	from .microsoft365_apps import Microsoft365AppsRequest
	from .edge import EdgeRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.admin import Admin


class AdminRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Admin:
		"""
		Get admin
		
		"""
		tags = ['admin.admin']

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
		return await self.request_adapter.send_async(request_info, Admin, error_mapping)

	async def patch(
		self,
		body: Admin,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Admin:
		"""
		Update admin
		
		"""
		tags = ['admin.admin']

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
		return await self.request_adapter.send_async(request_info, Admin, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AdminRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AdminRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AdminRequest(self.request_adapter, self.path_parameters)

	@property
	def edge(self,
	) -> EdgeRequest:
		from .edge import EdgeRequest
		return EdgeRequest(self.request_adapter, self.path_parameters)

	@property
	def microsoft365_apps(self,
	) -> Microsoft365AppsRequest:
		from .microsoft365_apps import Microsoft365AppsRequest
		return Microsoft365AppsRequest(self.request_adapter, self.path_parameters)

	@property
	def people(self,
	) -> PeopleRequest:
		from .people import PeopleRequest
		return PeopleRequest(self.request_adapter, self.path_parameters)

	@property
	def report_settings(self,
	) -> ReportSettingsRequest:
		from .report_settings import ReportSettingsRequest
		return ReportSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def service_announcement(self,
	) -> ServiceAnnouncementRequest:
		from .service_announcement import ServiceAnnouncementRequest
		return ServiceAnnouncementRequest(self.request_adapter, self.path_parameters)

	@property
	def sharepoint(self,
	) -> SharepointRequest:
		from .sharepoint import SharepointRequest
		return SharepointRequest(self.request_adapter, self.path_parameters)

