from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WebApplication(BaseModel):
	homePageUrl: Optional[str] = Field(default=None,alias="homePageUrl",)
	implicitGrantSettings: Optional[ImplicitGrantSettings] = Field(default=None,alias="implicitGrantSettings",)
	logoutUrl: Optional[str] = Field(default=None,alias="logoutUrl",)
	redirectUris: Optional[list[str]] = Field(default=None,alias="redirectUris",)
	redirectUriSettings: Optional[list[RedirectUriSettings]] = Field(default=None,alias="redirectUriSettings",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .implicit_grant_settings import ImplicitGrantSettings
from .redirect_uri_settings import RedirectUriSettings

