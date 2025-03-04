# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .parse_expression import ParseExpressionRequest
	from .functions import FunctionsRequest
	from .filter_operators import FilterOperatorsRequest
	from .directories import DirectoriesRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.synchronization_schema import SynchronizationSchema


class SchemaRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/synchronization/jobs/{synchronizationJob%2Did}/schema", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SynchronizationSchema:
		"""
		Get schema from applications
		The synchronization schema configured for the job.
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
		return await self.request_adapter.send_async(request_info, SynchronizationSchema, error_mapping)

	async def patch(
		self,
		body: SynchronizationSchema,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SynchronizationSchema:
		"""
		Update the navigation property schema in applications
		
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
		return await self.request_adapter.send_async(request_info, SynchronizationSchema, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property schema for applications
		
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



	def with_url(self, raw_url: str) -> SchemaRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SchemaRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SchemaRequest(self.request_adapter, self.path_parameters)

	def directories(self,
		application_id: str,
		synchronizationJob_id: str,
	) -> DirectoriesRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .directories import DirectoriesRequest
		return DirectoriesRequest(self.request_adapter, path_parameters)

	def filter_operators(self,
		application_id: str,
		synchronizationJob_id: str,
	) -> FilterOperatorsRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .filter_operators import FilterOperatorsRequest
		return FilterOperatorsRequest(self.request_adapter, path_parameters)

	def functions(self,
		application_id: str,
		synchronizationJob_id: str,
	) -> FunctionsRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .functions import FunctionsRequest
		return FunctionsRequest(self.request_adapter, path_parameters)

	def parse_expression(self,
		application_id: str,
		synchronizationJob_id: str,
	) -> ParseExpressionRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .parse_expression import ParseExpressionRequest
		return ParseExpressionRequest(self.request_adapter, path_parameters)

