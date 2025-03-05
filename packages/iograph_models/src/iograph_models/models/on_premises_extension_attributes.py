from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesExtensionAttributes(BaseModel):
	extensionAttribute1: Optional[str] = Field(default=None,alias="extensionAttribute1",)
	extensionAttribute10: Optional[str] = Field(default=None,alias="extensionAttribute10",)
	extensionAttribute11: Optional[str] = Field(default=None,alias="extensionAttribute11",)
	extensionAttribute12: Optional[str] = Field(default=None,alias="extensionAttribute12",)
	extensionAttribute13: Optional[str] = Field(default=None,alias="extensionAttribute13",)
	extensionAttribute14: Optional[str] = Field(default=None,alias="extensionAttribute14",)
	extensionAttribute15: Optional[str] = Field(default=None,alias="extensionAttribute15",)
	extensionAttribute2: Optional[str] = Field(default=None,alias="extensionAttribute2",)
	extensionAttribute3: Optional[str] = Field(default=None,alias="extensionAttribute3",)
	extensionAttribute4: Optional[str] = Field(default=None,alias="extensionAttribute4",)
	extensionAttribute5: Optional[str] = Field(default=None,alias="extensionAttribute5",)
	extensionAttribute6: Optional[str] = Field(default=None,alias="extensionAttribute6",)
	extensionAttribute7: Optional[str] = Field(default=None,alias="extensionAttribute7",)
	extensionAttribute8: Optional[str] = Field(default=None,alias="extensionAttribute8",)
	extensionAttribute9: Optional[str] = Field(default=None,alias="extensionAttribute9",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


