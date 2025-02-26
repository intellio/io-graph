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
	from .by_managed_app_policy_id import ByManagedAppPolicyIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.managed_app_policy import ManagedAppPolicy
from iograph_models.models.managed_app_policy_collection_response import ManagedAppPolicyCollectionResponse


class AppliedPoliciesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceAppManagement/managedAppRegistrations/{managedAppRegistration%2Did}/appliedPolicies"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedAppPolicyCollectionResponse:
		"""
		Get appliedPolicies from deviceAppManagement
		Zero or more policys already applied on the registered app when it last synchronized with managment service.
		"""
		tags = ['deviceAppManagement.managedAppRegistration']

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
		return await self.request_adapter.send_async(request_info, ManagedAppPolicyCollectionResponse, error_mapping)

	async def post(
		self,
		body: ManagedAppPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedAppPolicy:
		"""
		Create new navigation property to appliedPolicies for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.managedAppRegistration']

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
		return await self.request_adapter.send_async(request_info, ManagedAppPolicy, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_managed_app_policy_id(self,
		managedAppRegistration_id: str,
		managedAppPolicy_id: str,
	) -> ByManagedAppPolicyIdRequest:
		if managedAppRegistration_id is None:
			raise TypeError("managedAppRegistration_id cannot be null.")
		if managedAppPolicy_id is None:
			raise TypeError("managedAppPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedAppRegistration%2Did"] =  managedAppRegistration_id
		path_parameters["managedAppPolicy%2Did"] =  managedAppPolicy_id

		from .by_managed_app_policy_id import ByManagedAppPolicyIdRequest
		return ByManagedAppPolicyIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

