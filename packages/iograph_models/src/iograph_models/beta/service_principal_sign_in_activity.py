from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalSignInActivity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	applicationAuthenticationClientSignInActivity: Optional[SignInActivity] = Field(alias="applicationAuthenticationClientSignInActivity", default=None,)
	applicationAuthenticationResourceSignInActivity: Optional[SignInActivity] = Field(alias="applicationAuthenticationResourceSignInActivity", default=None,)
	delegatedClientSignInActivity: Optional[SignInActivity] = Field(alias="delegatedClientSignInActivity", default=None,)
	delegatedResourceSignInActivity: Optional[SignInActivity] = Field(alias="delegatedResourceSignInActivity", default=None,)
	lastSignInActivity: Optional[SignInActivity] = Field(alias="lastSignInActivity", default=None,)

from .sign_in_activity import SignInActivity
from .sign_in_activity import SignInActivity
from .sign_in_activity import SignInActivity
from .sign_in_activity import SignInActivity
from .sign_in_activity import SignInActivity

