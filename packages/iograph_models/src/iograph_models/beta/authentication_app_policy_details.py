from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationAppPolicyDetails(BaseModel):
	adminConfiguration: Optional[AuthenticationAppAdminConfiguration | str] = Field(alias="adminConfiguration",default=None,)
	authenticationEvaluation: Optional[AuthenticationAppEvaluation | str] = Field(alias="authenticationEvaluation",default=None,)
	policyName: Optional[str] = Field(alias="policyName",default=None,)
	status: Optional[AuthenticationAppPolicyStatus | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_app_admin_configuration import AuthenticationAppAdminConfiguration
from .authentication_app_evaluation import AuthenticationAppEvaluation
from .authentication_app_policy_status import AuthenticationAppPolicyStatus

