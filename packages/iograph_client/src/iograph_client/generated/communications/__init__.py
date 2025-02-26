# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .presences import PresencesRequest
	from .online_meetings import OnlineMeetingsRequest
	from .get_presences_by_user_id import GetPresencesByUserIdRequest
	from .calls import CallsRequest
	from .call_records import CallRecordsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.cloud_communications import CloudCommunications


class CommunicationsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/communications"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CloudCommunications:
		"""
		Get communications
		
		"""
		tags = ['communications.cloudCommunications']

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
		return await self.request_adapter.send_async(request_info, CloudCommunications, error_mapping)

	async def patch(
		self,
		body: CloudCommunications,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CloudCommunications:
		"""
		Update communications
		
		"""
		tags = ['communications.cloudCommunications']

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
		return await self.request_adapter.send_async(request_info, CloudCommunications, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	@property
	def call_records(self,
	) -> CallRecordsRequest:
		from .call_records import CallRecordsRequest
		return CallRecordsRequest(self.request_adapter, self.path_parameters)

	@property
	def calls(self,
	) -> CallsRequest:
		from .calls import CallsRequest
		return CallsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_presences_by_user_id(self,
	) -> GetPresencesByUserIdRequest:
		from .get_presences_by_user_id import GetPresencesByUserIdRequest
		return GetPresencesByUserIdRequest(self.request_adapter, self.path_parameters)

	@property
	def online_meetings(self,
	) -> OnlineMeetingsRequest:
		from .online_meetings import OnlineMeetingsRequest
		return OnlineMeetingsRequest(self.request_adapter, self.path_parameters)

	@property
	def presences(self,
	) -> PresencesRequest:
		from .presences import PresencesRequest
		return PresencesRequest(self.request_adapter, self.path_parameters)

