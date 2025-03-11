from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppManagementPolicyActorExemptions(BaseModel):
	customSecurityAttributes: SerializeAsAny[Optional[list[CustomSecurityAttributeExemption]]] = Field(alias="customSecurityAttributes",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .custom_security_attribute_exemption import CustomSecurityAttributeExemption

