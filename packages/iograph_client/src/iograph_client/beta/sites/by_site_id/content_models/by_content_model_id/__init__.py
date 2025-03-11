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
	from .remove_from_drive import RemoveFromDriveRequest
	from .get_applied_drives import GetAppliedDrivesRequest
	from .add_to_drive import AddToDriveRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.content_model import ContentModel
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByContentModelIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/contentModels/{contentModel%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContentModel:
		"""
		Get contentModel
		Read the properties and relationships of a contentModel object.
		Find more info here: https://learn.microsoft.com/graph/api/contentmodel-get?view=graph-rest-beta
		"""
		tags = ['sites.contentModel']

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
		return await self.request_adapter.send_async(request_info, ContentModel, error_mapping)

	async def patch(
		self,
		body: ContentModel,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ContentModel:
		"""
		Update the navigation property contentModels in sites
		
		"""
		tags = ['sites.contentModel']

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
		return await self.request_adapter.send_async(request_info, ContentModel, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property contentModels for sites
		
		"""
		tags = ['sites.contentModel']
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



	def with_url(self, raw_url: str) -> ByContentModelIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByContentModelIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByContentModelIdRequest(self.request_adapter, self.path_parameters)

	def add_to_drive(self,
		site_id: str,
		contentModel_id: str,
	) -> AddToDriveRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentModel_id is None:
			raise TypeError("contentModel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentModel%2Did"] =  contentModel_id

		from .add_to_drive import AddToDriveRequest
		return AddToDriveRequest(self.request_adapter, path_parameters)

	def get_applied_drives(self,
		site_id: str,
		contentModel_id: str,
	) -> GetAppliedDrivesRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentModel_id is None:
			raise TypeError("contentModel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentModel%2Did"] =  contentModel_id

		from .get_applied_drives import GetAppliedDrivesRequest
		return GetAppliedDrivesRequest(self.request_adapter, path_parameters)

	def remove_from_drive(self,
		site_id: str,
		contentModel_id: str,
	) -> RemoveFromDriveRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentModel_id is None:
			raise TypeError("contentModel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentModel%2Did"] =  contentModel_id

		from .remove_from_drive import RemoveFromDriveRequest
		return RemoveFromDriveRequest(self.request_adapter, path_parameters)

