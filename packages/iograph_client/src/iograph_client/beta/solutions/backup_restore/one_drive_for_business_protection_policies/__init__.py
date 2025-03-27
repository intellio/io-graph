# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_one_drive_for_business_protection_policy_id import ByOneDriveForBusinessProtectionPolicyIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.one_drive_for_business_protection_policy_collection_response import OneDriveForBusinessProtectionPolicyCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy


class OneDriveForBusinessProtectionPoliciesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/oneDriveForBusinessProtectionPolicies", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OneDriveForBusinessProtectionPolicyCollectionResponse:
		"""
		Get oneDriveForBusinessProtectionPolicies from solutions
		The list of OneDrive for Business protection policies in the tenant.
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
		return await self.request_adapter.send_async(request_info, OneDriveForBusinessProtectionPolicyCollectionResponse, error_mapping)

	async def post(
		self,
		body: OneDriveForBusinessProtectionPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OneDriveForBusinessProtectionPolicy:
		"""
		Create oneDriveForBusinessProtectionPolicy
		Create a protection policy for the OneDrive service in Microsoft 365. When the policy is created, its state is set to inactive. Users can also provide a list of protection units under the policy.
		Find more info here: https://learn.microsoft.com/graph/api/backuprestoreroot-post-onedriveforbusinessprotectionpolicies?view=graph-rest-beta
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, OneDriveForBusinessProtectionPolicy, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> OneDriveForBusinessProtectionPoliciesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OneDriveForBusinessProtectionPoliciesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OneDriveForBusinessProtectionPoliciesRequest(self.request_adapter, self.path_parameters)

	def by_one_drive_for_business_protection_policy_id(self,
		oneDriveForBusinessProtectionPolicy_id: str,
	) -> ByOneDriveForBusinessProtectionPolicyIdRequest:
		if oneDriveForBusinessProtectionPolicy_id is None:
			raise TypeError("oneDriveForBusinessProtectionPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oneDriveForBusinessProtectionPolicy%2Did"] =  oneDriveForBusinessProtectionPolicy_id

		from .by_one_drive_for_business_protection_policy_id import ByOneDriveForBusinessProtectionPolicyIdRequest
		return ByOneDriveForBusinessProtectionPolicyIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

