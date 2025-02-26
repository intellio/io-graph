from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaContentRatingUnitedStates(BaseModel):
	movieRating: Optional[RatingUnitedStatesMoviesType] = Field(default=None,alias="movieRating",)
	tvRating: Optional[RatingUnitedStatesTelevisionType] = Field(default=None,alias="tvRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rating_united_states_movies_type import RatingUnitedStatesMoviesType
from .rating_united_states_television_type import RatingUnitedStatesTelevisionType

