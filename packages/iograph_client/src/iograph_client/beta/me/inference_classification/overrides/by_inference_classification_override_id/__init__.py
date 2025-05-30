# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.inference_classification_override import InferenceClassificationOverride


class ByInferenceClassificationOverrideIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/inferenceClassification/overrides/{inferenceClassificationOverride%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> InferenceClassificationOverride:
		"""
		Get overrides from me
		A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.
		"""
		tags = ['me.inferenceClassification']

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
		return await self.request_adapter.send_async(request_info, InferenceClassificationOverride, error_mapping)

	async def patch(
		self,
		body: InferenceClassificationOverride,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> InferenceClassificationOverride:
		"""
		Update inferenceClassificationOverride
		Change the classifyAs field of a focused Inbox override as specified. You cannot use PATCH to change any other fields in an inferenceClassificationOverride instance. If an override exists for a sender and the sender changes his/her display name, you can use POST to force an update to the name field in the existing override. If an override exists for a sender and the sender changes his/her SMTP address, deleting the existing override and creating a new one with
the new SMTP address is the only way to 'update' the override for this sender.
		Find more info here: https://learn.microsoft.com/graph/api/inferenceclassificationoverride-update?view=graph-rest-beta
		"""
		tags = ['me.inferenceClassification']

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
		return await self.request_adapter.send_async(request_info, InferenceClassificationOverride, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete inferenceClassificationOverride
		Delete a focused Inbox override specified by its ID.
		Find more info here: https://learn.microsoft.com/graph/api/inferenceclassificationoverride-delete?view=graph-rest-beta
		"""
		tags = ['me.inferenceClassification']
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



	def with_url(self, raw_url: str) -> ByInferenceClassificationOverrideIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByInferenceClassificationOverrideIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByInferenceClassificationOverrideIdRequest(self.request_adapter, self.path_parameters)

