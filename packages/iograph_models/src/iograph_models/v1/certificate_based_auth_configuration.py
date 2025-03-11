from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CertificateBasedAuthConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	certificateAuthorities: Optional[list[CertificateAuthority]] = Field(alias="certificateAuthorities",default=None,)

from .certificate_authority import CertificateAuthority

