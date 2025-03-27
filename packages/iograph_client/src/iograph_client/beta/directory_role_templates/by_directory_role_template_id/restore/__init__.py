# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.restore_post_request import RestorePostRequest
from iograph_models.beta.directory_object import DirectoryObject


class RestoreRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directoryRoleTemplates/{directoryRoleTemplate%2Did}/restore", path_parameters)

	async def post(
		self,
		body: RestorePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DirectoryObject:
		"""
		Invoke action restore
		Restore a recently deleted directory object from deleted items. The following types are supported:
- administrativeUnit
- application
- certificateBasedAuthPki
- [certificateAuthorityDetail](../resources/certificateauthoritydetail.md
- externalUserProfile
- group
- pendingExternalUserProfile
- servicePrincipal
- user If an item was accidentally deleted, you can fully restore the item. This isn't applicable to security groups, which are deleted permanently. Also, restoring an application doesn't restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.
		Find more info here: https://learn.microsoft.com/graph/api/directory-deleteditems-restore?view=graph-rest-beta
		"""
		tags = ['directoryRoleTemplates.directoryRoleTemplate.Actions']

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
		return await self.request_adapter.send_async(request_info, DirectoryObject, error_mapping)


	def with_url(self, raw_url: str) -> RestoreRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RestoreRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RestoreRequest(self.request_adapter, self.path_parameters)

