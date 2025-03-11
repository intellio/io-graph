from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Validate_xmlPostRequest(BaseModel):
	officeConfigurationXml: Optional[str] = Field(alias="officeConfigurationXml",default=None,)


