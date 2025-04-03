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
	from .validate_credentials import ValidateCredentialsRequest
	from .count import CountRequest
	from .by_synchronization_job_id import BySynchronizationJobIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.synchronization_job import SynchronizationJob
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.synchronization_job_collection_response import SynchronizationJobCollectionResponse


class JobsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/synchronization/jobs", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SynchronizationJobCollectionResponse:
		"""
		List synchronization jobs
		List existing jobs for a given application instance (service principal).
		Find more info here: https://learn.microsoft.com/graph/api/synchronization-synchronization-list-jobs?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, SynchronizationJobCollectionResponse, error_mapping)

	async def post(
		self,
		body: SynchronizationJob,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SynchronizationJob:
		"""
		Create synchronizationJob
		Create new synchronization job with a default synchronization schema. The job is created in a disabled state. Call Start job to start synchronization.
		Find more info here: https://learn.microsoft.com/graph/api/synchronization-synchronization-post-jobs?view=graph-rest-beta
		"""
		tags = ['servicePrincipals.synchronization']

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
		return await self.request_adapter.send_async(request_info, SynchronizationJob, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> JobsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: JobsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return JobsRequest(self.request_adapter, self.path_parameters)

	def by_synchronization_job_id(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
	) -> BySynchronizationJobIdRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .by_synchronization_job_id import BySynchronizationJobIdRequest
		return BySynchronizationJobIdRequest(self.request_adapter, path_parameters)

	def count(self,
		servicePrincipal_id: str,
	) -> CountRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def validate_credentials(self,
		servicePrincipal_id: str,
	) -> ValidateCredentialsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .validate_credentials import ValidateCredentialsRequest
		return ValidateCredentialsRequest(self.request_adapter, path_parameters)

