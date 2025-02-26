# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_document_set_version_id import ByDocumentSetVersionIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.document_set_version_collection_response import DocumentSetVersionCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.document_set_version import DocumentSetVersion


class DocumentSetVersionsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/list/items/{listItem%2Did}/documentSetVersions"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DocumentSetVersionCollectionResponse:
		"""
		Get documentSetVersions from drives
		Version information for a document set version created by a user.
		"""
		tags = ['drives.list']

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
		return await self.request_adapter.send_async(request_info, DocumentSetVersionCollectionResponse, error_mapping)

	async def post(
		self,
		body: DocumentSetVersion,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DocumentSetVersion:
		"""
		Create new navigation property to documentSetVersions for drives
		
		"""
		tags = ['drives.list']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, DocumentSetVersion, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_document_set_version_id(self,
		drive_id: str,
		listItem_id: str,
		documentSetVersion_id: str,
	) -> ByDocumentSetVersionIdRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if documentSetVersion_id is None:
			raise TypeError("documentSetVersion_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["documentSetVersion%2Did"] =  documentSetVersion_id

		from .by_document_set_version_id import ByDocumentSetVersionIdRequest
		return ByDocumentSetVersionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

