# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.bitlocker_recovery_key import BitlockerRecoveryKey


class ByBitlockerRecoveryKeyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/informationProtection/bitlocker/recoveryKeys/{bitlockerRecoveryKey%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BitlockerRecoveryKey:
		"""
		Get bitlockerRecoveryKey
		Retrieve the properties and relationships of a bitlockerRecoveryKey object.  By default, this operation doesn't return the key property that represents the actual recovery key. To include the key property in the response, use the $select OData query parameter. Including the $select query parameter triggers a Microsoft Entra audit of the operation and generates an audit log. For more information on audit logs for bitlocker recovery keys, see the KeyManagement category filter of Microsoft Entra audit logs.
		Find more info here: https://learn.microsoft.com/graph/api/bitlockerrecoverykey-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, BitlockerRecoveryKey, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByBitlockerRecoveryKeyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByBitlockerRecoveryKeyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByBitlockerRecoveryKeyIdRequest(self.request_adapter, self.path_parameters)

