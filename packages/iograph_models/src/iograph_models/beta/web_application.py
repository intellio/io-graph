from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WebApplication(BaseModel):
	homePageUrl: Optional[str] = Field(alias="homePageUrl", default=None,)
	implicitGrantSettings: Optional[ImplicitGrantSettings] = Field(alias="implicitGrantSettings", default=None,)
	logoutUrl: Optional[str] = Field(alias="logoutUrl", default=None,)
	oauth2AllowImplicitFlow: Optional[bool] = Field(alias="oauth2AllowImplicitFlow", default=None,)
	redirectUris: Optional[list[str]] = Field(alias="redirectUris", default=None,)
	redirectUriSettings: Optional[list[RedirectUriSettings]] = Field(alias="redirectUriSettings", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .implicit_grant_settings import ImplicitGrantSettings
from .redirect_uri_settings import RedirectUriSettings
