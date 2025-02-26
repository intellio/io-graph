from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessSessionControls(BaseModel):
	applicationEnforcedRestrictions: Optional[ApplicationEnforcedRestrictionsSessionControl] = Field(default=None,alias="applicationEnforcedRestrictions",)
	cloudAppSecurity: Optional[CloudAppSecuritySessionControl] = Field(default=None,alias="cloudAppSecurity",)
	disableResilienceDefaults: Optional[bool] = Field(default=None,alias="disableResilienceDefaults",)
	persistentBrowser: Optional[PersistentBrowserSessionControl] = Field(default=None,alias="persistentBrowser",)
	signInFrequency: Optional[SignInFrequencySessionControl] = Field(default=None,alias="signInFrequency",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .application_enforced_restrictions_session_control import ApplicationEnforcedRestrictionsSessionControl
from .cloud_app_security_session_control import CloudAppSecuritySessionControl
from .persistent_browser_session_control import PersistentBrowserSessionControl
from .sign_in_frequency_session_control import SignInFrequencySessionControl

