# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.mailbox_protection_rule import MailboxProtectionRule
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByMailboxProtectionRuleIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/exchangeProtectionPolicies/{exchangeProtectionPolicy%2Did}/mailboxInclusionRules/{mailboxProtectionRule%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailboxProtectionRule:
		"""
		Get protectionRuleBase
		Get a protection rule that's associated with a protection policy. You can use this operation to get mailbox, drive, and site protection rules. An inclusion rule indicates that a protection policy should contain protection units that match the specified rule criteria. The initial status of a protection rule upon creation is active. After the rule is applied, the state is either completed or completedWithErrors.
		Find more info here: https://learn.microsoft.com/graph/api/protectionrulebase-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, MailboxProtectionRule, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByMailboxProtectionRuleIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMailboxProtectionRuleIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMailboxProtectionRuleIdRequest(self.request_adapter, self.path_parameters)

