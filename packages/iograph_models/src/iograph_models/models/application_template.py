from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ApplicationTemplate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	categories: list[Optional[str]] = Field(alias="categories",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	homePageUrl: Optional[str] = Field(default=None,alias="homePageUrl",)
	logoUrl: Optional[str] = Field(default=None,alias="logoUrl",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	supportedProvisioningTypes: list[Optional[str]] = Field(alias="supportedProvisioningTypes",)
	supportedSingleSignOnModes: list[Optional[str]] = Field(alias="supportedSingleSignOnModes",)


