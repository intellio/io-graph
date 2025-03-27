from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessSessionControls(BaseModel):
	applicationEnforcedRestrictions: Optional[ApplicationEnforcedRestrictionsSessionControl] = Field(alias="applicationEnforcedRestrictions", default=None,)
	cloudAppSecurity: Optional[CloudAppSecuritySessionControl] = Field(alias="cloudAppSecurity", default=None,)
	continuousAccessEvaluation: Optional[ContinuousAccessEvaluationSessionControl] = Field(alias="continuousAccessEvaluation", default=None,)
	disableResilienceDefaults: Optional[bool] = Field(alias="disableResilienceDefaults", default=None,)
	persistentBrowser: Optional[PersistentBrowserSessionControl] = Field(alias="persistentBrowser", default=None,)
	secureSignInSession: Optional[SecureSignInSessionControl] = Field(alias="secureSignInSession", default=None,)
	signInFrequency: Optional[SignInFrequencySessionControl] = Field(alias="signInFrequency", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .application_enforced_restrictions_session_control import ApplicationEnforcedRestrictionsSessionControl
from .cloud_app_security_session_control import CloudAppSecuritySessionControl
from .continuous_access_evaluation_session_control import ContinuousAccessEvaluationSessionControl
from .persistent_browser_session_control import PersistentBrowserSessionControl
from .secure_sign_in_session_control import SecureSignInSessionControl
from .sign_in_frequency_session_control import SignInFrequencySessionControl

