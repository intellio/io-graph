# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.get_member_objects_post_response import Get_member_objectsPostResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.get_member_objects_post_request import Get_member_objectsPostRequest


class GetMemberObjectsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/contacts/{orgContact%2Did}/getMemberObjects"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Get_member_objectsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Get_member_objectsPostResponse:
		"""
		Invoke action getMemberObjects
		Return all IDs for the groups, administrative units, and directory roles that an object of one of the following types is a member of:
- user
- group
- service principal
- organizational contact
- device
- directory object This function is transitive. Only users and role-enabled groups can be members of directory roles.
		Find more info here: https://learn.microsoft.com/graph/api/directoryobject-getmemberobjects?view=graph-rest-1.0
		"""
		tags = ['contacts.orgContact.Actions']

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
		return await self.request_adapter.send_async(request_info, Get_member_objectsPostResponse, error_mapping)


