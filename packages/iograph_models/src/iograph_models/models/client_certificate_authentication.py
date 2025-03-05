from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClientCertificateAuthentication(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	certificateList: Optional[list[Pkcs12CertificateInformation]] = Field(default=None,alias="certificateList",)

from .pkcs12_certificate_information import Pkcs12CertificateInformation

