from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesProvisioningError(BaseModel):
	category: Optional[str] = Field(alias="category", default=None,)
	occurredDateTime: Optional[datetime] = Field(alias="occurredDateTime", default=None,)
	propertyCausingError: Optional[str] = Field(alias="propertyCausingError", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


