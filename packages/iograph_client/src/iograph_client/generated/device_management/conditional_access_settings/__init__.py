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
from iograph_models.models.on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ConditionalAccessSettingsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/conditionalAccessSettings"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnPremisesConditionalAccessSettings:
		"""
		Get onPremisesConditionalAccessSettings
		Read properties and relationships of the onPremisesConditionalAccessSettings object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-onpremisesconditionalaccesssettings-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.onPremisesConditionalAccessSettings']

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
		return await self.request_adapter.send_async(request_info, OnPremisesConditionalAccessSettings, error_mapping)

	async def patch(
		self,
		body: OnPremisesConditionalAccessSettings,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnPremisesConditionalAccessSettings:
		"""
		Update onPremisesConditionalAccessSettings
		Update the properties of a onPremisesConditionalAccessSettings object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-onpremisesconditionalaccesssettings-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.onPremisesConditionalAccessSettings']

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
		return await self.request_adapter.send_async(request_info, OnPremisesConditionalAccessSettings, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property conditionalAccessSettings for deviceManagement
		
		"""
		tags = ['deviceManagement.onPremisesConditionalAccessSettings']
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



