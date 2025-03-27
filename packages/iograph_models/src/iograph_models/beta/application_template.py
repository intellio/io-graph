from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApplicationTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	configurationUris: Optional[list[ConfigurationUri]] = Field(alias="configurationUris", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	homePageUrl: Optional[str] = Field(alias="homePageUrl", default=None,)
	informationalUrls: Optional[InformationalUrls] = Field(alias="informationalUrls", default=None,)
	logoUrl: Optional[str] = Field(alias="logoUrl", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	supportedClaimConfiguration: Optional[SupportedClaimConfiguration] = Field(alias="supportedClaimConfiguration", default=None,)
	supportedProvisioningTypes: Optional[list[str]] = Field(alias="supportedProvisioningTypes", default=None,)
	supportedSingleSignOnModes: Optional[list[str]] = Field(alias="supportedSingleSignOnModes", default=None,)

from .configuration_uri import ConfigurationUri
from .informational_urls import InformationalUrls
from .supported_claim_configuration import SupportedClaimConfiguration

