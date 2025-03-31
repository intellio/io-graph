from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Fido2AuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fido2AuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.fido2AuthenticationMethod")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	aaGuid: Optional[str] = Field(alias="aaGuid", default=None,)
	attestationCertificates: Optional[list[str]] = Field(alias="attestationCertificates", default=None,)
	attestationLevel: Optional[AttestationLevel | str] = Field(alias="attestationLevel", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	publicKeyCredential: Optional[WebauthnPublicKeyCredential] = Field(alias="publicKeyCredential", default=None,)

from .attestation_level import AttestationLevel
from .webauthn_public_key_credential import WebauthnPublicKeyCredential
