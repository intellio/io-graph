from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ClientCertificateAuthentication(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	certificateList: list[Pkcs12CertificateInformation] = Field(alias="certificateList",)

from .pkcs12_certificate_information import Pkcs12CertificateInformation

