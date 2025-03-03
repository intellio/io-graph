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
	from .by_mailbox_protection_unit_id import ByMailboxProtectionUnitIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.mailbox_protection_unit_collection_response import MailboxProtectionUnitCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class MailboxProtectionUnitsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/exchangeProtectionPolicies/{exchangeProtectionPolicy%2Did}/mailboxProtectionUnits", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailboxProtectionUnitCollectionResponse:
		"""
		Get mailboxProtectionUnits from solutions
		The protection units (mailboxes) that are  protected under the Exchange protection policy.
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
		return await self.request_adapter.send_async(request_info, MailboxProtectionUnitCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> MailboxProtectionUnitsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MailboxProtectionUnitsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MailboxProtectionUnitsRequest(self.request_adapter, self.path_parameters)

	def by_mailbox_protection_unit_id(self,
		exchangeProtectionPolicy_id: str,
		mailboxProtectionUnit_id: str,
	) -> ByMailboxProtectionUnitIdRequest:
		if exchangeProtectionPolicy_id is None:
			raise TypeError("exchangeProtectionPolicy_id cannot be null.")
		if mailboxProtectionUnit_id is None:
			raise TypeError("mailboxProtectionUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["exchangeProtectionPolicy%2Did"] =  exchangeProtectionPolicy_id
		path_parameters["mailboxProtectionUnit%2Did"] =  mailboxProtectionUnit_id

		from .by_mailbox_protection_unit_id import ByMailboxProtectionUnitIdRequest
		return ByMailboxProtectionUnitIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

