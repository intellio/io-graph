from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LoginPageTextVisibilitySettings(BaseModel):
	hideAccountResetCredentials: Optional[bool] = Field(default=None,alias="hideAccountResetCredentials",)
	hideCannotAccessYourAccount: Optional[bool] = Field(default=None,alias="hideCannotAccessYourAccount",)
	hideForgotMyPassword: Optional[bool] = Field(default=None,alias="hideForgotMyPassword",)
	hidePrivacyAndCookies: Optional[bool] = Field(default=None,alias="hidePrivacyAndCookies",)
	hideResetItNow: Optional[bool] = Field(default=None,alias="hideResetItNow",)
	hideTermsOfUse: Optional[bool] = Field(default=None,alias="hideTermsOfUse",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


