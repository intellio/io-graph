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
	from .schema import SchemaRequest
	from .validate_credentials import ValidateCredentialsRequest
	from .start import StartRequest
	from .restart import RestartRequest
	from .provision_on_demand import ProvisionOnDemandRequest
	from .pause import PauseRequest
	from .bulk_upload import BulkUploadRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.synchronization_job import SynchronizationJob
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class BySynchronizationJobIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/synchronization/jobs/{synchronizationJob%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SynchronizationJob:
		"""
		Get synchronizationJob
		Retrieve the existing synchronization job and its properties.
		Find more info here: https://learn.microsoft.com/graph/api/synchronization-synchronizationjob-get?view=graph-rest-beta
		"""
		tags = ['servicePrincipals.synchronization']

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
		Update the navigation property jobs in servicePrincipals
		
		"""
		tags = ['servicePrincipals.synchronization']

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
		Delete synchronizationJob
		Stop the synchronization job, and permanently delete all the state associated with it. Synchronized accounts are left as-is.
		Find more info here: https://learn.microsoft.com/graph/api/synchronization-synchronizationjob-delete?view=graph-rest-beta
		"""
		tags = ['servicePrincipals.synchronization']
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

	def bulk_upload(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
	) -> BulkUploadRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .bulk_upload import BulkUploadRequest
		return BulkUploadRequest(self.request_adapter, path_parameters)

	def pause(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
	) -> PauseRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .pause import PauseRequest
		return PauseRequest(self.request_adapter, path_parameters)

	def provision_on_demand(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
	) -> ProvisionOnDemandRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .provision_on_demand import ProvisionOnDemandRequest
		return ProvisionOnDemandRequest(self.request_adapter, path_parameters)

	def restart(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
	) -> RestartRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .restart import RestartRequest
		return RestartRequest(self.request_adapter, path_parameters)

	def start(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
	) -> StartRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .start import StartRequest
		return StartRequest(self.request_adapter, path_parameters)

	def validate_credentials(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
	) -> ValidateCredentialsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .validate_credentials import ValidateCredentialsRequest
		return ValidateCredentialsRequest(self.request_adapter, path_parameters)

	def schema(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
	) -> SchemaRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .schema import SchemaRequest
		return SchemaRequest(self.request_adapter, path_parameters)

