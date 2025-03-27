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
	from .by_drive_restore_artifact_id import ByDriveRestoreArtifactIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.drive_restore_artifact import DriveRestoreArtifact
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.drive_restore_artifact_collection_response import DriveRestoreArtifactCollectionResponse


class DriveRestoreArtifactsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/oneDriveForBusinessRestoreSessions/{oneDriveForBusinessRestoreSession%2Did}/driveRestoreArtifacts", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DriveRestoreArtifactCollectionResponse:
		"""
		List driveRestoreArtifacts
		Get a list of the driveRestoreArtifact objects and their properties for a oneDriveForBusinessRestoreSession for a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/onedriveforbusinessrestoresession-list-driverestoreartifacts?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, DriveRestoreArtifactCollectionResponse, error_mapping)

	async def post(
		self,
		body: DriveRestoreArtifact,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DriveRestoreArtifact:
		"""
		Create new navigation property to driveRestoreArtifacts for solutions
		
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
		return await self.request_adapter.send_async(request_info, DriveRestoreArtifact, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DriveRestoreArtifactsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DriveRestoreArtifactsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DriveRestoreArtifactsRequest(self.request_adapter, self.path_parameters)

	def by_drive_restore_artifact_id(self,
		oneDriveForBusinessRestoreSession_id: str,
		driveRestoreArtifact_id: str,
	) -> ByDriveRestoreArtifactIdRequest:
		if oneDriveForBusinessRestoreSession_id is None:
			raise TypeError("oneDriveForBusinessRestoreSession_id cannot be null.")
		if driveRestoreArtifact_id is None:
			raise TypeError("driveRestoreArtifact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oneDriveForBusinessRestoreSession%2Did"] =  oneDriveForBusinessRestoreSession_id
		path_parameters["driveRestoreArtifact%2Did"] =  driveRestoreArtifact_id

		from .by_drive_restore_artifact_id import ByDriveRestoreArtifactIdRequest
		return ByDriveRestoreArtifactIdRequest(self.request_adapter, path_parameters)

	def count(self,
		oneDriveForBusinessRestoreSession_id: str,
	) -> CountRequest:
		if oneDriveForBusinessRestoreSession_id is None:
			raise TypeError("oneDriveForBusinessRestoreSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oneDriveForBusinessRestoreSession%2Did"] =  oneDriveForBusinessRestoreSession_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

