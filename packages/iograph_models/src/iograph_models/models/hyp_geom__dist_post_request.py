from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Hyp_geom__distPostRequest(BaseModel):
	sampleS: Optional[str] = Field(default=None,alias="sampleS",)
	numberSample: Optional[str] = Field(default=None,alias="numberSample",)
	populationS: Optional[str] = Field(default=None,alias="populationS",)
	numberPop: Optional[str] = Field(default=None,alias="numberPop",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


