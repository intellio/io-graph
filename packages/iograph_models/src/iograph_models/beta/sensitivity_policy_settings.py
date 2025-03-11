from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SensitivityPolicySettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	applicableTo: Optional[SensitivityLabelTarget | str] = Field(alias="applicableTo",default=None,)
	downgradeSensitivityRequiresJustification: Optional[bool] = Field(alias="downgradeSensitivityRequiresJustification",default=None,)
	helpWebUrl: Optional[str] = Field(alias="helpWebUrl",default=None,)
	isMandatory: Optional[bool] = Field(alias="isMandatory",default=None,)

from .sensitivity_label_target import SensitivityLabelTarget

