# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.domain import Domain
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class VerifyRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/domains/{domain%2Did}/verify", path_parameters)

	async def post(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Domain:
		"""
		Invoke action verify
		Validates the ownership of the domain.
		Find more info here: https://learn.microsoft.com/graph/api/domain-verify?view=graph-rest-1.0
		"""
		tags = ['domains.domain.Actions']

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
		return await self.request_adapter.send_async(request_info, Domain, error_mapping)


	def with_url(self, raw_url: str) -> VerifyRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: VerifyRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return VerifyRequest(self.request_adapter, self.path_parameters)

