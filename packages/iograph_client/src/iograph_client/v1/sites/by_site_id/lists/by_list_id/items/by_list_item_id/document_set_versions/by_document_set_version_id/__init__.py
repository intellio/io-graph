# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .restore import RestoreRequest
	from .fields import FieldsRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.v1.document_set_version import DocumentSetVersion
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByDocumentSetVersionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/lists/{list%2Did}/items/{listItem%2Did}/documentSetVersions/{documentSetVersion%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DocumentSetVersion:
		"""
		Get documentSetVersion
		Read the properties and relationships of a documentSetVersion object.
		Find more info here: https://learn.microsoft.com/graph/api/documentsetversion-get?view=graph-rest-1.0
		"""
		tags = ['sites.list']

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
		return await self.request_adapter.send_async(request_info, DocumentSetVersion, error_mapping)

	async def patch(
		self,
		body: DocumentSetVersion,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DocumentSetVersion:
		"""
		Update the navigation property documentSetVersions in sites
		
		"""
		tags = ['sites.list']

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
		return await self.request_adapter.send_async(request_info, DocumentSetVersion, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete documentSetVersion
		Delete a version of a document set in a list.
		Find more info here: https://learn.microsoft.com/graph/api/documentsetversion-delete?view=graph-rest-1.0
		"""
		tags = ['sites.list']
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



	def with_url(self, raw_url: str) -> ByDocumentSetVersionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDocumentSetVersionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDocumentSetVersionIdRequest(self.request_adapter, self.path_parameters)

	def fields(self,
		site_id: str,
		list_id: str,
		listItem_id: str,
		documentSetVersion_id: str,
	) -> FieldsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if documentSetVersion_id is None:
			raise TypeError("documentSetVersion_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["documentSetVersion%2Did"] =  documentSetVersion_id

		from .fields import FieldsRequest
		return FieldsRequest(self.request_adapter, path_parameters)

	def restore(self,
		site_id: str,
		list_id: str,
		listItem_id: str,
		documentSetVersion_id: str,
	) -> RestoreRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if documentSetVersion_id is None:
			raise TypeError("documentSetVersion_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["documentSetVersion%2Did"] =  documentSetVersion_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

