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
	from .count import CountRequest
	from .by_site_restore_artifacts_bulk_addition_request_id import BySiteRestoreArtifactsBulkAdditionRequestIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest
from iograph_models.beta.site_restore_artifacts_bulk_addition_request_collection_response import SiteRestoreArtifactsBulkAdditionRequestCollectionResponse


class SiteRestoreArtifactsBulkAdditionRequestsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/sharePointRestoreSessions/{sharePointRestoreSession%2Did}/siteRestoreArtifactsBulkAdditionRequests", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SiteRestoreArtifactsBulkAdditionRequestCollectionResponse:
		"""
		List siteRestoreArtifactsBulkAdditionRequests
		Get a list of the siteRestoreArtifactsBulkAdditionRequest objects associated with a sharePointRestoreSession. The siteWebUrls property is deliberately omitted from the response body in order to limit the response size.
		Find more info here: https://learn.microsoft.com/graph/api/sharepointrestoresession-list-siterestoreartifactsbulkadditionrequests?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, SiteRestoreArtifactsBulkAdditionRequestCollectionResponse, error_mapping)

	async def post(
		self,
		body: SiteRestoreArtifactsBulkAdditionRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SiteRestoreArtifactsBulkAdditionRequest:
		"""
		Create siteRestoreArtifactsBulkAdditionRequests
		Create a new siteRestoreArtifactsBulkAdditionRequest object associated with a sharePointRestoreSession. The following steps describe how to create and manage a sharePointRestoreSession with bulk artifact additions:
		Find more info here: https://learn.microsoft.com/graph/api/sharepointrestoresession-post-siterestoreartifactsbulkadditionrequests?view=graph-rest-beta
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, SiteRestoreArtifactsBulkAdditionRequest, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SiteRestoreArtifactsBulkAdditionRequestsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SiteRestoreArtifactsBulkAdditionRequestsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SiteRestoreArtifactsBulkAdditionRequestsRequest(self.request_adapter, self.path_parameters)

	def by_site_restore_artifacts_bulk_addition_request_id(self,
		sharePointRestoreSession_id: str,
		siteRestoreArtifactsBulkAdditionRequest_id: str,
	) -> BySiteRestoreArtifactsBulkAdditionRequestIdRequest:
		if sharePointRestoreSession_id is None:
			raise TypeError("sharePointRestoreSession_id cannot be null.")
		if siteRestoreArtifactsBulkAdditionRequest_id is None:
			raise TypeError("siteRestoreArtifactsBulkAdditionRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharePointRestoreSession%2Did"] =  sharePointRestoreSession_id
		path_parameters["siteRestoreArtifactsBulkAdditionRequest%2Did"] =  siteRestoreArtifactsBulkAdditionRequest_id

		from .by_site_restore_artifacts_bulk_addition_request_id import BySiteRestoreArtifactsBulkAdditionRequestIdRequest
		return BySiteRestoreArtifactsBulkAdditionRequestIdRequest(self.request_adapter, path_parameters)

	def count(self,
		sharePointRestoreSession_id: str,
	) -> CountRequest:
		if sharePointRestoreSession_id is None:
			raise TypeError("sharePointRestoreSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharePointRestoreSession%2Did"] =  sharePointRestoreSession_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

