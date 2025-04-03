from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SelfServiceSignUp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.selfServiceSignUp"] = Field(alias="@odata.type", default="#microsoft.graph.selfServiceSignUp")
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	appliedEventListeners: Optional[list[AppliedAuthenticationEventListener]] = Field(alias="appliedEventListeners", default=None,)
	correlationId: Optional[str] = Field(alias="correlationId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	signUpIdentity: Optional[SignUpIdentity] = Field(alias="signUpIdentity", default=None,)
	signUpIdentityProvider: Optional[str] = Field(alias="signUpIdentityProvider", default=None,)
	signUpStage: Optional[SignUpStage | str] = Field(alias="signUpStage", default=None,)
	status: Optional[SignUpStatus] = Field(alias="status", default=None,)
	userSnapshot: Optional[CiamUserSnapshot] = Field(alias="userSnapshot", default=None,)

from .applied_authentication_event_listener import AppliedAuthenticationEventListener
from .sign_up_identity import SignUpIdentity
from .sign_up_stage import SignUpStage
from .sign_up_status import SignUpStatus
from .ciam_user_snapshot import CiamUserSnapshot
