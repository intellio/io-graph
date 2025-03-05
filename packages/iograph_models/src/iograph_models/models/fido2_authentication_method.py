from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Fido2AuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	aaGuid: Optional[str] = Field(alias="aaGuid",default=None,)
	attestationCertificates: Optional[list[str]] = Field(alias="attestationCertificates",default=None,)
	attestationLevel: Optional[str | AttestationLevel] = Field(alias="attestationLevel",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)

from .attestation_level import AttestationLevel

