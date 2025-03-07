# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .schema import SchemaRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.synchronization_template import SynchronizationTemplate
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class BySynchronizationTemplateIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/synchronization/templates/{synchronizationTemplate%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SynchronizationTemplate:
		"""
		Get templates from applications
		Preconfigured synchronization settings for a particular application.
		"""
		tags = ['applications.synchronization']

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
		return await self.request_adapter.send_async(request_info, SynchronizationTemplate, error_mapping)

	async def patch(
		self,
		body: SynchronizationTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SynchronizationTemplate:
		"""
		Update synchronizationTemplate
		Update (override) the synchronization template associated with a given application.
		Find more info here: https://learn.microsoft.com/graph/api/synchronization-synchronizationtemplate-update?view=graph-rest-1.0
		"""
		tags = ['applications.synchronization']

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
		return await self.request_adapter.send_async(request_info, SynchronizationTemplate, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property templates for applications
		
		"""
		tags = ['applications.synchronization']
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



	def with_url(self, raw_url: str) -> BySynchronizationTemplateIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySynchronizationTemplateIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySynchronizationTemplateIdRequest(self.request_adapter, self.path_parameters)

	def schema(self,
		application_id: str,
		synchronizationTemplate_id: str,
	) -> SchemaRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if synchronizationTemplate_id is None:
			raise TypeError("synchronizationTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["synchronizationTemplate%2Did"] =  synchronizationTemplate_id

		from .schema import SchemaRequest
		return SchemaRequest(self.request_adapter, path_parameters)

