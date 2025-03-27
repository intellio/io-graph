from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OrganizationalBrandingLocalization(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.organizationalBrandingLocalization"] = Field(alias="@odata.type", default="#microsoft.graph.organizationalBrandingLocalization")
	backgroundColor: Optional[str] = Field(alias="backgroundColor", default=None,)
	backgroundImage: Optional[str] = Field(alias="backgroundImage", default=None,)
	backgroundImageRelativeUrl: Optional[str] = Field(alias="backgroundImageRelativeUrl", default=None,)
	bannerLogo: Optional[str] = Field(alias="bannerLogo", default=None,)
	bannerLogoRelativeUrl: Optional[str] = Field(alias="bannerLogoRelativeUrl", default=None,)
	cdnList: Optional[list[str]] = Field(alias="cdnList", default=None,)
	contentCustomization: Optional[ContentCustomization] = Field(alias="contentCustomization", default=None,)
	customAccountResetCredentialsUrl: Optional[str] = Field(alias="customAccountResetCredentialsUrl", default=None,)
	customCannotAccessYourAccountText: Optional[str] = Field(alias="customCannotAccessYourAccountText", default=None,)
	customCannotAccessYourAccountUrl: Optional[str] = Field(alias="customCannotAccessYourAccountUrl", default=None,)
	customCSS: Optional[str] = Field(alias="customCSS", default=None,)
	customCSSRelativeUrl: Optional[str] = Field(alias="customCSSRelativeUrl", default=None,)
	customForgotMyPasswordText: Optional[str] = Field(alias="customForgotMyPasswordText", default=None,)
	customPrivacyAndCookiesText: Optional[str] = Field(alias="customPrivacyAndCookiesText", default=None,)
	customPrivacyAndCookiesUrl: Optional[str] = Field(alias="customPrivacyAndCookiesUrl", default=None,)
	customResetItNowText: Optional[str] = Field(alias="customResetItNowText", default=None,)
	customTermsOfUseText: Optional[str] = Field(alias="customTermsOfUseText", default=None,)
	customTermsOfUseUrl: Optional[str] = Field(alias="customTermsOfUseUrl", default=None,)
	favicon: Optional[str] = Field(alias="favicon", default=None,)
	faviconRelativeUrl: Optional[str] = Field(alias="faviconRelativeUrl", default=None,)
	headerBackgroundColor: Optional[str] = Field(alias="headerBackgroundColor", default=None,)
	headerLogo: Optional[str] = Field(alias="headerLogo", default=None,)
	headerLogoRelativeUrl: Optional[str] = Field(alias="headerLogoRelativeUrl", default=None,)
	loginPageLayoutConfiguration: Optional[LoginPageLayoutConfiguration] = Field(alias="loginPageLayoutConfiguration", default=None,)
	loginPageTextVisibilitySettings: Optional[LoginPageTextVisibilitySettings] = Field(alias="loginPageTextVisibilitySettings", default=None,)
	signInPageText: Optional[str] = Field(alias="signInPageText", default=None,)
	squareLogo: Optional[str] = Field(alias="squareLogo", default=None,)
	squareLogoDark: Optional[str] = Field(alias="squareLogoDark", default=None,)
	squareLogoDarkRelativeUrl: Optional[str] = Field(alias="squareLogoDarkRelativeUrl", default=None,)
	squareLogoRelativeUrl: Optional[str] = Field(alias="squareLogoRelativeUrl", default=None,)
	usernameHintText: Optional[str] = Field(alias="usernameHintText", default=None,)

from .content_customization import ContentCustomization
from .login_page_layout_configuration import LoginPageLayoutConfiguration
from .login_page_text_visibility_settings import LoginPageTextVisibilitySettings

