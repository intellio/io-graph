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
	from .deactivate import DeactivateRequest
	from .activate import ActivateRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.service_app import ServiceApp


class ByServiceAppIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/serviceApps/{serviceApp%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ServiceApp:
		"""
		Get serviceApp
		Read the properties and relationships of a serviceApp object.
		Find more info here: https://learn.microsoft.com/graph/api/serviceapp-get?view=graph-rest-1.0
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, ServiceApp, error_mapping)

	async def patch(
		self,
		body: ServiceApp,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ServiceApp:
		"""
		Update the navigation property serviceApps in solutions
		
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, ServiceApp, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete serviceApp
		Delete a serviceApp.
		Find more info here: https://learn.microsoft.com/graph/api/backuprestoreroot-delete-serviceapps?view=graph-rest-1.0
		"""
		tags = ['solutions.backupRestoreRoot']
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



	def with_url(self, raw_url: str) -> ByServiceAppIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByServiceAppIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByServiceAppIdRequest(self.request_adapter, self.path_parameters)

	def activate(self,
		serviceApp_id: str,
	) -> ActivateRequest:
		if serviceApp_id is None:
			raise TypeError("serviceApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["serviceApp%2Did"] =  serviceApp_id

		from .activate import ActivateRequest
		return ActivateRequest(self.request_adapter, path_parameters)

	def deactivate(self,
		serviceApp_id: str,
	) -> DeactivateRequest:
		if serviceApp_id is None:
			raise TypeError("serviceApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["serviceApp%2Did"] =  serviceApp_id

		from .deactivate import DeactivateRequest
		return DeactivateRequest(self.request_adapter, path_parameters)

