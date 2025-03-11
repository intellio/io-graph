# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.schema_extension import SchemaExtension


class BySchemaExtensionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/schemaExtensions/{schemaExtension%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SchemaExtension:
		"""
		Get schemaExtension
		Get the properties of the specified schemaExtension definition.
		Find more info here: https://learn.microsoft.com/graph/api/schemaextension-get?view=graph-rest-beta
		"""
		tags = ['schemaExtensions.schemaExtension']

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
		return await self.request_adapter.send_async(request_info, SchemaExtension, error_mapping)

	async def patch(
		self,
		body: SchemaExtension,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SchemaExtension:
		"""
		Update schemaExtension
		Update properties in the definition of the specified schemaExtension. Additive updates to the extension can only be made when the extension is in the InDevelopment or Available status. This means custom properties or target resource types cannot be removed from the definition, but new custom properties can be added and the description of the extension changed. The update applies to all the resources that are included in the targetTypes property of the extension. These resources are among the supporting resource types. For delegated flows, the signed-in user can update a schema extension as long as the owner property of the extension is set to the appId of an application the signed-in user owns. That application can be the one that initially created the extension, or some other application owned by the signed-in user.  This criteria for the owner property allows a signed-in user to make updates through other applications they don't own, such as Microsoft Graph Explorer. When using Graph Explorer to update a schemaExtension resource, include the owner property in the PATCH request body.
		Find more info here: https://learn.microsoft.com/graph/api/schemaextension-update?view=graph-rest-beta
		"""
		tags = ['schemaExtensions.schemaExtension']

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
		return await self.request_adapter.send_async(request_info, SchemaExtension, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete schemaExtension
		Delete the definition of a schema extension. In app-only scenarios, only the app that created the schema extension (owner app) can delete the schema extension definition, and only when the extension is in the InDevelopment state. In delegated scenarios, the owner of the owner app can delete the schema extension definition, and only when the extension is in the InDevelopment state.  Deleting a schema extension definition before deleting the data associated with the extension in the target resources makes the data inaccessible. To recover the data, you can recreate the schema extension definition with the same configuration, but only if you used the verified domain for the schema extension id.
		Find more info here: https://learn.microsoft.com/graph/api/schemaextension-delete?view=graph-rest-beta
		"""
		tags = ['schemaExtensions.schemaExtension']
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



	def with_url(self, raw_url: str) -> BySchemaExtensionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySchemaExtensionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySchemaExtensionIdRequest(self.request_adapter, self.path_parameters)

