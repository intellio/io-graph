from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateIssuerHintsConfiguration(BaseModel):
	state: Optional[X509CertificateIssuerHintsState | str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .x509_certificate_issuer_hints_state import X509CertificateIssuerHintsState
