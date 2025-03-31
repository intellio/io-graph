from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class Get_planPostRequest(BaseModel):
	target: Optional[Union[BusinessScenarioGroupTarget]] = Field(alias="target", default=None,discriminator="odata_type", )

from .business_scenario_group_target import BusinessScenarioGroupTarget
