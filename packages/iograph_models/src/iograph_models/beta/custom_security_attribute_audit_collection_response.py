from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomSecurityAttributeAuditCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CustomSecurityAttributeAudit]] = Field(alias="value", default=None,)

from .custom_security_attribute_audit import CustomSecurityAttributeAudit

