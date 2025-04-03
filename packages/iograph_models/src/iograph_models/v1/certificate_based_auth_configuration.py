from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CertificateBasedAuthConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.certificateBasedAuthConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.certificateBasedAuthConfiguration")
	certificateAuthorities: Optional[list[CertificateAuthority]] = Field(alias="certificateAuthorities", default=None,)

from .certificate_authority import CertificateAuthority
