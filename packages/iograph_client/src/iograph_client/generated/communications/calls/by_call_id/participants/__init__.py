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
	from .invite import InviteRequest
	from .count import CountRequest
	from .by_participant_id import ByParticipantIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.participant import Participant
from iograph_models.models.participant_collection_response import ParticipantCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ParticipantsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/communications/calls/{call%2Did}/participants"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ParticipantCollectionResponse:
		"""
		List participants
		Retrieve a list of participant objects in the call.
		Find more info here: https://learn.microsoft.com/graph/api/call-list-participants?view=graph-rest-1.0
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_async(request_info, ParticipantCollectionResponse, error_mapping)

	async def post(
		self,
		body: Participant,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Participant:
		"""
		Create new navigation property to participants for communications
		
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_async(request_info, Participant, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_participant_id(self,
		call_id: str,
		participant_id: str,
	) -> ByParticipantIdRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")
		if participant_id is None:
			raise TypeError("participant_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id
		path_parameters["participant%2Did"] =  participant_id

		from .by_participant_id import ByParticipantIdRequest
		return ByParticipantIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def invite(self,
	) -> InviteRequest:
		from .invite import InviteRequest
		return InviteRequest(self.request_adapter, self.path_parameters)

