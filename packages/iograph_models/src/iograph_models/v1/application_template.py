from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ApplicationTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.applicationTemplate"] = Field(alias="@odata.type",)
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	homePageUrl: Optional[str] = Field(alias="homePageUrl", default=None,)
	logoUrl: Optional[str] = Field(alias="logoUrl", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	supportedProvisioningTypes: Optional[list[str]] = Field(alias="supportedProvisioningTypes", default=None,)
	supportedSingleSignOnModes: Optional[list[str]] = Field(alias="supportedSingleSignOnModes", default=None,)

