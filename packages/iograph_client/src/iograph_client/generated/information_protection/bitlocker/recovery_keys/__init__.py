# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_bitlocker_recovery_key_id import ByBitlockerRecoveryKeyIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.bitlocker_recovery_key_collection_response import BitlockerRecoveryKeyCollectionResponse


class RecoveryKeysRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/informationProtection/bitlocker/recoveryKeys"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BitlockerRecoveryKeyCollectionResponse:
		"""
		List recoveryKeys
		Get a list of the bitlockerRecoveryKey objects and their properties.  This operation does not return the key property. For information about how to read the key property, see Get bitlockerRecoveryKey. You can use this API to programmatically iterate through the list of recovery keys in the tenant and identify devices with BitLocker enabled. For more information, see the sample PowerShell code in BitLocker recovery process.
		Find more info here: https://learn.microsoft.com/graph/api/bitlocker-list-recoverykeys?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, BitlockerRecoveryKeyCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def by_bitlocker_recovery_key_id(self,
		bitlockerRecoveryKey_id: str,
	) -> ByBitlockerRecoveryKeyIdRequest:
		if bitlockerRecoveryKey_id is None:
			raise TypeError("bitlockerRecoveryKey_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bitlockerRecoveryKey%2Did"] =  bitlockerRecoveryKey_id

		from .by_bitlocker_recovery_key_id import ByBitlockerRecoveryKeyIdRequest
		return ByBitlockerRecoveryKeyIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

