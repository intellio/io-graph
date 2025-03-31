from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Hyp_geom__distPostRequest(BaseModel):
	sampleS: Optional[str] = Field(alias="sampleS", default=None,)
	numberSample: Optional[str] = Field(alias="numberSample", default=None,)
	populationS: Optional[str] = Field(alias="populationS", default=None,)
	numberPop: Optional[str] = Field(alias="numberPop", default=None,)
	cumulative: Optional[str] = Field(alias="cumulative", default=None,)

