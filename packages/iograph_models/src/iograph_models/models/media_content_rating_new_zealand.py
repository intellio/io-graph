from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingNewZealand(BaseModel):
	movieRating: Optional[RatingNewZealandMoviesType] = Field(default=None,alias="movieRating",)
	tvRating: Optional[RatingNewZealandTelevisionType] = Field(default=None,alias="tvRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rating_new_zealand_movies_type import RatingNewZealandMoviesType
from .rating_new_zealand_television_type import RatingNewZealandTelevisionType

