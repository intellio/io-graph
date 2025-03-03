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
	from .mailbox_protection_units import MailboxProtectionUnitsRequest
	from .mailbox_inclusion_rules import MailboxInclusionRulesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.exchange_protection_policy import ExchangeProtectionPolicy
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByExchangeProtectionPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/exchangeProtectionPolicies/{exchangeProtectionPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExchangeProtectionPolicy:
		"""
		Get exchangeProtectionPolicies from solutions
		The list of Exchange protection policies in the tenant.
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
		return await self.request_adapter.send_async(request_info, ExchangeProtectionPolicy, error_mapping)

	async def patch(
		self,
		body: ExchangeProtectionPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ExchangeProtectionPolicy:
		"""
		Update exchangeProtectionPolicy
		Update an Exchange protection policy. This method adds a mailboxprotectionunit to or removes it from the protection policy.
		Find more info here: https://learn.microsoft.com/graph/api/exchangeprotectionpolicy-update?view=graph-rest-1.0
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, ExchangeProtectionPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property exchangeProtectionPolicies for solutions
		
		"""
		tags = ['solutions.backupRestoreRoot']
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



	def with_url(self, raw_url: str) -> ByExchangeProtectionPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByExchangeProtectionPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByExchangeProtectionPolicyIdRequest(self.request_adapter, self.path_parameters)

	@property
	def mailbox_inclusion_rules(self,
	) -> MailboxInclusionRulesRequest:
		from .mailbox_inclusion_rules import MailboxInclusionRulesRequest
		return MailboxInclusionRulesRequest(self.request_adapter, self.path_parameters)

	@property
	def mailbox_protection_units(self,
	) -> MailboxProtectionUnitsRequest:
		from .mailbox_protection_units import MailboxProtectionUnitsRequest
		return MailboxProtectionUnitsRequest(self.request_adapter, self.path_parameters)

