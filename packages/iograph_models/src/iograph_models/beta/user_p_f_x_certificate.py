from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserPFXCertificate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	encryptedPfxBlob: Optional[str] = Field(alias="encryptedPfxBlob",default=None,)
	encryptedPfxPassword: Optional[str] = Field(alias="encryptedPfxPassword",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	intendedPurpose: Optional[UserPfxIntendedPurpose | str] = Field(alias="intendedPurpose",default=None,)
	keyName: Optional[str] = Field(alias="keyName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	paddingScheme: Optional[UserPfxPaddingScheme | str] = Field(alias="paddingScheme",default=None,)
	providerName: Optional[str] = Field(alias="providerName",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	thumbprint: Optional[str] = Field(alias="thumbprint",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)

from .user_pfx_intended_purpose import UserPfxIntendedPurpose
from .user_pfx_padding_scheme import UserPfxPaddingScheme

