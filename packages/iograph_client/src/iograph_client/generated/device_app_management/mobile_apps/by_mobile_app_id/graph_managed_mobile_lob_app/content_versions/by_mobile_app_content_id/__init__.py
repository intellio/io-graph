# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .files import FilesRequest
	from .contained_apps import ContainedAppsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.mobile_app_content import MobileAppContent
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByMobileAppContentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileApps/{mobileApp%2Did}/graph.managedMobileLobApp/contentVersions/{mobileAppContent%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MobileAppContent:
		"""
		Get contentVersions from deviceAppManagement
		The list of content versions for this app.
		"""
		tags = ['deviceAppManagement.mobileApp']

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
		return await self.request_adapter.send_async(request_info, MobileAppContent, error_mapping)

	async def patch(
		self,
		body: MobileAppContent,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MobileAppContent:
		"""
		Update the navigation property contentVersions in deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.mobileApp']

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
		return await self.request_adapter.send_async(request_info, MobileAppContent, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property contentVersions for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.mobileApp']
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



	def with_url(self, raw_url: str) -> ByMobileAppContentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMobileAppContentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMobileAppContentIdRequest(self.request_adapter, self.path_parameters)

	def contained_apps(self,
		mobileApp_id: str,
		mobileAppContent_id: str,
	) -> ContainedAppsRequest:
		if mobileApp_id is None:
			raise TypeError("mobileApp_id cannot be null.")
		if mobileAppContent_id is None:
			raise TypeError("mobileAppContent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileApp%2Did"] =  mobileApp_id
		path_parameters["mobileAppContent%2Did"] =  mobileAppContent_id

		from .contained_apps import ContainedAppsRequest
		return ContainedAppsRequest(self.request_adapter, path_parameters)

	def files(self,
		mobileApp_id: str,
		mobileAppContent_id: str,
	) -> FilesRequest:
		if mobileApp_id is None:
			raise TypeError("mobileApp_id cannot be null.")
		if mobileAppContent_id is None:
			raise TypeError("mobileAppContent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileApp%2Did"] =  mobileApp_id
		path_parameters["mobileAppContent%2Did"] =  mobileAppContent_id

		from .files import FilesRequest
		return FilesRequest(self.request_adapter, path_parameters)

