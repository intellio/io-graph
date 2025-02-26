from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Fido2AuthenticationMethod(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	aaGuid: Optional[str] = Field(default=None,alias="aaGuid",)
	attestationCertificates: list[Optional[str]] = Field(alias="attestationCertificates",)
	attestationLevel: Optional[AttestationLevel] = Field(default=None,alias="attestationLevel",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	model: Optional[str] = Field(default=None,alias="model",)

from .attestation_level import AttestationLevel

