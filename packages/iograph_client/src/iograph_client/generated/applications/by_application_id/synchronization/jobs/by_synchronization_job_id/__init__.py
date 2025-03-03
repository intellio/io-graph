# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .schema import SchemaRequest
	from .validate_credentials import ValidateCredentialsRequest
	from .start import StartRequest
	from .restart import RestartRequest
	from .provision_on_demand import ProvisionOnDemandRequest
	from .pause import PauseRequest
	from .bulk_upload import BulkUploadRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.synchronization_job import SynchronizationJob
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class BySynchronizationJobIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/synchronization/jobs/{synchronizationJob%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SynchronizationJob:
		"""
		Get jobs from applications
		Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
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
		return await self.request_adapter.send_async(request_info, SynchronizationJob, error_mapping)

	async def patch(
		self,
		body: SynchronizationJob,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SynchronizationJob:
		"""
		Update the navigation property jobs in applications
		
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
		return await self.request_adapter.send_async(request_info, SynchronizationJob, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property jobs for applications
		
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



	def with_url(self, raw_url: str) -> BySynchronizationJobIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySynchronizationJobIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySynchronizationJobIdRequest(self.request_adapter, self.path_parameters)

	@property
	def bulk_upload(self,
	) -> BulkUploadRequest:
		from .bulk_upload import BulkUploadRequest
		return BulkUploadRequest(self.request_adapter, self.path_parameters)

	@property
	def pause(self,
	) -> PauseRequest:
		from .pause import PauseRequest
		return PauseRequest(self.request_adapter, self.path_parameters)

	@property
	def provision_on_demand(self,
	) -> ProvisionOnDemandRequest:
		from .provision_on_demand import ProvisionOnDemandRequest
		return ProvisionOnDemandRequest(self.request_adapter, self.path_parameters)

	@property
	def restart(self,
	) -> RestartRequest:
		from .restart import RestartRequest
		return RestartRequest(self.request_adapter, self.path_parameters)

	@property
	def start(self,
	) -> StartRequest:
		from .start import StartRequest
		return StartRequest(self.request_adapter, self.path_parameters)

	@property
	def validate_credentials(self,
	) -> ValidateCredentialsRequest:
		from .validate_credentials import ValidateCredentialsRequest
		return ValidateCredentialsRequest(self.request_adapter, self.path_parameters)

	@property
	def schema(self,
	) -> SchemaRequest:
		from .schema import SchemaRequest
		return SchemaRequest(self.request_adapter, self.path_parameters)

