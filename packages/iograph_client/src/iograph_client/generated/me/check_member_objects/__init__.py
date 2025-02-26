# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.check_member_objects_post_response import Check_member_objectsPostResponse
from iograph_models.models.check_member_objects_post_request import Check_member_objectsPostRequest


class CheckMemberObjectsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/checkMemberObjects"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Check_member_objectsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Check_member_objectsPostResponse:
		"""
		Invoke action checkMemberObjects
		Check for membership in a list of group IDs, administrative unit IDs, or directory role IDs, for the IDs of the specified 
- user
- group
- service principal
- organizational contact
- device
- directory object. This method is transitive.
		"""
		tags = ['me.user.Actions']

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
		return await self.request_adapter.send_async(request_info, Check_member_objectsPostResponse, error_mapping)


