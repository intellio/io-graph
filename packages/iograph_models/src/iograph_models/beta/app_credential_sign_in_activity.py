from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AppCredentialSignInActivity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	appObjectId: Optional[str] = Field(alias="appObjectId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	credentialOrigin: Optional[ApplicationKeyOrigin | str] = Field(alias="credentialOrigin",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	keyId: Optional[str] = Field(alias="keyId",default=None,)
	keyType: Optional[ApplicationKeyType | str] = Field(alias="keyType",default=None,)
	keyUsage: Optional[ApplicationKeyUsage | str] = Field(alias="keyUsage",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	servicePrincipalObjectId: Optional[str] = Field(alias="servicePrincipalObjectId",default=None,)
	signInActivity: Optional[SignInActivity] = Field(alias="signInActivity",default=None,)

from .application_key_origin import ApplicationKeyOrigin
from .application_key_type import ApplicationKeyType
from .application_key_usage import ApplicationKeyUsage
from .sign_in_activity import SignInActivity

