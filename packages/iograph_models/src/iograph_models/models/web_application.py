from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WebApplication(BaseModel):
	homePageUrl: Optional[str] = Field(default=None,alias="homePageUrl",)
	implicitGrantSettings: Optional[ImplicitGrantSettings] = Field(default=None,alias="implicitGrantSettings",)
	logoutUrl: Optional[str] = Field(default=None,alias="logoutUrl",)
	redirectUris: list[str] = Field(alias="redirectUris",)
	redirectUriSettings: list[RedirectUriSettings] = Field(alias="redirectUriSettings",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .implicit_grant_settings import ImplicitGrantSettings
from .redirect_uri_settings import RedirectUriSettings

