from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SensitivityPolicySettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sensitivityPolicySettings"] = Field(alias="@odata.type",)
	applicableTo: Optional[SensitivityLabelTarget | str] = Field(alias="applicableTo", default=None,)
	downgradeSensitivityRequiresJustification: Optional[bool] = Field(alias="downgradeSensitivityRequiresJustification", default=None,)
	helpWebUrl: Optional[str] = Field(alias="helpWebUrl", default=None,)
	isMandatory: Optional[bool] = Field(alias="isMandatory", default=None,)

from .sensitivity_label_target import SensitivityLabelTarget
