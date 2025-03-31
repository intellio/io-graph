# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_mobile_app_provisioning_config_group_assignment_id import ByMobileAppProvisioningConfigGroupAssignmentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment
from iograph_models.beta.mobile_app_provisioning_config_group_assignment_collection_response import MobileAppProvisioningConfigGroupAssignmentCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class GroupAssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/iosLobAppProvisioningConfigurations/{iosLobAppProvisioningConfiguration%2Did}/groupAssignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MobileAppProvisioningConfigGroupAssignmentCollectionResponse:
		"""
		Get groupAssignments from deviceAppManagement
		The associated group assignments.
		"""
		tags = ['deviceAppManagement.iosLobAppProvisioningConfiguration']

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
		return await self.request_adapter.send_async(request_info, MobileAppProvisioningConfigGroupAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: MobileAppProvisioningConfigGroupAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MobileAppProvisioningConfigGroupAssignment:
		"""
		Create new navigation property to groupAssignments for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.iosLobAppProvisioningConfiguration']

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
		return await self.request_adapter.send_async(request_info, MobileAppProvisioningConfigGroupAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> GroupAssignmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GroupAssignmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GroupAssignmentsRequest(self.request_adapter, self.path_parameters)

	def by_mobile_app_provisioning_config_group_assignment_id(self,
		iosLobAppProvisioningConfiguration_id: str,
		mobileAppProvisioningConfigGroupAssignment_id: str,
	) -> ByMobileAppProvisioningConfigGroupAssignmentIdRequest:
		if iosLobAppProvisioningConfiguration_id is None:
			raise TypeError("iosLobAppProvisioningConfiguration_id cannot be null.")
		if mobileAppProvisioningConfigGroupAssignment_id is None:
			raise TypeError("mobileAppProvisioningConfigGroupAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["iosLobAppProvisioningConfiguration%2Did"] =  iosLobAppProvisioningConfiguration_id
		path_parameters["mobileAppProvisioningConfigGroupAssignment%2Did"] =  mobileAppProvisioningConfigGroupAssignment_id

		from .by_mobile_app_provisioning_config_group_assignment_id import ByMobileAppProvisioningConfigGroupAssignmentIdRequest
		return ByMobileAppProvisioningConfigGroupAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		iosLobAppProvisioningConfiguration_id: str,
	) -> CountRequest:
		if iosLobAppProvisioningConfiguration_id is None:
			raise TypeError("iosLobAppProvisioningConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["iosLobAppProvisioningConfiguration%2Did"] =  iosLobAppProvisioningConfiguration_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

