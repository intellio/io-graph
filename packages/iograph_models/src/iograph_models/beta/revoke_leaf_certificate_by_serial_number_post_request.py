from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Revoke_leaf_certificate_by_serial_numberPostRequest(BaseModel):
	certificateSerialNumber: Optional[str] = Field(alias="certificateSerialNumber", default=None,)

