from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MutualTlsOauthConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	certificateAuthorities: Optional[list[CertificateAuthority]] = Field(alias="certificateAuthorities",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	tlsClientAuthParameter: Optional[TlsClientRegistrationMetadata | str] = Field(alias="tlsClientAuthParameter",default=None,)

from .certificate_authority import CertificateAuthority
from .tls_client_registration_metadata import TlsClientRegistrationMetadata

