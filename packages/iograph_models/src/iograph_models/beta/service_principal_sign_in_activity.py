from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServicePrincipalSignInActivity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.servicePrincipalSignInActivity"] = Field(alias="@odata.type",)
	appId: Optional[str] = Field(alias="appId", default=None,)
	applicationAuthenticationClientSignInActivity: Optional[SignInActivity] = Field(alias="applicationAuthenticationClientSignInActivity", default=None,)
	applicationAuthenticationResourceSignInActivity: Optional[SignInActivity] = Field(alias="applicationAuthenticationResourceSignInActivity", default=None,)
	delegatedClientSignInActivity: Optional[SignInActivity] = Field(alias="delegatedClientSignInActivity", default=None,)
	delegatedResourceSignInActivity: Optional[SignInActivity] = Field(alias="delegatedResourceSignInActivity", default=None,)
	lastSignInActivity: Optional[SignInActivity] = Field(alias="lastSignInActivity", default=None,)

from .sign_in_activity import SignInActivity
