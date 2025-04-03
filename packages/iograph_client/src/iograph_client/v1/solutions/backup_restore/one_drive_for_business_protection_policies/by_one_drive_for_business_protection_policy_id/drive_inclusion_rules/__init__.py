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
	from .by_drive_protection_rule_id import ByDriveProtectionRuleIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.drive_protection_rule_collection_response import DriveProtectionRuleCollectionResponse


class DriveInclusionRulesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/oneDriveForBusinessProtectionPolicies/{oneDriveForBusinessProtectionPolicy%2Did}/driveInclusionRules", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DriveProtectionRuleCollectionResponse:
		"""
		List driveInclusionRules
		Get a list of the driveProtectionRule objects that are associated with a OneDrive for Business protection policy. An inclusion rule indicates that a protection policy should contain protection units that match the specified rule criteria. The initial status of a protection rule upon creation is active. After the rule is applied, the state is either completed or completedWithErrors.
		Find more info here: https://learn.microsoft.com/graph/api/onedriveforbusinessprotectionpolicy-list-driveinclusionrules?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, DriveProtectionRuleCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> DriveInclusionRulesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DriveInclusionRulesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DriveInclusionRulesRequest(self.request_adapter, self.path_parameters)

	def by_drive_protection_rule_id(self,
		oneDriveForBusinessProtectionPolicy_id: str,
		driveProtectionRule_id: str,
	) -> ByDriveProtectionRuleIdRequest:
		if oneDriveForBusinessProtectionPolicy_id is None:
			raise TypeError("oneDriveForBusinessProtectionPolicy_id cannot be null.")
		if driveProtectionRule_id is None:
			raise TypeError("driveProtectionRule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oneDriveForBusinessProtectionPolicy%2Did"] =  oneDriveForBusinessProtectionPolicy_id
		path_parameters["driveProtectionRule%2Did"] =  driveProtectionRule_id

		from .by_drive_protection_rule_id import ByDriveProtectionRuleIdRequest
		return ByDriveProtectionRuleIdRequest(self.request_adapter, path_parameters)

	def count(self,
		oneDriveForBusinessProtectionPolicy_id: str,
	) -> CountRequest:
		if oneDriveForBusinessProtectionPolicy_id is None:
			raise TypeError("oneDriveForBusinessProtectionPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oneDriveForBusinessProtectionPolicy%2Did"] =  oneDriveForBusinessProtectionPolicy_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

