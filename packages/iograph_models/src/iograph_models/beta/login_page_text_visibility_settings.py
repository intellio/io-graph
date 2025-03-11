from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LoginPageTextVisibilitySettings(BaseModel):
	hideAccountResetCredentials: Optional[bool] = Field(alias="hideAccountResetCredentials",default=None,)
	hideCannotAccessYourAccount: Optional[bool] = Field(alias="hideCannotAccessYourAccount",default=None,)
	hideForgotMyPassword: Optional[bool] = Field(alias="hideForgotMyPassword",default=None,)
	hidePrivacyAndCookies: Optional[bool] = Field(alias="hidePrivacyAndCookies",default=None,)
	hideResetItNow: Optional[bool] = Field(alias="hideResetItNow",default=None,)
	hideTermsOfUse: Optional[bool] = Field(alias="hideTermsOfUse",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


