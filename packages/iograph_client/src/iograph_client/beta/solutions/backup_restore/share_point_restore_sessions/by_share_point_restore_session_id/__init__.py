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
	from .site_restore_artifacts_bulk_addition_requests import SiteRestoreArtifactsBulkAdditionRequestsRequest
	from .site_restore_artifacts import SiteRestoreArtifactsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.share_point_restore_session import SharePointRestoreSession


class BySharePointRestoreSessionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/sharePointRestoreSessions/{sharePointRestoreSession%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SharePointRestoreSession:
		"""
		Get sharePointRestoreSessions from solutions
		The list of SharePoint restore sessions available in the tenant.
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
		return await self.request_adapter.send_async(request_info, SharePointRestoreSession, error_mapping)

	async def patch(
		self,
		body: SharePointRestoreSession,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SharePointRestoreSession:
		"""
		Update the navigation property sharePointRestoreSessions in solutions
		
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
		return await self.request_adapter.send_async(request_info, SharePointRestoreSession, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property sharePointRestoreSessions for solutions
		
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



	def with_url(self, raw_url: str) -> BySharePointRestoreSessionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySharePointRestoreSessionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySharePointRestoreSessionIdRequest(self.request_adapter, self.path_parameters)

	def site_restore_artifacts(self,
		sharePointRestoreSession_id: str,
	) -> SiteRestoreArtifactsRequest:
		if sharePointRestoreSession_id is None:
			raise TypeError("sharePointRestoreSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharePointRestoreSession%2Did"] =  sharePointRestoreSession_id

		from .site_restore_artifacts import SiteRestoreArtifactsRequest
		return SiteRestoreArtifactsRequest(self.request_adapter, path_parameters)

	def site_restore_artifacts_bulk_addition_requests(self,
		sharePointRestoreSession_id: str,
	) -> SiteRestoreArtifactsBulkAdditionRequestsRequest:
		if sharePointRestoreSession_id is None:
			raise TypeError("sharePointRestoreSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharePointRestoreSession%2Did"] =  sharePointRestoreSession_id

		from .site_restore_artifacts_bulk_addition_requests import SiteRestoreArtifactsBulkAdditionRequestsRequest
		return SiteRestoreArtifactsBulkAdditionRequestsRequest(self.request_adapter, path_parameters)

