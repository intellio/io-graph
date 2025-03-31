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
	from .by_drive_restore_artifacts_bulk_addition_request_id import ByDriveRestoreArtifactsBulkAdditionRequestIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.drive_restore_artifacts_bulk_addition_request_collection_response import DriveRestoreArtifactsBulkAdditionRequestCollectionResponse
from iograph_models.beta.drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DriveRestoreArtifactsBulkAdditionRequestsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/oneDriveForBusinessRestoreSessions/{oneDriveForBusinessRestoreSession%2Did}/driveRestoreArtifactsBulkAdditionRequests", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DriveRestoreArtifactsBulkAdditionRequestCollectionResponse:
		"""
		List driveRestoreArtifactsBulkAdditionRequests
		Get a list of the driveRestoreArtifactsBulkAdditionRequest objects associated with a oneDriveForBusinessRestoreSession. The drives property is deliberately omitted from the response body in order to limit the response size.
		Find more info here: https://learn.microsoft.com/graph/api/onedriveforbusinessrestoresession-list-driverestoreartifactsbulkadditionrequests?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, DriveRestoreArtifactsBulkAdditionRequestCollectionResponse, error_mapping)

	async def post(
		self,
		body: DriveRestoreArtifactsBulkAdditionRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DriveRestoreArtifactsBulkAdditionRequest:
		"""
		Create driveRestoreArtifactsBulkAdditionRequest
		Create a driveRestoreArtifactsBulkAdditionRequest object associated with a oneDriveForBusinessRestoreSession. The following steps describe how to create and manage a oneDriveForBusinessRestoreSession with bulk artifact additions.
		Find more info here: https://learn.microsoft.com/graph/api/onedriveforbusinessrestoresession-post-driverestoreartifactsbulkadditionrequests?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, DriveRestoreArtifactsBulkAdditionRequest, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DriveRestoreArtifactsBulkAdditionRequestsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DriveRestoreArtifactsBulkAdditionRequestsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DriveRestoreArtifactsBulkAdditionRequestsRequest(self.request_adapter, self.path_parameters)

	def by_drive_restore_artifacts_bulk_addition_request_id(self,
		oneDriveForBusinessRestoreSession_id: str,
		driveRestoreArtifactsBulkAdditionRequest_id: str,
	) -> ByDriveRestoreArtifactsBulkAdditionRequestIdRequest:
		if oneDriveForBusinessRestoreSession_id is None:
			raise TypeError("oneDriveForBusinessRestoreSession_id cannot be null.")
		if driveRestoreArtifactsBulkAdditionRequest_id is None:
			raise TypeError("driveRestoreArtifactsBulkAdditionRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oneDriveForBusinessRestoreSession%2Did"] =  oneDriveForBusinessRestoreSession_id
		path_parameters["driveRestoreArtifactsBulkAdditionRequest%2Did"] =  driveRestoreArtifactsBulkAdditionRequest_id

		from .by_drive_restore_artifacts_bulk_addition_request_id import ByDriveRestoreArtifactsBulkAdditionRequestIdRequest
		return ByDriveRestoreArtifactsBulkAdditionRequestIdRequest(self.request_adapter, path_parameters)

	def count(self,
		oneDriveForBusinessRestoreSession_id: str,
	) -> CountRequest:
		if oneDriveForBusinessRestoreSession_id is None:
			raise TypeError("oneDriveForBusinessRestoreSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oneDriveForBusinessRestoreSession%2Did"] =  oneDriveForBusinessRestoreSession_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

