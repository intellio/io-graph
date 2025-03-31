# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .instantiate import InstantiateRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.application_template import ApplicationTemplate
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByApplicationTemplateIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applicationTemplates/{applicationTemplate%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ApplicationTemplate:
		"""
		Get applicationTemplate
		Retrieve the properties of an applicationTemplate object.
		Find more info here: https://learn.microsoft.com/graph/api/applicationtemplate-get?view=graph-rest-1.0
		"""
		tags = ['applicationTemplates.applicationTemplate']

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
		return await self.request_adapter.send_async(request_info, ApplicationTemplate, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByApplicationTemplateIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByApplicationTemplateIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByApplicationTemplateIdRequest(self.request_adapter, self.path_parameters)

	def instantiate(self,
		applicationTemplate_id: str,
	) -> InstantiateRequest:
		if applicationTemplate_id is None:
			raise TypeError("applicationTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["applicationTemplate%2Did"] =  applicationTemplate_id

		from .instantiate import InstantiateRequest
		return InstantiateRequest(self.request_adapter, path_parameters)

