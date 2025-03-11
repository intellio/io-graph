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
	from .troubleshoot import TroubleshootRequest
	from .stop import StopRequest
	from .start import StartRequest
	from .set_review_status import SetReviewStatusRequest
	from .retry_partner_agent_installation import RetryPartnerAgentInstallationRequest
	from .retrieve_snapshots import RetrieveSnapshotsRequest
	from .retrieve_review_status import RetrieveReviewStatusRequest
	from .retrieve_cloud_p_c_remote_action_results import RetrieveCloudPCRemoteActionResultsRequest
	from .restore import RestoreRequest
	from .resize import ResizeRequest
	from .reprovision import ReprovisionRequest
	from .rename import RenameRequest
	from .reboot import RebootRequest
	from .power_on import PowerOnRequest
	from .power_off import PowerOffRequest
	from .get_supported_cloud_pc_remote_actions import GetSupportedCloudPcRemoteActionsRequest
	from .get_frontline_cloud_pc_access_state import GetFrontlineCloudPcAccessStateRequest
	from .get_cloud_pc_launch_info import GetCloudPcLaunchInfoRequest
	from .get_cloud_pc_connectivity_history import GetCloudPcConnectivityHistoryRequest
	from .end_grace_period import EndGracePeriodRequest
	from .create_snapshot import CreateSnapshotRequest
	from .change_user_account_type import ChangeUserAccountTypeRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.cloud_p_c import CloudPC


class ByCloudPCIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs/{cloudPC%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudPC:
		"""
		Get cloudPC
		Read the properties and relationships of a specific cloudPC object.
		Find more info here: https://learn.microsoft.com/graph/api/cloudpc-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)

	async def patch(
		self,
		body: CloudPC,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudPC:
		"""
		Update the navigation property cloudPCs in deviceManagement
		
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property cloudPCs for deviceManagement
		
		"""
		tags = ['deviceManagement.virtualEndpoint']
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



	def with_url(self, raw_url: str) -> ByCloudPCIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCloudPCIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCloudPCIdRequest(self.request_adapter, self.path_parameters)

	def change_user_account_type(self,
		cloudPC_id: str,
	) -> ChangeUserAccountTypeRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .change_user_account_type import ChangeUserAccountTypeRequest
		return ChangeUserAccountTypeRequest(self.request_adapter, path_parameters)

	def create_snapshot(self,
		cloudPC_id: str,
	) -> CreateSnapshotRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .create_snapshot import CreateSnapshotRequest
		return CreateSnapshotRequest(self.request_adapter, path_parameters)

	def end_grace_period(self,
		cloudPC_id: str,
	) -> EndGracePeriodRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .end_grace_period import EndGracePeriodRequest
		return EndGracePeriodRequest(self.request_adapter, path_parameters)

	def get_cloud_pc_connectivity_history(self,
		cloudPC_id: str,
	) -> GetCloudPcConnectivityHistoryRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .get_cloud_pc_connectivity_history import GetCloudPcConnectivityHistoryRequest
		return GetCloudPcConnectivityHistoryRequest(self.request_adapter, path_parameters)

	def get_cloud_pc_launch_info(self,
		cloudPC_id: str,
	) -> GetCloudPcLaunchInfoRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .get_cloud_pc_launch_info import GetCloudPcLaunchInfoRequest
		return GetCloudPcLaunchInfoRequest(self.request_adapter, path_parameters)

	def get_frontline_cloud_pc_access_state(self,
		cloudPC_id: str,
	) -> GetFrontlineCloudPcAccessStateRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .get_frontline_cloud_pc_access_state import GetFrontlineCloudPcAccessStateRequest
		return GetFrontlineCloudPcAccessStateRequest(self.request_adapter, path_parameters)

	def get_supported_cloud_pc_remote_actions(self,
		cloudPC_id: str,
	) -> GetSupportedCloudPcRemoteActionsRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .get_supported_cloud_pc_remote_actions import GetSupportedCloudPcRemoteActionsRequest
		return GetSupportedCloudPcRemoteActionsRequest(self.request_adapter, path_parameters)

	def power_off(self,
		cloudPC_id: str,
	) -> PowerOffRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .power_off import PowerOffRequest
		return PowerOffRequest(self.request_adapter, path_parameters)

	def power_on(self,
		cloudPC_id: str,
	) -> PowerOnRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .power_on import PowerOnRequest
		return PowerOnRequest(self.request_adapter, path_parameters)

	def reboot(self,
		cloudPC_id: str,
	) -> RebootRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .reboot import RebootRequest
		return RebootRequest(self.request_adapter, path_parameters)

	def rename(self,
		cloudPC_id: str,
	) -> RenameRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .rename import RenameRequest
		return RenameRequest(self.request_adapter, path_parameters)

	def reprovision(self,
		cloudPC_id: str,
	) -> ReprovisionRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .reprovision import ReprovisionRequest
		return ReprovisionRequest(self.request_adapter, path_parameters)

	def resize(self,
		cloudPC_id: str,
	) -> ResizeRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .resize import ResizeRequest
		return ResizeRequest(self.request_adapter, path_parameters)

	def restore(self,
		cloudPC_id: str,
	) -> RestoreRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def retrieve_cloud_p_c_remote_action_results(self,
		cloudPC_id: str,
	) -> RetrieveCloudPCRemoteActionResultsRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .retrieve_cloud_p_c_remote_action_results import RetrieveCloudPCRemoteActionResultsRequest
		return RetrieveCloudPCRemoteActionResultsRequest(self.request_adapter, path_parameters)

	def retrieve_review_status(self,
		cloudPC_id: str,
	) -> RetrieveReviewStatusRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .retrieve_review_status import RetrieveReviewStatusRequest
		return RetrieveReviewStatusRequest(self.request_adapter, path_parameters)

	def retrieve_snapshots(self,
		cloudPC_id: str,
	) -> RetrieveSnapshotsRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .retrieve_snapshots import RetrieveSnapshotsRequest
		return RetrieveSnapshotsRequest(self.request_adapter, path_parameters)

	def retry_partner_agent_installation(self,
		cloudPC_id: str,
	) -> RetryPartnerAgentInstallationRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .retry_partner_agent_installation import RetryPartnerAgentInstallationRequest
		return RetryPartnerAgentInstallationRequest(self.request_adapter, path_parameters)

	def set_review_status(self,
		cloudPC_id: str,
	) -> SetReviewStatusRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .set_review_status import SetReviewStatusRequest
		return SetReviewStatusRequest(self.request_adapter, path_parameters)

	def start(self,
		cloudPC_id: str,
	) -> StartRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .start import StartRequest
		return StartRequest(self.request_adapter, path_parameters)

	def stop(self,
		cloudPC_id: str,
	) -> StopRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .stop import StopRequest
		return StopRequest(self.request_adapter, path_parameters)

	def troubleshoot(self,
		cloudPC_id: str,
	) -> TroubleshootRequest:
		if cloudPC_id is None:
			raise TypeError("cloudPC_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["cloudPC%2Did"] =  cloudPC_id

		from .troubleshoot import TroubleshootRequest
		return TroubleshootRequest(self.request_adapter, path_parameters)

