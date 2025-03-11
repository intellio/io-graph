from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CertificateBasedApplicationConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	trustedCertificateAuthorities: Optional[list[CertificateAuthorityAsEntity]] = Field(alias="trustedCertificateAuthorities",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)

from .certificate_authority_as_entity import CertificateAuthorityAsEntity

