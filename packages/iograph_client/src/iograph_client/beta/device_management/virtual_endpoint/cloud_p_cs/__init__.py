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
	from .validate_bulk_resize import ValidateBulkResizeRequest
	from .get_provisioned_cloud_p_cs_with_groupid_serviceplanid import GetProvisionedCloudPCsWithGroupIdServicePlanIdRequest
	from .bulk_resize import BulkResizeRequest
	from .count import CountRequest
	from .by_cloud_p_c_id import ByCloudPCIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.cloud_p_c_collection_response import CloudPCCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.cloud_p_c import CloudPC


class CloudPCsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudPCCollectionResponse:
		"""
		List cloudPCs
		List the cloudPC devices in a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/virtualendpoint-list-cloudpcs?view=graph-rest-beta
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPCCollectionResponse, error_mapping)

	async def post(
		self,
		body: CloudPC,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPC:
		"""
		Create new navigation property to cloudPCs for deviceManagement
		
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> CloudPCsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CloudPCsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CloudPCsRequest(self.request_adapter, self.path_parameters)

	def by_cloud_p_c_id(self,
		cloudPC_id: str,
	) -> ByCloudPCIdRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .by_cloud_p_c_id import ByCloudPCIdRequest
		return ByCloudPCIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def bulk_resize(self,
	) -> BulkResizeRequest:
		from .bulk_resize import BulkResizeRequest
		return BulkResizeRequest(self.request_adapter, self.path_parameters)

	def get_provisioned_cloud_p_cs_with_groupid_serviceplanid(self,
		groupId: str,
		servicePlanId: str,
	) -> GetProvisionedCloudPCsWithGroupIdServicePlanIdRequest:
		if groupId is None:
			raise TypeError("groupId cannot be null.")
		if servicePlanId is None:
			raise TypeError("servicePlanId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupId"] =  groupId
		path_parameters["servicePlanId"] =  servicePlanId

		from .get_provisioned_cloud_p_cs_with_groupid_serviceplanid import GetProvisionedCloudPCsWithGroupIdServicePlanIdRequest
		return GetProvisionedCloudPCsWithGroupIdServicePlanIdRequest(self.request_adapter, path_parameters)

	@property
	def validate_bulk_resize(self,
	) -> ValidateBulkResizeRequest:
		from .validate_bulk_resize import ValidateBulkResizeRequest
		return ValidateBulkResizeRequest(self.request_adapter, self.path_parameters)

