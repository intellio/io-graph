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
	from .count import CountRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.secrets_put_response import SecretsPutResponse
from iograph_models.models.secrets_put_request import SecretsPutRequest


class SecretsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/synchronization/secrets", path_parameters)

	async def put(
		self,
		body: SecretsPutRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecretsPutResponse:
		"""
		Update property secrets value.
		
		"""
		tags = ['applications.synchronization']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PUT,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, SecretsPutResponse, error_mapping)


	def with_url(self, raw_url: str) -> SecretsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SecretsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SecretsRequest(self.request_adapter, self.path_parameters)

	def count(self,
		application_id: str,
	) -> CountRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

