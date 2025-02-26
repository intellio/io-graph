# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_unified_role_management_policy_rule_id import ByUnifiedRoleManagementPolicyRuleIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.unified_role_management_policy_rule_collection_response import UnifiedRoleManagementPolicyRuleCollectionResponse
from iograph_models.models.unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class EffectiveRulesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/policies/roleManagementPolicies/{unifiedRoleManagementPolicy%2Did}/effectiveRules"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleManagementPolicyRuleCollectionResponse:
		"""
		Get effectiveRules from policies
		The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.
		"""
		tags = ['policies.unifiedRoleManagementPolicy']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementPolicyRuleCollectionResponse, error_mapping)

	async def post(
		self,
		body: UnifiedRoleManagementPolicyRule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleManagementPolicyRule:
		"""
		Create new navigation property to effectiveRules for policies
		
		"""
		tags = ['policies.unifiedRoleManagementPolicy']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementPolicyRule, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_unified_role_management_policy_rule_id(self,
		unifiedRoleManagementPolicy_id: str,
		unifiedRoleManagementPolicyRule_id: str,
	) -> ByUnifiedRoleManagementPolicyRuleIdRequest:
		if unifiedRoleManagementPolicy_id is None:
			raise TypeError("unifiedRoleManagementPolicy_id cannot be null.")
		if unifiedRoleManagementPolicyRule_id is None:
			raise TypeError("unifiedRoleManagementPolicyRule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleManagementPolicy%2Did"] =  unifiedRoleManagementPolicy_id
		path_parameters["unifiedRoleManagementPolicyRule%2Did"] =  unifiedRoleManagementPolicyRule_id

		from .by_unified_role_management_policy_rule_id import ByUnifiedRoleManagementPolicyRuleIdRequest
		return ByUnifiedRoleManagementPolicyRuleIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

