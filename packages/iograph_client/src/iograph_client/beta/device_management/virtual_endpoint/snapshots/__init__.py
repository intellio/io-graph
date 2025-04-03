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
	from .get_subscriptions import GetSubscriptionsRequest
	from .get_storage_accounts_with_subscriptionid import GetStorageAccountsWithSubscriptionIdRequest
	from .count import CountRequest
	from .by_cloud_pc_snapshot_id import ByCloudPcSnapshotIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.cloud_pc_snapshot_collection_response import CloudPcSnapshotCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.cloud_pc_snapshot import CloudPcSnapshot


class SnapshotsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/snapshots", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudPcSnapshotCollectionResponse:
		"""
		List snapshots (deprecated)
		Get a list of cloudPcSnapshot objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/virtualendpoint-list-snapshots?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, CloudPcSnapshotCollectionResponse, error_mapping)

	async def post(
		self,
		body: CloudPcSnapshot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPcSnapshot:
		"""
		Create new navigation property to snapshots for deviceManagement
		
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
		return await self.request_adapter.send_async(request_info, CloudPcSnapshot, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SnapshotsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SnapshotsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SnapshotsRequest(self.request_adapter, self.path_parameters)

	def by_cloud_pc_snapshot_id(self,
		cloudPcSnapshot_id: str,
	) -> ByCloudPcSnapshotIdRequest:
		if cloudPcSnapshot_id is None:
			raise TypeError("cloudPcSnapshot_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPcSnapshot%2Did"] =  cloudPcSnapshot_id

		from .by_cloud_pc_snapshot_id import ByCloudPcSnapshotIdRequest
		return ByCloudPcSnapshotIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	def get_storage_accounts_with_subscriptionid(self,
		subscriptionId: str,
	) -> GetStorageAccountsWithSubscriptionIdRequest:
		if subscriptionId is None:
			raise TypeError("subscriptionId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subscriptionId"] =  subscriptionId

		from .get_storage_accounts_with_subscriptionid import GetStorageAccountsWithSubscriptionIdRequest
		return GetStorageAccountsWithSubscriptionIdRequest(self.request_adapter, path_parameters)

	@property
	def get_subscriptions(self,
	) -> GetSubscriptionsRequest:
		from .get_subscriptions import GetSubscriptionsRequest
		return GetSubscriptionsRequest(self.request_adapter, self.path_parameters)

