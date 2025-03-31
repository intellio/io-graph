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
	from .retention_labels import RetentionLabelsRequest
	from .file_plan_references import FilePlanReferencesRequest
	from .departments import DepartmentsRequest
	from .citations import CitationsRequest
	from .categories import CategoriesRequest
	from .authorities import AuthoritiesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.security_labels_root import SecurityLabelsRoot
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class LabelsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/labels", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityLabelsRoot:
		"""
		Get labels from security
		
		"""
		tags = ['security.labelsRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityLabelsRoot, error_mapping)

	async def patch(
		self,
		body: SecurityLabelsRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityLabelsRoot:
		"""
		Update the navigation property labels in security
		
		"""
		tags = ['security.labelsRoot']

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
		return await self.request_adapter.send_async(request_info, SecurityLabelsRoot, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property labels for security
		
		"""
		tags = ['security.labelsRoot']
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



	def with_url(self, raw_url: str) -> LabelsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LabelsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LabelsRequest(self.request_adapter, self.path_parameters)

	@property
	def authorities(self,
	) -> AuthoritiesRequest:
		from .authorities import AuthoritiesRequest
		return AuthoritiesRequest(self.request_adapter, self.path_parameters)

	@property
	def categories(self,
	) -> CategoriesRequest:
		from .categories import CategoriesRequest
		return CategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def citations(self,
	) -> CitationsRequest:
		from .citations import CitationsRequest
		return CitationsRequest(self.request_adapter, self.path_parameters)

	@property
	def departments(self,
	) -> DepartmentsRequest:
		from .departments import DepartmentsRequest
		return DepartmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def file_plan_references(self,
	) -> FilePlanReferencesRequest:
		from .file_plan_references import FilePlanReferencesRequest
		return FilePlanReferencesRequest(self.request_adapter, self.path_parameters)

	@property
	def retention_labels(self,
	) -> RetentionLabelsRequest:
		from .retention_labels import RetentionLabelsRequest
		return RetentionLabelsRequest(self.request_adapter, self.path_parameters)

