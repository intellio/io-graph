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
	from .file_plan_reference_template import FilePlanReferenceTemplateRequest
	from .department_template import DepartmentTemplateRequest
	from .citation_template import CitationTemplateRequest
	from .category_template import CategoryTemplateRequest
	from .authority_template import AuthorityTemplateRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.security_file_plan_descriptor import SecurityFilePlanDescriptor


class DescriptorsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/labels/retentionLabels/{retentionLabel%2Did}/descriptors", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityFilePlanDescriptor:
		"""
		Get descriptors from security
		Represents out-of-the-box values that provide more options to improve the manageability and organization of the content you need to label.
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
		return await self.request_adapter.send_async(request_info, SecurityFilePlanDescriptor, error_mapping)

	async def patch(
		self,
		body: SecurityFilePlanDescriptor,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityFilePlanDescriptor:
		"""
		Update the navigation property descriptors in security
		
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
		return await self.request_adapter.send_async(request_info, SecurityFilePlanDescriptor, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property descriptors for security
		
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



	def with_url(self, raw_url: str) -> DescriptorsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DescriptorsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DescriptorsRequest(self.request_adapter, self.path_parameters)

	def authority_template(self,
		retentionLabel_id: str,
	) -> AuthorityTemplateRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id

		from .authority_template import AuthorityTemplateRequest
		return AuthorityTemplateRequest(self.request_adapter, path_parameters)

	def category_template(self,
		retentionLabel_id: str,
	) -> CategoryTemplateRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id

		from .category_template import CategoryTemplateRequest
		return CategoryTemplateRequest(self.request_adapter, path_parameters)

	def citation_template(self,
		retentionLabel_id: str,
	) -> CitationTemplateRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id

		from .citation_template import CitationTemplateRequest
		return CitationTemplateRequest(self.request_adapter, path_parameters)

	def department_template(self,
		retentionLabel_id: str,
	) -> DepartmentTemplateRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id

		from .department_template import DepartmentTemplateRequest
		return DepartmentTemplateRequest(self.request_adapter, path_parameters)

	def file_plan_reference_template(self,
		retentionLabel_id: str,
	) -> FilePlanReferenceTemplateRequest:
		if retentionLabel_id is None:
			raise TypeError("retentionLabel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["retentionLabel%2Did"] =  retentionLabel_id

		from .file_plan_reference_template import FilePlanReferenceTemplateRequest
		return FilePlanReferenceTemplateRequest(self.request_adapter, path_parameters)

