from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesExtensionAttributes(BaseModel):
	extensionAttribute1: Optional[str] = Field(alias="extensionAttribute1", default=None,)
	extensionAttribute10: Optional[str] = Field(alias="extensionAttribute10", default=None,)
	extensionAttribute11: Optional[str] = Field(alias="extensionAttribute11", default=None,)
	extensionAttribute12: Optional[str] = Field(alias="extensionAttribute12", default=None,)
	extensionAttribute13: Optional[str] = Field(alias="extensionAttribute13", default=None,)
	extensionAttribute14: Optional[str] = Field(alias="extensionAttribute14", default=None,)
	extensionAttribute15: Optional[str] = Field(alias="extensionAttribute15", default=None,)
	extensionAttribute2: Optional[str] = Field(alias="extensionAttribute2", default=None,)
	extensionAttribute3: Optional[str] = Field(alias="extensionAttribute3", default=None,)
	extensionAttribute4: Optional[str] = Field(alias="extensionAttribute4", default=None,)
	extensionAttribute5: Optional[str] = Field(alias="extensionAttribute5", default=None,)
	extensionAttribute6: Optional[str] = Field(alias="extensionAttribute6", default=None,)
	extensionAttribute7: Optional[str] = Field(alias="extensionAttribute7", default=None,)
	extensionAttribute8: Optional[str] = Field(alias="extensionAttribute8", default=None,)
	extensionAttribute9: Optional[str] = Field(alias="extensionAttribute9", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

