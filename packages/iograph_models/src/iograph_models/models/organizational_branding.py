from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OrganizationalBranding(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	backgroundColor: Optional[str] = Field(default=None,alias="backgroundColor",)
	backgroundImage: Optional[str] = Field(default=None,alias="backgroundImage",)
	backgroundImageRelativeUrl: Optional[str] = Field(default=None,alias="backgroundImageRelativeUrl",)
	bannerLogo: Optional[str] = Field(default=None,alias="bannerLogo",)
	bannerLogoRelativeUrl: Optional[str] = Field(default=None,alias="bannerLogoRelativeUrl",)
	cdnList: Optional[list[str]] = Field(default=None,alias="cdnList",)
	contentCustomization: Optional[ContentCustomization] = Field(default=None,alias="contentCustomization",)
	customAccountResetCredentialsUrl: Optional[str] = Field(default=None,alias="customAccountResetCredentialsUrl",)
	customCannotAccessYourAccountText: Optional[str] = Field(default=None,alias="customCannotAccessYourAccountText",)
	customCannotAccessYourAccountUrl: Optional[str] = Field(default=None,alias="customCannotAccessYourAccountUrl",)
	customCSS: Optional[str] = Field(default=None,alias="customCSS",)
	customCSSRelativeUrl: Optional[str] = Field(default=None,alias="customCSSRelativeUrl",)
	customForgotMyPasswordText: Optional[str] = Field(default=None,alias="customForgotMyPasswordText",)
	customPrivacyAndCookiesText: Optional[str] = Field(default=None,alias="customPrivacyAndCookiesText",)
	customPrivacyAndCookiesUrl: Optional[str] = Field(default=None,alias="customPrivacyAndCookiesUrl",)
	customResetItNowText: Optional[str] = Field(default=None,alias="customResetItNowText",)
	customTermsOfUseText: Optional[str] = Field(default=None,alias="customTermsOfUseText",)
	customTermsOfUseUrl: Optional[str] = Field(default=None,alias="customTermsOfUseUrl",)
	favicon: Optional[str] = Field(default=None,alias="favicon",)
	faviconRelativeUrl: Optional[str] = Field(default=None,alias="faviconRelativeUrl",)
	headerBackgroundColor: Optional[str] = Field(default=None,alias="headerBackgroundColor",)
	headerLogo: Optional[str] = Field(default=None,alias="headerLogo",)
	headerLogoRelativeUrl: Optional[str] = Field(default=None,alias="headerLogoRelativeUrl",)
	loginPageLayoutConfiguration: Optional[LoginPageLayoutConfiguration] = Field(default=None,alias="loginPageLayoutConfiguration",)
	loginPageTextVisibilitySettings: Optional[LoginPageTextVisibilitySettings] = Field(default=None,alias="loginPageTextVisibilitySettings",)
	signInPageText: Optional[str] = Field(default=None,alias="signInPageText",)
	squareLogo: Optional[str] = Field(default=None,alias="squareLogo",)
	squareLogoDark: Optional[str] = Field(default=None,alias="squareLogoDark",)
	squareLogoDarkRelativeUrl: Optional[str] = Field(default=None,alias="squareLogoDarkRelativeUrl",)
	squareLogoRelativeUrl: Optional[str] = Field(default=None,alias="squareLogoRelativeUrl",)
	usernameHintText: Optional[str] = Field(default=None,alias="usernameHintText",)
	localizations: Optional[list[OrganizationalBrandingLocalization]] = Field(default=None,alias="localizations",)

from .content_customization import ContentCustomization
from .login_page_layout_configuration import LoginPageLayoutConfiguration
from .login_page_text_visibility_settings import LoginPageTextVisibilitySettings
from .organizational_branding_localization import OrganizationalBrandingLocalization

