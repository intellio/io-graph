# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .installation_options import InstallationOptionsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.admin_microsoft365_apps import AdminMicrosoft365Apps
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class Microsoft365AppsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/microsoft365Apps", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AdminMicrosoft365Apps:
		"""
		Get microsoft365Apps from admin
		A container for the Microsoft 365 apps admin functionality.
		"""
		tags = ['admin.adminMicrosoft365Apps']

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
		return await self.request_adapter.send_async(request_info, AdminMicrosoft365Apps, error_mapping)

	async def patch(
		self,
		body: AdminMicrosoft365Apps,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AdminMicrosoft365Apps:
		"""
		Update the navigation property microsoft365Apps in admin
		
		"""
		tags = ['admin.adminMicrosoft365Apps']

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
		return await self.request_adapter.send_async(request_info, AdminMicrosoft365Apps, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property microsoft365Apps for admin
		
		"""
		tags = ['admin.adminMicrosoft365Apps']
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



	def with_url(self, raw_url: str) -> Microsoft365AppsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: Microsoft365AppsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return Microsoft365AppsRequest(self.request_adapter, self.path_parameters)

	@property
	def installation_options(self,
	) -> InstallationOptionsRequest:
		from .installation_options import InstallationOptionsRequest
		return InstallationOptionsRequest(self.request_adapter, self.path_parameters)

