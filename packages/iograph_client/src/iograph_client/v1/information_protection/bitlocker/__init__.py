# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .recovery_keys import RecoveryKeysRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.bitlocker import Bitlocker
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class BitlockerRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/informationProtection/bitlocker", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Bitlocker:
		"""
		Get bitlocker from informationProtection
		
		"""
		tags = ['informationProtection.bitlocker']

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
		return await self.request_adapter.send_async(request_info, Bitlocker, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> BitlockerRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BitlockerRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BitlockerRequest(self.request_adapter, self.path_parameters)

	@property
	def recovery_keys(self,
	) -> RecoveryKeysRequest:
		from .recovery_keys import RecoveryKeysRequest
		return RecoveryKeysRequest(self.request_adapter, self.path_parameters)

